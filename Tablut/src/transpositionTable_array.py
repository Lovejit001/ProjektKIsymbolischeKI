from src import config
import math
import numpy as np  # Optional: für effizienteres Array, falls verfügbar

class TTableEntry:
    """Einzelner Eintrag in der Transposition Table"""
    __slots__ = ('hash_key', 'score', 'depth', 'flag', 'best_move')
    
    def __init__(self, hash_key=0, score=0, depth=0, flag='', best_move=None):
        self.hash_key = hash_key      # Zobrist-Key (oder vollständiger Hash)
        self.score = score            # Berechneter Wert
        self.depth = depth            # Verbleibende Suchtiefe
        self.flag = flag              # 'exact', 'lower', 'upper'
        self.best_move = best_move    # Bester Zug für diese Position


class ArrayTranspositionTable:
    """
    Array-basierte Transposition Table mit direkter Adressierung.
    Verwendet ein lineares Array von Einträgen (keine Verkettung).
    
    Vorteile:
    - Extrem schneller Zugriff (O(1) mit minimalem Overhead)
    - Cache-freundlich durch lineare Speicheranordnung
    - Kein Python-Dictionary-Overhead
    
    Nachteile:
    - Feste Größe muss im Voraus bekannt sein
    - Hash-Kollisionen führen zu Überschreiben
    """
    
    def __init__(self, size_mb=64):  # Standard: 64 MB
        """
        Initialisiert die Transposition Table mit einem Array fester Größe.
        
        Args:
            size_mb: Größe in Megabytes (ca. 80 MB = 1 Million Einträge)
        """
        # Ein Eintrag benötigt ca. 72 Bytes (bei __slots__ etwas weniger)
        # 1 Million Einträge ≈ 72 MB + Overhead
        entry_size_bytes = 72  # Schätzwert pro Eintrag
        num_entries = (size_mb * 1024 * 1024) // entry_size_bytes
        
        self.size = num_entries
        self.table = [None] * self.size  # Array mit None initialisiert
        self.hits = 0
        self.misses = 0
        
        # Für die generation-basierte Ersetzung (optional)
        self.generation = 0
        self.entry_generation = [0] * self.size  # Altersmarkierung
        
        print(f"[TT] Initialisiert mit {self.size:,} Einträgen (~{size_mb} MB)")
    
    def _get_index(self, hash_key):
        """
        Berechnet den Index im Array aus dem Hash-Key.
        Verwendet Modulo-Operation (Zweierpotenz-Optimierung möglich).
        """
        # Optimierung: Wenn size eine Zweierpotenz ist, kann modulo durch & ersetzt werden
        # if (self.size & (self.size - 1)) == 0:  # Prüfen ob Zweierpotenz
        #     return hash_key & (self.size - 1)
        return hash_key % self.size
    
    def get_hash(self, board, onTurn):
        """
        Erstellt einen eindeutigen Hash für die aktuelle Position.
        ACHTUNG: Die Tiefe wird NICHT mehr Teil des Hash-Keys!
        Die Tiefe wird im Entry gespeichert und beim Lookup verglichen.
        
        Returns:
            Integer-Hash-Wert für die Position
        """
        board_tuple = tuple(tuple(row) for row in board)
        # Hash aus Board und Spieler (ohne depth!)
        return hash((board_tuple, onTurn))
    
    def lookup(self, board, depth, alpha, beta, onTurn):
        """
        Sucht in der Tabelle nach einer gespeicherten Position.
        
        Returns:
            (found, score, flag, best_move)
        """
        pos_hash = self.get_hash(board, onTurn)
        index = self._get_index(pos_hash)
        
        entry = self.table[index]
        
        if entry is not None and entry.hash_key == pos_hash:
            # Hash stimmt überein -> potentiell gültiger Eintrag
            self.hits += 1
            
            # Prüfe ob die gespeicherte Tiefe ausreicht
            if entry.depth < depth:
                # Gespeicherte Tiefe ist geringer, nicht verwendbar
                return False, None, None, None
            
            # Prüfe ob der gespeicherte Wert innerhalb der aktuellen Alpha-Beta-Grenzen liegt
            if entry.flag == 'exact':
                # Exakter Wert ist immer gültig
                return True, entry.score, entry.flag, entry.best_move
            
            elif entry.flag == 'lower':
                # Lower Bound: gespeicherter Wert ist <= tatsächlicher Wert
                # Kann verwendet werden wenn entry.score >= beta
                if entry.score >= beta:
                    return True, entry.score, entry.flag, entry.best_move
            
            elif entry.flag == 'upper':
                # Upper Bound: gespeicherter Wert ist >= tatsächlicher Wert
                # Kann verwendet werden wenn entry.score <= alpha
                if entry.score <= alpha:
                    return True, entry.score, entry.flag, entry.best_move
            
            # Sonst: Wert nicht direkt verwendbar aufgrund geänderter Alpha-Beta-Grenzen
        
        self.misses += 1
        return False, None, None, None
    
    def store(self, board, depth, score, flag, best_move, onTurn):
        """
        Speichert eine berechnete Position in der Tabelle.
        Verwendet eine depth-preferred Ersetzungsstrategie.
        
        Args:
            board: Aktuelles Board
            depth: Verbleibende Suchtiefe
            score: Berechneter Wert
            flag: 'exact', 'lower', 'upper'
            best_move: Bester Zug für diese Position
            onTurn: Wer am Zug ist
        """
        pos_hash = self.get_hash(board, onTurn)
        index = self._get_index(pos_hash)
        
        current_entry = self.table[index]
        
        # Entscheide ob überschrieben werden soll (depth-preferred)
        should_replace = False
        
        if current_entry is None:
            # Slot ist leer -> speichern
            should_replace = True
        elif current_entry.hash_key != pos_hash:
            # Hash-Kollision: depth-preferred Entscheidung
            # Speichere nur wenn neue Tiefe >= gespeicherte Tiefe
            if depth >= current_entry.depth:
                should_replace = True
            # Ansonsten: Behalte den vorhandenen (tieferen) Eintrag
        else:
            # Gleiche Position: überschreibe wenn neue Tiefe >= alte Tiefe
            if depth >= current_entry.depth:
                should_replace = True
        
        if should_replace:
            self.table[index] = TTableEntry(
                hash_key=pos_hash,
                score=score,
                depth=depth,
                flag=flag,
                best_move=best_move
            )
            # Optional: Generation für altersbasierte Ersetzung aktualisieren
            self.entry_generation[index] = self.generation
    
    def store_always(self, board, depth, score, flag, best_move, onTurn):
        """
        Alternative: Always-replace Strategie (immer überschreiben).
        Für Vergleichszwecke mit der Dictionary-Version.
        """
        pos_hash = self.get_hash(board, onTurn)
        index = self._get_index(pos_hash)
        
        self.table[index] = TTableEntry(
            hash_key=pos_hash,
            score=score,
            depth=depth,
            flag=flag,
            best_move=best_move
        )
    
    def new_game(self):
        """Startet eine neue Partie (erhöht Generation für altersbasierte Ersetzung)"""
        self.generation += 1
        # Optional: Alte Einträge ungültig machen (z.B. Generation check beim Lookup)
        # Dafür müsste man beim Lookup auch die Generation prüfen
    
    def clear(self):
        """Löscht die gesamte Tabelle"""
        self.table = [None] * self.size
        self.entry_generation = [0] * self.size
        self.hits = 0
        self.misses = 0
        self.generation = 0
    
    def get_stats(self):
        """Gibt Statistik zurück"""
        total = self.hits + self.misses
        hit_rate = (self.hits / total * 100) if total > 0 else 0
        
        # Zähle belegte Einträge (für Füllgrad)
        used = sum(1 for entry in self.table if entry is not None)
        fill_rate = (used / self.size * 100) if self.size > 0 else 0
        
        return {
            'size': self.size,
            'used': used,
            'fill_rate': fill_rate,
            'hits': self.hits,
            'misses': self.misses,
            'hit_rate': hit_rate
        }
    
    def set_size(self, size_mb):
        """Ändert die Größe der Tabelle (löscht dabei alle Einträge)"""
        entry_size_bytes = 72
        num_entries = (size_mb * 1024 * 1024) // entry_size_bytes
        self.size = num_entries
        self.table = [None] * self.size
        self.entry_generation = [0] * self.size
        self.clear()


