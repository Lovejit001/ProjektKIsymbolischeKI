import unittest
import copy
from src.gamelogic import config
from src.gamelogic import attack
from src.gamelogic.saveBoardState import undoMove
from src.gamelogic import makeMove
from src.gamelogic import debug


class TestUndoMove(unittest.TestCase):

    def setUp(self):
        config.B_pieces = 16
        config.W_pieces = 8
        config.K_pieces = 1
        config.K = 'K'
        config.W = 'W'
        config.B = 'B'

    # ── König zieht und schlägt mehrere schwarze Steine ─────────
    def test_king_move_multiple_captures(self):
        board = [[0]*9 for _ in range(9)]
        board[3][3] = config.K
        board[2][3] = config.B
        board[4][0] = config.B
        board_before = copy.deepcopy(board)

        changed_list = makeMove.updateBoard(board, ((4,0), (4,3)))

        undoMove(board, changed_list)

        self.assertEqual(board, board_before)

    # ── Weiß zieht, kein Kill ────────────────────────────────────
    def test_white_move_no_capture(self):
        board = [[0]*9 for _ in range(9)]
        board[4][4] = config.W          # Weiß auf (4,4)
        board_before = copy.deepcopy(board)

        changed_list = makeMove.updateBoard(board, ((4,4), (4,6)))   # zieht nach (4,6) – kein Schlag
        undoMove(board, changed_list)

        self.assertEqual(board, board_before)

    # ── Weiß zieht und schlägt einen schwarzen Stein ────────────
    def test_white_move_single_capture(self):
        board = [[0]*9 for _ in range(9)]
        board[4][4] = config.W          # Weiß
        board[4][6] = config.B
        board[4][7] = config.W 
        board[2][3] = config.W 
        board[5][6] = config.B
        board[3][8] = config.W 
        board[1][3] = config.W 
        board[1][1] = config.K 
        board_before = copy.deepcopy(board)

        changed_list = makeMove.updateBoard(board, ((4,4), (4,5)))   # Weiß schlägt Schwarz

        undoMove(board, changed_list)
        self.assertEqual(board, board_before)

    # ── Schwarz zieht, kein Kill ────────────────────────────────
    def test_black_move_no_capture(self):
        board = [[0]*9 for _ in range(9)]
        board[4][4] = config.B
        board_before = copy.deepcopy(board)

        changed_list = makeMove.updateBoard(board, ((4,4), (4,6)))   # Schwarz zieht nach (4,6)
        undoMove(board, changed_list)

        self.assertEqual(board, board_before)

    # ── Schwarz zieht und schlägt einen weißen Stein ────────────
    def test_black_move_capture_white(self):
        board = [[0]*9 for _ in range(9)]
        board[5][4] = config.W
        board[6][3] = config.B
        board[6][5] = config.B
        board[6][2] = config.W
        board[6][6] = config.W   
      
        board_before = copy.deepcopy(board)

        changed_list = makeMove.updateBoard(board, ((5,4), (6,4)))   # Schwarz schlägt Weiß
    
        undoMove(board, changed_list)

        self.assertEqual(board, board_before)

   

    # ── Schwarz schlägt mehrere Figuren gleichzeitig ──────────
    def test_black_move_multiple_captures_mixed(self):
        board = [[0]*9 for _ in range(9)]
        board[4][4] = config.B          # Schwarz
        board[4][3] = config.W          # Weiß auf dem Weg
        board[4][2] = config.K          # König auf dem Ziel
        board_before = copy.deepcopy(board)
        

        changed_list = makeMove.updateBoard(board, ((5,4), (6,4)))   # Schwarz schlägt Weiß

        undoMove(board, changed_list)

        self.assertEqual(board, board_before)

if __name__ == "__main__":
    unittest.main()