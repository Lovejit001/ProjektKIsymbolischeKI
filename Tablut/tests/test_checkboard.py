import unittest
from src.gamelogic import config
from src.gamelogic.checkBoard import checkBoard2, recent_moves, getHash
from tests.definitions import starting_board

"""
Hier werden die Unit Tests für die Funktionen in checkBoard.py definiert.
Getestet werden:
- checkBoard2(): Spielstandprüfung (Sieg, Niederlage, Remis, laufendes Spiel)
- recent_moves(): 3-fache Stellungswiederholung
- getHash(): Hash-Erstellung für Boards
"""

class TestCheckBoard(unittest.TestCase):
    
    def setUp(self):
        """Setzt den Zustand vor jedem Test zurück."""
        config.reset_pieces()
        config.K_pieces = 1
        config.B_pieces = 16
        config.W_pieces = 8
        config.zugRegel = 0
        config.boardHash = []
    
    def test_checkBoard_king_captured(self):
        """Prüft ob -1 zurückgegeben wird wenn der König geschlagen wurde."""
        config.K_pieces = 0
        board = [[0]*9 for _ in range(9)]
        result = checkBoard2(board)
        self.assertEqual(result, -1, "König geschlagen -> Schwarz gewinnt (-1)")
        print(f"✓ König geschlagen -> Schwarz gewinnt")
    
    def test_checkBoard_king_on_corner(self):
        """Prüft ob 1 zurückgegeben wird wenn der König auf einem Eckfeld steht."""
        board = [[0]*9 for _ in range(9)]
        # König auf Eckfeld (0,0)
        board[0][0] = config.K
        result = checkBoard2(board)
        self.assertEqual(result, 1, "König auf Eckfeld -> Weiß gewinnt (1)")
        print(f"✓ König auf Eckfeld -> Weiß gewinnt")
    
    def test_checkBoard_king_on_other_corner(self):
        """Prüft ob 1 zurückgegeben wird wenn der König auf einem anderen Eckfeld steht."""
        board = [[0]*9 for _ in range(9)]
        # König auf Eckfeld (0,8)
        board[0][8] = config.K
        result = checkBoard2(board)
        self.assertEqual(result, 1, "König auf Eckfeld (0,8) -> Weiß gewinnt (1)")
        print(f"✓ König auf anderem Eckfeld -> Weiß gewinnt")
    
    def test_checkBoard_no_black_pieces(self):
        """Prüft ob 1 zurückgegeben wird wenn keine schwarzen Figuren mehr vorhanden sind."""
        config.B_pieces = 0
        board = [[0]*9 for _ in range(9)]
        board[4][4] = config.K
        result = checkBoard2(board)
        self.assertEqual(result, 1, "Keine schwarzen Figuren -> Weiß gewinnt (1)")
        print(f"✓ Keine schwarzen Figuren -> Weiß gewinnt")
    
    def test_checkBoard_no_white_pieces(self):
        """Prüft ob -1 zurückgegeben wird wenn keine weißen Figuren mehr vorhanden sind."""
        config.W_pieces = 0
        board = [[0]*9 for _ in range(9)]
        board[4][4] = config.K
        result = checkBoard2(board)
        self.assertEqual(result, -1, "Keine weißen Figuren -> Schwarz gewinnt (-1)")
        print(f"✓ Keine weißen Figuren -> Schwarz gewinnt")
    
    def test_checkBoard_draw_50_moves(self):
        """Prüft ob 0 zurückgegeben wird bei 50 Zügen ohne Schlag."""
        config.zugRegel = 50
        board = [[0]*9 for _ in range(9)]
        board[4][4] = config.K
        result = checkBoard2(board)
        self.assertEqual(result, 0, "50 Züge ohne Schlag -> Remis (0)")
        print(f"✓ 50 Züge ohne Schlag -> Remis")
    
    def test_checkBoard_no_pieces_error(self):
        """Prüft ob 0 zurückgegeben wird wenn keine Figuren auf dem Board sind."""
        config.B_pieces = 0
        config.W_pieces = 0
        config.K_pieces = 0
        board = [[0]*9 for _ in range(9)]
        result = checkBoard2(board)
        self.assertEqual(result, 0, "Keine Figuren -> Fehler (0)")
        print(f"✓ Keine Figuren -> Fehler")
    
    def test_checkBoard_multiple_kings_error(self):
        """Prüft ob 0 zurückgegeben wird wenn mehrere Könige auf dem Board sind."""
        config.K_pieces = 2
        board = [[0]*9 for _ in range(9)]
        board[4][4] = config.K
        board[4][5] = config.K
        result = checkBoard2(board)
        self.assertEqual(result, 0, "Mehrere Könige -> Fehler (0)")
        print(f"✓ Mehrere Könige -> Fehler")
    
    def test_checkBoard_game_continues(self):
        """Prüft ob -2 zurückgegeben wird wenn das Spiel weitergeht."""
        config.K_pieces = 1
        config.B_pieces = 5
        config.W_pieces = 3
        config.zugRegel = 10
        board = [[0]*9 for _ in range(9)]
        board[4][4] = config.K
        board[3][4] = config.W
        board[4][3] = config.B
        result = checkBoard2(board)
        self.assertEqual(result, -2, "Spiel läuft weiter (-2)")
        print(f"✓ Spiel läuft weiter")
    
    def test_getHash_returns_tuple(self):
        """Prüft ob getHash ein Tupel von Tupeln zurückgibt."""
        board = [[0]*9 for _ in range(9)]
        board[4][4] = config.K
        board[0][0] = config.W
        result = getHash(board)
        self.assertIsInstance(result, tuple, "getHash gibt Tupel zurück")
        self.assertIsInstance(result[0], tuple, "getHash gibt Tupel von Tupeln zurück")
        print(f"✓ getHash gibt korrekten Typ zurück")
    
    def test_getHash_consistency(self):
        """Prüft ob getHash für gleiche Boards gleiche Hashes liefert."""
        board1 = [[0]*9 for _ in range(9)]
        board1[4][4] = config.K
        board1[3][4] = config.W
        
        board2 = [[0]*9 for _ in range(9)]
        board2[4][4] = config.K
        board2[3][4] = config.W
        
        hash1 = getHash(board1)
        hash2 = getHash(board2)
        self.assertEqual(hash1, hash2, "Gleiche Boards -> gleiche Hashes")
        print(f"✓ getHash ist konsistent")
    
    def test_getHash_different_boards(self):
        """Prüft ob getHash für unterschiedliche Boards unterschiedliche Hashes liefert."""
        board1 = [[0]*9 for _ in range(9)]
        board1[4][4] = config.K
        
        board2 = [[0]*9 for _ in range(9)]
        board2[4][4] = config.K
        board2[3][4] = config.W
        
        hash1 = getHash(board1)
        hash2 = getHash(board2)
        self.assertNotEqual(hash1, hash2, "Unterschiedliche Boards -> unterschiedliche Hashes")
        print(f"✓ getHash unterscheidet Boards")
    
    def test_recent_moves_no_repetition(self):
        """Prüft ob recent_moves False zurückgibt bei keiner Wiederholung."""
        board = [[0]*9 for _ in range(9)]
        board[4][4] = config.K
        config.boardHash = [getHash(board)]
        result = recent_moves(board)
        self.assertFalse(result, "Keine 3-fache Wiederholung -> False")
        print(f"✓ Keine Stellungswiederholung -> False")
    
    def test_recent_moves_single_repetition(self):
        """Prüft ob recent_moves False zurückgibt bei einfacher Wiederholung."""
        board = [[0]*9 for _ in range(9)]
        board[4][4] = config.K
        hash_val = getHash(board)
        config.boardHash = [hash_val, hash_val]
        result = recent_moves(board)
        self.assertFalse(result, "Nur 2-fache Wiederholung -> False")
        print(f"✓ Einfache Wiederholung -> False")
    
    def test_recent_moves_triple_repetition(self):
        """Prüft ob recent_moves True zurückgibt bei 3-facher Wiederholung."""
        board = [[0]*9 for _ in range(9)]
        board[4][4] = config.K
        hash_val = getHash(board)
        config.boardHash = [hash_val, hash_val, hash_val]
        result = recent_moves(board)
        self.assertTrue(result, "3-fache Wiederholung -> True")
        print(f"✓ 3-fache Wiederholung -> True")
    
    def test_recent_moves_more_than_triple(self):
        """Prüft ob recent_moves True zurückgibt bei mehr als 3-facher Wiederholung."""
        board = [[0]*9 for _ in range(9)]
        board[4][4] = config.K
        hash_val = getHash(board)
        config.boardHash = [hash_val, hash_val, hash_val, hash_val, hash_val]
        result = recent_moves(board)
        self.assertTrue(result, "Mehr als 3-fache Wiederholung -> True")
        print(f"✓ Mehrfache Wiederholung -> True")
    
    def test_checkBoard_king_on_corner_with_other_pieces(self):
        """Prüft ob 1 zurückgegeben wird wenn König auf Eckfeld steht (mit anderen Figuren)."""
        board = [[0]*9 for _ in range(9)]
        board[0][0] = config.K
        board[4][4] = config.W
        board[4][3] = config.B
        config.K_pieces = 1
        config.B_pieces = 1
        config.W_pieces = 1
        result = checkBoard2(board)
        self.assertEqual(result, 1, "König auf Eckfeld (mit anderen Figuren) -> Weiß gewinnt (1)")
        print(f"✓ König auf Eckfeld mit anderen Figuren -> Weiß gewinnt")
    
    def test_checkBoard_king_not_on_corner_continues(self):
        """Prüft ob -2 zurückgegeben wird wenn König nicht auf Eckfeld steht."""
        board = [[0]*9 for _ in range(9)]
        board[4][4] = config.K
        board[3][4] = config.W
        board[4][3] = config.B
        config.K_pieces = 1
        config.B_pieces = 1
        config.W_pieces = 1
        config.zugRegel = 10
        result = checkBoard2(board)
        self.assertEqual(result, -2, "König nicht auf Eckfeld -> Spiel läuft weiter (-2)")
        print(f"✓ König nicht auf Eckfeld -> Spiel läuft weiter")


if __name__ == '__main__':
    unittest.main()