import unittest
import io
import sys
from src.gamelogic import config
from src.gamelogic.debug import (
    print_dic,
    print_board1,
    print_board,
    print_possible_Moves,
    print_board_colorful,
    FenToBoard,
    fen_to_array,
    countMoves
)

"""
Hier werden die Unit Tests für die Funktionen in debug.py definiert.
Getestet werden:
- print_dic(): Dictionary-Ausgabe
- print_board1(): Einfache Board-Ausgabe
- print_board(): Farbige Board-Ausgabe
- print_possible_Moves(): Mögliche Züge Ausgabe
- print_board_colorful(): Farbige Board-Ausgabe mit Vergleich
- FenToBoard(): FEN-String zu Board konvertieren
- fen_to_array(): FEN zu 2D-Array
- countMoves(): Anzahl der Züge zählen
"""

class TestDebug(unittest.TestCase):
    
    def setUp(self):
        """Setzt den Zustand vor jedem Test zurück."""
        config.reset_pieces()
        config.K_pieces = 1
        config.B_pieces = 16
        config.W_pieces = 8
        config.zugRegel = 0
        config.zugCounter = 0
        config.onTurn = 'Black'
    
    # ========== print_dic() Tests ==========
    
    def test_print_dic(self):
        """Prüft ob print_dic Dictionary korrekt ausgibt."""
        test_dict = {"a": 1, "b": 2, "c": 3}
        captured_output = io.StringIO()
        sys.stdout = captured_output
        try:
            print_dic(test_dict)
            output = captured_output.getvalue()
            self.assertIn("a: 1,", output)
            self.assertIn("b: 2,", output)
            self.assertIn("c: 3,", output)
            print("print_dic funktioniert")
        finally:
            sys.stdout = sys.__stdout__
    
    def test_print_dic_empty(self):
        """Prüft ob print_dic mit leerem Dictionary läuft."""
        test_dict = {}
        captured_output = io.StringIO()
        sys.stdout = captured_output
        try:
            print_dic(test_dict)
            output = captured_output.getvalue()
            self.assertEqual(output.strip(), "")
            print("print_dic mit leerem Dict funktioniert")
        finally:
            sys.stdout = sys.__stdout__
    
    # ========== print_board1() Tests ==========
    
    def test_print_board1(self):
        """Prüft ob print_board1 Board korrekt ausgibt."""
        board = [[0]*9 for _ in range(9)]
        board[4][4] = config.K
        board[3][4] = config.W
        board[4][3] = config.B
        captured_output = io.StringIO()
        sys.stdout = captured_output
        try:
            print_board1(board)
            output = captured_output.getvalue()
            self.assertIn("K", output)
            self.assertIn("W", output)
            self.assertIn("B", output)
            print("print_board1 funktioniert")
        finally:
            sys.stdout = sys.__stdout__
    
    def test_print_board1_empty(self):
        """Prüft ob print_board1 mit leerem Board läuft."""
        board = [[0]*9 for _ in range(9)]
        captured_output = io.StringIO()
        sys.stdout = captured_output
        try:
            print_board1(board)
            output = captured_output.getvalue()
            self.assertIn("0", output)
            print("print_board1 mit leerem Board funktioniert")
        finally:
            sys.stdout = sys.__stdout__
    
    # ========== print_board() Tests ==========
    
    def test_print_board(self):
        """Prüft ob print_board mit Farben korrekt ausgibt."""
        board = [[0]*9 for _ in range(9)]
        board[4][4] = config.K
        board[3][4] = config.W
        board[4][3] = config.B
        captured_output = io.StringIO()
        sys.stdout = captured_output
        try:
            print_board(board)
            output = captured_output.getvalue()
            self.assertIn("K", output)
            self.assertIn("W", output)
            self.assertIn("B", output)
            print("print_board funktioniert")
        finally:
            sys.stdout = sys.__stdout__
    
    def test_print_board_empty(self):
        """Prüft ob print_board mit leerem Board läuft."""
        board = [[0]*9 for _ in range(9)]
        captured_output = io.StringIO()
        sys.stdout = captured_output
        try:
            print_board(board)
            output = captured_output.getvalue()
            self.assertIn("0", output)
            print("print_board mit leerem Board funktioniert")
        finally:
            sys.stdout = sys.__stdout__
    
    # ========== print_possible_Moves() Tests ==========
    
    
    def test_print_possible_moves_empty(self):
        """Prüft ob print_possible_Moves mit leerem Dictionary läuft."""
        moves = {}
        captured_output = io.StringIO()
        sys.stdout = captured_output
        try:
            print_possible_Moves(moves)
            output = captured_output.getvalue()
            self.assertEqual(output.strip(), "")
            print("print_possible_Moves mit leerem Dict funktioniert")
        finally:
            sys.stdout = sys.__stdout__
    
    
    # ========== print_board_colorful() Tests ==========
    
    def test_print_board_colorful(self):
        """Prüft ob print_board_colorful mit altem Board läuft."""
        board = [[0]*9 for _ in range(9)]
        board[4][4] = config.K
        board[3][4] = config.W
        board[4][3] = config.B
        
        old_board = [[0]*9 for _ in range(9)]
        old_board[4][4] = config.K
        
        captured_output = io.StringIO()
        sys.stdout = captured_output
        try:
            print_board_colorful(board, old_board)
            output = captured_output.getvalue()
            self.assertIn("K", output)
            print("print_board_colorful mit altem Board funktioniert")
        finally:
            sys.stdout = sys.__stdout__
    
    def test_print_board_colorful_no_old(self):
        """Prüft ob print_board_colorful ohne old_board läuft."""
        board = [[0]*9 for _ in range(9)]
        board[4][4] = config.K
        
        captured_output = io.StringIO()
        sys.stdout = captured_output
        try:
            print_board_colorful(board, None)
            output = captured_output.getvalue()
            self.assertIn("K", output)
            print("print_board_colorful ohne altes Board funktioniert")
        finally:
            sys.stdout = sys.__stdout__
    
    def test_print_board_colorful_empty(self):
        """Prüft ob print_board_colorful mit leerem Board läuft."""
        board = [[0]*9 for _ in range(9)]
        old_board = [[0]*9 for _ in range(9)]
        captured_output = io.StringIO()
        sys.stdout = captured_output
        try:
            print_board_colorful(board, old_board)
            output = captured_output.getvalue()
            self.assertIn("0", output)
            print("print_board_colorful mit leerem Board funktioniert")
        finally:
            sys.stdout = sys.__stdout__
    
    # ========== FenToBoard() Tests ==========
    
    def test_fen_to_board_starting(self):
        """Prüft ob FenToBoard die Startstellung korrekt konvertiert."""
        fen = "3aaa3/4a4/4d4/a3d3a/aaddkddaa/a3d3a/4d4/4a4/3aaa3 a 0 0"
        board, side = FenToBoard(fen)
        
        self.assertEqual(board[4][4], config.K, "Koenig sollte auf (4,4) sein")
        self.assertEqual(board[4][2], config.W, "Weisse Figur sollte auf (4,2) sein")
        self.assertEqual(board[0][3], config.B, "Schwarze Figur sollte auf (0,3) sein")
        self.assertEqual(side, 'a', "Seite sollte 'a' sein")
        print("FenToBoard konvertiert Startstellung korrekt")
    
    def test_fen_to_board_empty(self):
        """Prueft ob FenToBoard mit leerem String die Startstellung liefert."""
        board, side = FenToBoard("")
        self.assertEqual(board[4][4], config.K, "Koenig sollte auf (4,4) sein")
        self.assertEqual(board[4][2], config.W, "Weisse Figur sollte auf (4,2) sein")
        print("FenToBoard mit leerem String liefert Startstellung")
    
    def test_fen_to_board_custom(self):
        """Prueft ob FenToBoard ein benutzerdefiniertes Board konvertiert."""
        fen = "9/9/9/9/4k4/9/9/9/9 a 0 0"
        board, side = FenToBoard(fen)
        self.assertEqual(board[4][4], config.K, "Koenig sollte auf (4,4) sein")
        self.assertEqual(side, 'a', "Seite sollte 'a' sein")
        print("FenToBoard konvertiert benutzerdefiniertes Board")
    
    def test_fen_to_board_invalid(self):
        """Prueft ob FenToBoard bei ungueltigem FEN eine Exception wirft."""
        with self.assertRaises(ValueError):
            FenToBoard("invalid")
        print("FenToBoard wirft Exception bei ungueltigem FEN")
    
    def test_fen_to_board_side_black(self):
        """Prueft ob FenToBoard 'a' als Black erkennt."""
        fen = "9/9/9/9/9/9/9/9/9 a 0 0"
        board, side = FenToBoard(fen)
        self.assertEqual(side, 'a', "Seite sollte 'a' (Black) sein")
        print("FenToBoard erkennt 'a' als Black")
    
    def test_fen_to_board_sets_config(self):
        """Prueft ob FenToBoard config-Variablen setzt."""
        fen = "3aaa3/4a4/4d4/a3d3a/aaddkddaa/a3d3a/4d4/4a4/3aaa3 a 5 10"
        board, side = FenToBoard(fen)
        self.assertEqual(config.zugRegel, 5, "zugRegel sollte 5 sein")
        self.assertEqual(config.zugCounter, 10, "zugCounter sollte 10 sein")
        print("FenToBoard setzt config-Variablen korrekt")
    
    # ========== fen_to_array() Tests ==========
    
    
    
    def test_fen_to_array_empty(self):
        """Prueft ob fen_to_array mit leerem Board funktioniert."""
        fen = "9/9/9/9/9/9/9/9/9"
        board = fen_to_array(fen)
        
        self.assertEqual(len(board), 9, "Board sollte 9x9 sein")
        for row in board:
            for cell in row:
                self.assertEqual(cell, 0, "Alle Felder sollten 0 sein")
        print("fen_to_array mit leerem Board funktioniert")
    
    
    # ========== countMoves() Tests ==========
    
    def test_count_moves(self):
        """Prueft ob countMoves die Anzahl der Zuege korrekt zaehlt."""
        moves = {
            (4, 4): [(4, 5), (4, 3), (3, 4), (5, 4)],
            (3, 4): [(3, 5), (3, 3)],
            (4, 3): [(5, 3), (4, 2)]
        }
        count = countMoves(moves)
        self.assertEqual(count, 8, "countMoves sollte 8 zurueckgeben")
        print(f"countMoves zaehlt korrekt: {count}")
    
    def test_count_moves_empty(self):
        """Prueft ob countMoves mit leerem Dictionary 0 zurueckgibt."""
        moves = {}
        count = countMoves(moves)
        self.assertEqual(count, 0, "countMoves sollte 0 zurueckgeben")
        print("countMoves mit leerem Dict gibt 0 zurueck")
    
    def test_count_moves_single(self):
        """Prueft ob countMoves mit einem einzigen Zug korrekt zaehlt."""
        moves = {
            (4, 4): [(4, 5)]
        }
        count = countMoves(moves)
        self.assertEqual(count, 1, "countMoves sollte 1 zurueckgeben")
        print("countMoves mit einem Zug zaehlt korrekt")

if __name__ == '__main__':
    unittest.main()