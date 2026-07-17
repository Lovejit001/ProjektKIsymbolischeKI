import unittest

from src.gamelogic.makeMove import updateBoard
from tests.definitions import movingBoard1, movingBoard2, movingBoard3, movingBoard4,B

class TestMakeMoves(unittest.TestCase):
    
    def test_down_move(self):
        expected = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, B, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [B, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0] 
        ]

        move = ((0,0),(7,0))
        updateBoard(movingBoard1,move)

        self.assertEqual(movingBoard1, expected)
        print(f"✓ test_down_move test passed")

    def test_up_move(self):

        expected = [
        [0, 0, 0, B, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0] 
        ]

        move = ((6,3),(0,3))
        updateBoard(movingBoard2,move)

        self.assertEqual(movingBoard2, expected)
        print(f"✓ test_up_move test passed")
    
    def test_right_move(self):

        expected = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, B, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0] 
        ]

        move = ((3,0),(3,4))
        updateBoard(movingBoard3,move)
        
        self.assertEqual(movingBoard3, expected)
        print(f"✓ test_right_move test passed")


    def test_left_move(self):

        expected = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [B, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0] 
    ]   

        move = ((6,3),(6,0))
        updateBoard(movingBoard4,move)
        self.assertEqual(movingBoard4, expected)
        print(f"✓ test_left_move test passed")

        
#MAKE MOVE FUNKTIONIERT NICHT VOR RAND BEWEGUNGEN BESONDERRS DIE RÄNDER WO OUT OF BOUND PASSIERT
#ATTACK MOVE Teste Schreiben 
#Attack move klappt nicht für ränder outofbound passert

 



if __name__ == "__main__":
    unittest.main()