import unittest
from src.gamelogic import config

"""
Hier werden die Unit Tests für die Funktionen in config.py definiert.
Getestet werden:
- reset_pieces(): Setzt alle Piece-Zähler zurück
- init_pieces(): Initialisiert die Piece-Zähler basierend auf dem Board
- reset_time(): Setzt Zeitvariablen zurück
- account_move(): Erhöht Zugzähler
- Globale Variablen: Korrekte Initialisierung
"""

class TestConfig(unittest.TestCase):
    
    def setUp(self):
        """Setzt den Zustand vor jedem Test zurück."""
        config.reset_pieces()
        config.reset_time()
    
    # ========== Globale Variablen Tests ==========
    
    def test_global_variables_initialized(self):
        """Prüft ob alle globalen Variablen korrekt initialisiert sind."""
        self.assertEqual(config.B_pieces, 0, "B_pieces sollte 0 sein")
        self.assertEqual(config.W_pieces, 0, "W_pieces sollte 0 sein")
        self.assertEqual(config.K_pieces, 0, "K_pieces sollte 0 sein")
        self.assertEqual(config.zugRegel, 0, "zugRegel sollte 0 sein")
        self.assertEqual(config.zugCounter, 0, "zugCounter sollte 0 sein")
        self.assertEqual(config.eval_counter, 0, "eval_counter sollte 0 sein")
        self.assertEqual(config.onTurn, "Black", "onTurn sollte 'Black' sein")
        self.assertIsNone(config.bestMove, "bestMove sollte None sein")
        self.assertEqual(config.search_start, 0.0, "search_start sollte 0.0 sein")
        self.assertEqual(config.stop_time, 0.0, "stop_time sollte 0.0 sein")
        self.assertEqual(config.nodes, 0, "nodes sollte 0 sein")
        self.assertFalse(config.stop_search, "stop_search sollte False sein")
        print("Globale Variablen korrekt initialisiert")
    
    def test_constants_defined(self):
        """Prüft ob alle Konstanten korrekt definiert sind."""
        self.assertEqual(config.W, 'W', "W sollte 'W' sein")
        self.assertEqual(config.K, 'K', "K sollte 'K' sein")
        self.assertEqual(config.B, 'B', "B sollte 'B' sein")
        self.assertEqual(config.Throne, (4, 4), "Throne sollte (4,4) sein")
        self.assertEqual(len(config.Goal), 4, "Goal sollte 4 Eckfelder enthalten")
        self.assertEqual(len(config.Edge), 28, "Edge sollte 28 Randfelder enthalten")
        print("Konstanten korrekt definiert")
    
    # ========== reset_pieces() Tests ==========
    
    def test_reset_pieces(self):
        """Prüft ob reset_pieces alle Piece-Zähler zurücksetzt."""
        # Werte setzen
        config.B_pieces = 10
        config.W_pieces = 5
        config.K_pieces = 1
        config.zugRegel = 20
        config.zugCounter = 15
        config.eval_counter = 100
        config.onTurn = "White"
        config.bestMove = ((0, 0), (1, 1))
        config.boardHash = ["hash1", "hash2"]
        
        # Zurücksetzen
        config.reset_pieces()
        
        # Prüfen
        self.assertEqual(config.B_pieces, 0)
        self.assertEqual(config.W_pieces, 0)
        self.assertEqual(config.K_pieces, 0)
        self.assertEqual(config.zugRegel, 0)
        self.assertEqual(config.zugCounter, 0)
        self.assertEqual(config.eval_counter, 0)
        self.assertEqual(config.onTurn, "Black")
        self.assertIsNone(config.bestMove)
        print("reset_pieces setzt alle Werte korrekt zurück")
    
    # ========== init_pieces() Tests ==========
    
    def test_init_pieces_starting_board(self):
        """Prüft ob init_pieces die Startstellung korrekt zählt."""
        board = [
            [0, 0, 0, config.B, config.B, config.B, 0, 0, 0],
            [0, 0, 0, 0, config.B, 0, 0, 0, 0],
            [0, 0, 0, 0, config.W, 0, 0, 0, 0],
            [config.B, 0, 0, 0, config.W, 0, 0, 0, config.B],
            [config.B, config.B, config.W, config.W, config.K, config.W, config.W, config.B, config.B],
            [config.B, 0, 0, 0, config.W, 0, 0, 0, config.B],
            [0, 0, 0, 0, config.W, 0, 0, 0, 0],
            [0, 0, 0, 0, config.B, 0, 0, 0, 0],
            [0, 0, 0, config.B, config.B, config.B, 0, 0, 0]
        ]
        
        config.init_pieces(board)
        
        self.assertEqual(config.B_pieces, 16, "Startstellung hat 16 schwarze Figuren")
        self.assertEqual(config.W_pieces, 9, "Startstellung hat 8 weiße + 1 König = 9")
        self.assertEqual(config.K_pieces, 1, "Startstellung hat 1 König")
        print("init_pieces zählt Startstellung korrekt")
    
    def test_init_pieces_empty_board(self):
        """Prüft ob init_pieces mit leerem Board korrekt zählt."""
        board = [[0]*9 for _ in range(9)]
        
        config.init_pieces(board)
        
        self.assertEqual(config.B_pieces, 0, "Leeres Board hat 0 schwarze Figuren")
        self.assertEqual(config.W_pieces, 0, "Leeres Board hat 0 weiße Figuren")
        self.assertEqual(config.K_pieces, 0, "Leeres Board hat 0 Könige")
        print("init_pieces mit leerem Board korrekt")
    
    def test_init_pieces_only_king(self):
        """Prüft ob init_pieces nur mit König korrekt zählt."""
        board = [[0]*9 for _ in range(9)]
        board[4][4] = config.K
        
        config.init_pieces(board)
        
        self.assertEqual(config.B_pieces, 0)
        self.assertEqual(config.W_pieces, 1)
        self.assertEqual(config.K_pieces, 1)
        print("init_pieces mit nur König korrekt")
    
    def test_init_pieces_only_white(self):
        """Prüft ob init_pieces nur mit weißen Figuren korrekt zählt."""
        board = [[0]*9 for _ in range(9)]
        board[4][2] = config.W
        board[4][3] = config.W
        board[4][5] = config.W
        
        config.init_pieces(board)
        
        self.assertEqual(config.B_pieces, 0)
        self.assertEqual(config.W_pieces, 3)
        self.assertEqual(config.K_pieces, 0)
        print("init_pieces mit nur weißen Figuren korrekt")
    
    def test_init_pieces_only_black(self):
        """Prüft ob init_pieces nur mit schwarzen Figuren korrekt zählt."""
        board = [[0]*9 for _ in range(9)]
        board[0][3] = config.B
        board[0][4] = config.B
        board[0][5] = config.B
        
        config.init_pieces(board)
        
        self.assertEqual(config.B_pieces, 3)
        self.assertEqual(config.W_pieces, 0)
        self.assertEqual(config.K_pieces, 0)
        print("init_pieces mit nur schwarzen Figuren korrekt")
    
    def test_init_pieces_mixed(self):
        """Prüft ob init_pieces mit gemischten Figuren korrekt zählt."""
        board = [[0]*9 for _ in range(9)]
        board[4][4] = config.K
        board[4][2] = config.W
        board[4][3] = config.W
        board[0][3] = config.B
        board[0][4] = config.B
        
        config.init_pieces(board)
        
        self.assertEqual(config.B_pieces, 2)
        self.assertEqual(config.W_pieces, 3)  # 2 weiße + 1 König
        self.assertEqual(config.K_pieces, 1)
        print("init_pieces mit gemischten Figuren korrekt")
    
    # ========== reset_time() Tests ==========
    
    def test_reset_time(self):
        """Prüft ob reset_time alle Zeitvariablen zurücksetzt."""
        # Werte setzen
        config.search_start = 10.5
        config.stop_time = 20.3
        config.nodes = 100
        config.stop_search = True
        
        config.reset_time()
        
        self.assertEqual(config.search_start, 0.0)
        self.assertEqual(config.stop_time, 0.0)
        self.assertEqual(config.nodes, 0)
        self.assertFalse(config.stop_search)
        print("reset_time setzt Zeitvariablen korrekt zurück")
    
    def test_reset_time_after_use(self):
        """Prüft ob reset_time nach Benutzung korrekt zurücksetzt."""
        config.search_start = 5.2
        config.stop_time = 10.1
        config.nodes = 50
        config.stop_search = True
        
        config.reset_time()
        
        self.assertEqual(config.search_start, 0.0)
        self.assertEqual(config.stop_time, 0.0)
        self.assertEqual(config.nodes, 0)
        self.assertFalse(config.stop_search)
        print("reset_time nach Benutzung korrekt")
    
    # ========== account_move() Tests ==========
    
    def test_account_move(self):
        """Prüft ob account_move die Zähler korrekt erhöht."""
        config.zugCounter = 0
        config.zugRegel = 0
        
        config.account_move()
        
        self.assertEqual(config.zugCounter, 1)
        self.assertEqual(config.zugRegel, 1)
        print("account_move erhöht Zähler korrekt")
    
    def test_account_move_multiple(self):
        """Prüft ob account_move bei mehreren Aufrufen korrekt zählt."""
        config.zugCounter = 0
        config.zugRegel = 0
        
        for _ in range(5):
            config.account_move()
        
        self.assertEqual(config.zugCounter, 5)
        self.assertEqual(config.zugRegel, 5)
        print("account_move bei mehreren Aufrufen korrekt")
    
    def test_account_move_after_reset(self):
        """Prüft ob account_move nach reset korrekt funktioniert."""
        config.zugCounter = 10
        config.zugRegel = 10
        
        config.reset_pieces()
        
        config.account_move()
        
        self.assertEqual(config.zugCounter, 1)
        self.assertEqual(config.zugRegel, 1)
        print("account_move nach reset korrekt")
    
    # ========== Kombinierte Tests ==========

    
    def test_reset_time_preserves_pieces(self):
        """Prüft ob reset_time Piece-Zähler nicht verändert."""
        config.B_pieces = 16
        config.W_pieces = 9
        config.K_pieces = 1
        
        config.reset_time()
        
        self.assertEqual(config.B_pieces, 16)
        self.assertEqual(config.W_pieces, 9)
        self.assertEqual(config.K_pieces, 1)
        print("reset_time verändert Piece-Zähler nicht")
    
    def test_full_reset_sequence(self):
        """Prüft ob eine vollständige Reset-Sequenz korrekt funktioniert."""
        # Board mit Figuren
        board = [[0]*9 for _ in range(9)]
        board[4][4] = config.K
        board[4][2] = config.W
        board[0][3] = config.B
        
        # Initialisieren
        config.init_pieces(board)
        config.account_move()
        config.account_move()
        
        # Werte vor Reset
        self.assertEqual(config.B_pieces, 1)
        self.assertEqual(config.W_pieces, 2)
        self.assertEqual(config.K_pieces, 1)
        self.assertEqual(config.zugCounter, 2)
        
        # Reset
        config.reset_pieces()
        config.reset_time()
        
        # Werte nach Reset
        self.assertEqual(config.B_pieces, 0)
        self.assertEqual(config.W_pieces, 0)
        self.assertEqual(config.K_pieces, 0)
        self.assertEqual(config.zugCounter, 0)
        self.assertEqual(config.zugRegel, 0)
        self.assertEqual(config.search_start, 0.0)
        print("Vollständige Reset-Sequenz korrekt")

if __name__ == '__main__':
    unittest.main()