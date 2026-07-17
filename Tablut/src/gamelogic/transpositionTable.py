from src.gamelogic import config
import math

class TranspositionTable:
    """Speichert bereits berechnete Positionen für Alpha-Beta-Suche"""
    
    def __init__(self):
        self.table = {}  # Hash -> Eintrag
        self.hits = 0    # Statistik: Anzahl erfolgreicher Treffer
        self.misses = 0  # Statistik: Anzahl Fehlversuche
    
    def get_hash(self, board, depth, alpha, beta, onTurn):
        """
        Erstellt einen eindeutigen Hash für die aktuelle Position.
        Kombiniert aus:
        - Board-Zustand (als Tupel)
        - Aktueller Spieler (onTurn)
        - Tiefe (depth) - wichtig für unterschiedliche Suchtiefen
        """
        board_tuple = tuple(tuple(row) for row in board)
        # Einfacher Hash aus Board und Spieler
        return hash((board_tuple, onTurn, depth))
    
    def lookup(self, board, depth, alpha, beta, onTurn):
        """
        Sucht in der Tabelle nach einer gespeicherten Position.
        
        Returns:
            (found, score, flag, best_move)
            found:  True/False ob Eintrag existiert
            score:  Berechneter Wert
            flag:   'exact', 'lower', 'upper' (Art des Eintrags)
            best_move: Gespeicherter bester Zug für diese Position
        """
        pos_hash = self.get_hash(board, depth, alpha, beta, onTurn)
        
        if pos_hash in self.table:
            self.hits += 1
            entry = self.table[pos_hash]
            
            # === DEBUG: Ausgabe des Eintrags ===
            #print("DEBUG: entry =", entry)
            #print("DEBUG: Typ von entry =", type(entry))
            # =================================

            # Prüfe ob die gespeicherte Tiefe ausreicht
            if entry['depth'] < depth:
                # Gespeicherte Tiefe ist geringer, nicht verwendbar
                return False, None, None, None
            
            # Prüfe ob der gespeicherte Wert innerhalb der aktuellen Alpha-Beta-Grenzen liegt
            if entry['flag'] == 'exact':
                # Exakter Wert ist immer gültig
                return True, entry['score'], entry['flag'], entry.get('best_move')
            
            elif entry['flag'] == 'lower':
                # Lower Bound: gespeicherter Wert ist <= tatsächlicher Wert
                # Kann verwendet werden wenn entry['score'] >= beta
                if entry['score'] >= beta:
                    return True, entry['score'], entry['flag'], entry.get('best_move')
            
            elif entry['flag'] == 'upper':
                # Upper Bound: gespeicherter Wert ist >= tatsächlicher Wert
                # Kann verwendet werden wenn entry['score'] <= alpha
                if entry['score'] <= alpha:
                    return True, entry['score'], entry['flag'], entry.get('best_move')
            
            # Sonst: Wert nicht direkt verwendbar aufgrund geänderter Alpha-Beta-Grenzen
        
        self.misses += 1
        return False, None, None, None
    
    def store(self, board, depth, score, flag, best_move, onTurn):
        """
        Speichert eine berechnete Position in der Tabelle.
        
        Args:
            board: Aktuelles Board
            depth: Verbleibende Suchtiefe
            score: Berechneter Wert
            flag: 'exact', 'lower', 'upper'
            best_move: Bester Zug für diese Position
            onTurn: Wer am Zug ist
        """
        pos_hash = self.get_hash(board, depth, None, None, onTurn)
        
        # Größenbegrenzung (1 Million Einträge)
        MAX_SIZE = 1000000
        if len(self.table) > MAX_SIZE:
            # Lösche 10% der ältesten Einträge
            items_to_remove = len(self.table) // 10
            keys_to_remove = list(self.table.keys())[:items_to_remove]
            for key in keys_to_remove:
                del self.table[key]
        
        self.table[pos_hash] = {
            'score': score,
            'flag': flag,
            'depth': depth,
            'best_move': best_move
        }

        #ZUSATZZ: !!!
        #self.table[pos_hash] = {...}
        #if len(self.table) % 1000 == 0:
        #    print(f"[TT] Store, size={len(self.table)}")
    
    def clear(self):
        """Löscht die gesamte Tabelle"""
        self.table.clear()
        self.hits = 0
        self.misses = 0
    
    def get_stats(self):
        """Gibt Statistik zurück"""
        total = self.hits + self.misses
        hit_rate = (self.hits / total * 100) if total > 0 else 0
        return {
            'size': len(self.table),
            'hits': self.hits,
            'misses': self.misses,
            'hit_rate': hit_rate
        }

# Globale Instanz für die Verwendung in alphaBeta.py
trans_table = TranspositionTable()