# Für bessere Performance: Verwende array.array für primitive Typen
class CompactArrayTranspositionTable(ArrayTranspositionTable):
    """
    Kompakte Array-Version mit separaten Arrays für primitive Typen.
    Noch cache-freundlicher und speichereffizienter.
    """
    
    def __init__(self, size_mb=64):
        import array
        
        # Größenberechnung
        entry_size_bytes = 32  # Optimierte Schätzung für primitive Typen
        num_entries = (size_mb * 1024 * 1024) // entry_size_bytes
        
        self.size = num_entries
        
        # Separate Arrays für jeden Feldtyp (cache-freundlicher)
        self.hash_keys = array.array('Q', [0]) * self.size  # unsigned long long (8 bytes)
        self.scores = array.array('h', [0]) * self.size     # signed short (2 bytes)
        self.depths = array.array('b', [0]) * self.size     # signed char (1 byte)
        self.flags = array.array('b', [0]) * self.size      # 0=empty,1=exact,2=lower,3=upper
        self.best_moves = [None] * self.size                # Nur Züge als Referenzen
        
        self.hits = 0
        self.misses = 0
        
        print(f"[TT] Kompakte Tabelle initialisiert mit {self.size:,} Einträgen (~{size_mb} MB)")
    
    def _encode_flag(self, flag):
        """Konvertiert String-Flag in Integer"""
        return {'exact': 1, 'lower': 2, 'upper': 3}.get(flag, 0)
    
    def _decode_flag(self, code):
        """Konvertiert Integer-Flag zurück in String"""
        return {1: 'exact', 2: 'lower', 3: 'upper'}.get(code, '')
    
    def lookup(self, board, depth, alpha, beta, onTurn):
        pos_hash = self.get_hash(board, onTurn)
        index = self._get_index(pos_hash)
        
        # Prüfe ob Eintrag existiert (hash_key != 0)
        if self.hash_keys[index] == 0:
            self.misses += 1
            return False, None, None, None
        
        # Verifiziere vollständigen Hash (gegen Kollisionen)
        if self.hash_keys[index] != pos_hash:
            self.misses += 1
            return False, None, None, None
        
        self.hits += 1
        
        # Prüfe Tiefe
        if self.depths[index] < depth:
            return False, None, None, None
        
        score = self.scores[index]
        flag = self._decode_flag(self.flags[index])
        
        # Alpha-Beta Prüfungen
        if flag == 'exact':
            return True, score, flag, self.best_moves[index]
        elif flag == 'lower':
            if score >= beta:
                return True, score, flag, self.best_moves[index]
        elif flag == 'upper':
            if score <= alpha:
                return True, score, flag, self.best_moves[index]
        
        return False, None, None, None
    
    def store(self, board, depth, score, flag, best_move, onTurn):
        pos_hash = self.get_hash(board, onTurn)
        index = self._get_index(pos_hash)
        
        # depth-preferred Entscheidung
        current_depth = self.depths[index]
        current_hash = self.hash_keys[index]
        
        should_replace = False
        if current_hash == 0:  # Leerer Slot
            should_replace = True
        elif current_hash != pos_hash:  # Kollision
            if depth >= current_depth:
                should_replace = True
        else:  # Gleiche Position
            if depth >= current_depth:
                should_replace = True
        
        if should_replace:
            self.hash_keys[index] = pos_hash
            self.scores[index] = score
            self.depths[index] = depth
            self.flags[index] = self._encode_flag(flag)
            self.best_moves[index] = best_move
    
    def clear(self):
        import array
        self.hash_keys = array.array('Q', [0]) * self.size
        self.scores = array.array('h', [0]) * self.size
        self.depths = array.array('b', [0]) * self.size
        self.flags = array.array('b', [0]) * self.size
        self.best_moves = [None] * self.size
        self.hits = 0
        self.misses = 0


# Globale Instanz (ersetzen Sie die alte mit dieser)
# trans_table = ArrayTranspositionTable(size_mb=128)  # 128 MB für bessere Performance