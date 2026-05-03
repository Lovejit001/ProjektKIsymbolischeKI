import unittest

from scr.debug import FenToBoard
from scr.debug import print_board
from scr.makeMove import total_moves
from scr.debug import countMoves
from scr import config 
from tests.definitions import otherBoardFEN1,otherBoardFEN2,otherBoardFEN3,otherBoardFEN4,otherBoardFEN5


class TestStudentsZüge(unittest.TestCase):
    
    def test_totalMoves_byBoard_other_Students(self):

        getBoard1 = FenToBoard(otherBoardFEN1)
        all_Moves1 = total_moves(getBoard1,config.onTurn)
        moves_amount1 = countMoves(all_Moves1)
        self.assertEqual(moves_amount1,16)

        print(f"✓ Same possible moves for board from Student one are found")
    

    def test_second_Studentboard(self):
        
        getBoard2 = FenToBoard(otherBoardFEN2)
        all_Moves2 = total_moves(getBoard2,config.onTurn)
        moves_amount2 = countMoves(all_Moves2)
        self.assertEqual(moves_amount2, 15)
        print(f"✓ Same possible moves for board from Student two are found")
    

    def test_third_Studentboard(self):
        
        getBoard3 = FenToBoard(otherBoardFEN3)
        all_Moves3 = total_moves(getBoard3,config.onTurn)
        moves_amount3 = countMoves(all_Moves3)
        self.assertEqual(moves_amount3, 21)
        print(f"✓ Same possible moves for board from Student four are found")



    def test_fourth_Studentboard(self):
        
        getBoard4 = FenToBoard(otherBoardFEN4)
        all_Moves4 = total_moves(getBoard4,config.onTurn)
        moves_amount4 = countMoves(all_Moves4)
        self.assertEqual(moves_amount4, 30)
        print(f"✓ Same possible Moves are found")

    def test_fifth_Studentboard(self):

        getBoard5 = FenToBoard(otherBoardFEN5)
        all_Moves5 = total_moves(getBoard5,config.onTurn)
        moves_amount5 = countMoves(all_Moves5)
        self.assertEqual(moves_amount5, 32)
        
        print(f"✓ Same possible moves for board from Student five are found")
