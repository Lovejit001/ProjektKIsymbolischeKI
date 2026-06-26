import unittest
# Importiere die Funktionen und die config
from src.saveBoardState import undoMove
from src import config

class TestUndoMove(unittest.TestCase):

    def setUp(self):
        # Erstelle ein leeres 9x9 Board für die Tests
        self.board = [[0 for _ in range(9)] for _ in range(9)]

    def test_undo_move_standard_figur(self):
        # --- Arrange ---
        # Figur 'P' bewegt sich von (1,1) nach (1,2)
        # Dabei wurde bei (1,3) eine Figur vom Typ 'B' geschlagen
        figure = 'P'
        bestmove = ((1, 1), (1, 2))
        move_track = [((1, 3), 'B')]
        changed_list = [figure, bestmove, move_track]
        
        # Board vorbereiten: Ziel besetzt, Start leer, Opferfeld leer
        self.board[1][1] = 0
        self.board[1][2] = 'P'
        self.board[1][3] = 0
        
        # --- Act ---
        undoMove(self.board, changed_list)
        
        # --- Assert ---
        self.assertEqual(self.board[1][1], 'P', "Figur sollte zurück auf Start sein")
        self.assertEqual(self.board[1][2], 0, "Ziel sollte wieder leer sein")
        self.assertEqual(self.board[1][3], 'B', "Geschlagene Figur sollte wieder auf dem Board sein")

    def test_undo_move_k_oder_w(self):
        # --- Arrange ---
        # König (K) bewegt sich, dabei wurden mehrere 'B' gekillt
        figure = config.K
        bestmove = ((4, 4), (5, 5))
        # Bei K oder W sind in move_track nur die Koordinaten der gekillten B's
        move_track = [(4, 3), (3, 4)]
        changed_list = [figure, bestmove, move_track]
        
        # Board vorbereiten
        self.board[4][4] = 0
        self.board[5][5] = config.K
        self.board[4][3] = 0
        self.board[3][4] = 0
        
        # --- Act ---
        undoMove(self.board, changed_list)
        
        # --- Assert ---
        self.assertEqual(self.board[4][4], config.K)
        self.assertEqual(self.board[5][5], 0)
        self.assertEqual(self.board[4][3], config.B, "Kill-Position 1 muss B sein")
        self.assertEqual(self.board[3][4], config.B, "Kill-Position 2 muss B sein")

if __name__ == '__main__':
    unittest.main()