import unittest
from scr import makeMove
from scr import config



class TestTotalMoves(unittest.TestCase):  

    def test_total_moves_restrictions(self):
        """Prüft, ob Soldaten Eckfelder und den Thron meiden."""
        # Weißer Soldat (W) auf (0,1) neben Ecke (0,0) und auf (4,3) neben dem Thron (4,4)[cite: 1]
        board = [[0]*9 for _ in range(9)]
        board[0][1] = config.W
        board[4][3] = config.W
        
        moves = makeMove.total_moves(board, "White")
        
        # Eckfeld-Check: Ein Soldat darf die Eckfelder (0,0), (0,8), (8,0), (8,8) nicht betreten[cite: 1]
        self.assertNotIn((0, 0), moves.get((0, 1), []), "Soldat darf kein Eckfeld betreten.")
        # Thron-Check: Normale Figuren dürfen das Feld in der Mitte (den Thron) nicht betreten[cite: 1]
        self.assertNotIn((4, 4), moves.get((4, 3), []), "Soldat darf den Thron nicht betreten.")
        
        print(f"✓ Erster Test bestanden")
    

    def test_total_moves_king_victory(self):
        """Prüft, ob der König legal auf Eckfelder ziehen darf, um zu gewinnen."""
        # König (K) steht auf (0,1) direkt neben einem Sieg-Feld[cite: 1]
        board = [[0]*9 for _ in range(9)]
        board[0][1] = config.K

        moves = makeMove.total_moves(board, "White")

        # Siegbedingung: Die Verteidigung gewinnt durch Setzen des Königs auf ein Eckfeld[cite: 1]
        self.assertIn((0, 0), moves.get((0, 1), []), "König muss auf Eckfelder ziehen dürfen.")
        print(f"✓ Zweiter Test bestanden")

    def test_total_moves_blocked(self):
        """Prüft, ob Figuren korrekt gestoppt werden, wenn der Weg versperrt ist."""
        # Eine Figur darf keine anderen Figuren überspringen[cite: 1]
        # Weißer Soldat auf (4,2) ist durch schwarze Steine (1) eingekesselt
        board = [[0]*9 for _ in range(9)]
        board[4][2] = config.W # Weiß
        board[3][2] = config.B  # Blockiert oben
        board[5][2] = config.B  # Blockiert unten
        board[4][1] = config.B  # Blockiert links
        board[4][3] = config.B  # Blockiert rechts
        
        moves = makeMove.total_moves(board, "White")
        
        # Die Figur muss auf einem freien Feld landen und darf nicht springen[cite: 1]
        self.assertEqual(len(moves.get((4, 2), [])), 0, "Blockierte Figur darf keine Züge haben.")
        print(f"✓ Dritter Test bestanden")

def test_total_moves_jump_throne(self):
    """Prüft, ob der leere Thron gemäß den Regeln übersprungen werden darf."""
    # Regel: Der leere Thron darf übersprungen werden (Beispiel 7)[cite: 1]
    # Weißer Soldat auf (4,2), Weg über den Thron (4,4) nach (4,5)
    board = [[0]*9 for _ in range(9)]
    board[4][2] = config.W
    # Thron (4,4) ist 0 (leer)
    moves = makeMove.total_moves(board, "White")
        
    # Die Figur darf über den leeren Thron hinweg auf ein freies Feld dahinter ziehen[cite: 1]
    self.assertIn((4, 5), moves.get((4, 2), []), "Leerer Thron muss übersprungen werden können.")
    print(f"✓ Vierter Test bestanden")