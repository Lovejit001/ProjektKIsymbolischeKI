import unittest
import math

from scr import config
from scr import alphaBeta
from scr import makeMove
from tests.definitions import starting_board, alphaBeta_FinalMove

class TestAlphaBeta(unittest.TestCase): 

    def findBestMove1(self):
        
        config.onTurn = 'Black'

        all_possible_moves = makeMove.total_moves(starting_board,config.onTurn)

        alphaBeta.alphaBetaMax(board=starting_board,alpha=(-math.inf),beta=math.inf,depth=10,all_Moves=all_possible_moves,onTurn=config.onTurn,root=True)

        #self.assertEqual(config.bestMove, ((StartRow,StartCol),(GoalRow,GoalCol))) WAS WÄRE BEIM STARTBOARD DER BESTE MOVE ? 

    def findBestMove2(self):
        
        config.onTurn = 'White'

        all_possible_moves = makeMove.total_moves(alphaBeta_FinalMove,config.onTurn)

        alphaBeta.alphaBetaMax(board=alphaBeta_FinalMove,alpha=(-math.inf),beta=math.inf,depth=10,all_Moves=all_possible_moves,onTurn=config.onTurn,root=True)

        excepted = ((4,0),(0,0))
        
        self.assertEqual(config.bestMove, excepted)
        print(f"✓ King reaches Goal Field --> Winner: White")


    def findBestMove3(self):
        
        config.onTurn = 'Black'

        all_possible_moves = makeMove.total_moves(alphaBeta_FinalMove,config.onTurn)

        alphaBeta.alphaBetaMax(board=alphaBeta_FinalMove,alpha=(-math.inf),beta=math.inf,depth=10,all_Moves=all_possible_moves,onTurn=config.onTurn,root=True)

        excepted = ((4,3),(4,1))

        self.assertEqual(config.bestMove,excepted)
        print(f"✓ Black kills King --> Winner: Black")
