import unittest

from scr.board import print_board
from scr.makeMove import makeMove
from tests.definitions import movingBoard1,movingBoard2,movingBoard3, movingBoard4

class TestMakeMoves(unittest.TestCase):
    
    def test_down_move(self):
        expected = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0] 
        ]

        possible_moves = {(0,0):[(7,0)]}

        self.assertEqual(makeMove(movingBoard1,possible_moves), expected)
        print(f"✓ test_down_move test passed")

    def test_up_move(self):

        expected = [
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0] 
        ]

        possible_moves = {(6,3):[(0,3)]}

        self.assertEqual(makeMove(movingBoard2,possible_moves), expected)
        print(f"✓ test_up_move test passed")
    
    def test_right_move(self):

        expected = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0] 
        ]

        possible_moves = {(3,0):[(3,4)]}

        self.assertEqual(makeMove(movingBoard3,possible_moves), expected)
        print(f"✓ test_right_move test passed")


    def test_left_move(self):

        expected = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0] 
    ]   

        possible_moves = {(6,3):[(6,0)]}

        self.assertEqual(makeMove(movingBoard4,possible_moves), expected)
        print(f"✓ test_left_move test passed")

        
#MAKE MOVE FUNKTIONIERT NICHT VOR RAND BEWEGUNGEN BESONDERRS DIE RÄNDER WO OUT OF BOUND PASSIERT
#ATTACK MOVE Teste Schreiben 
#Attack move klappt nicht für ränder outofbound passert

 



if __name__ == "__main__":
    unittest.main()