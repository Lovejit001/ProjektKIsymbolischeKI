import unittest

from scr.board import get_all_positions
from tests.definitions import White, Black, simple_pawns, white_pawns, black_pawns, simple_board, starting_board

## Für die Erstellung der Unit Tests wurde folgendes Link verwendet:
## https://docs.python.org/3/library/unittest.html
## auch wurde als Inspiration das selbst geschriebene Code, aus dem Modul SWTPP verwendet

## Hier werden die Unit Tests für die Funktion positionen() definiert
## Es wird getestet ob die Funktion positionen() die richtigen Positionen der Figuren zurückgibt


class TestPositions(unittest.TestCase):
    
    def test_simple_pawns_white(self):
        expected = [(0, 6), (1, 6), (2, 6), (3, 3), (4, 3), (6, 6)]
        self.assertEqual(get_all_positions(simple_pawns, White), expected)
        print(f"✓ simple_pawns_white test passed")

    def test_simple_pawns_black(self):
        expected = [(0, 2), (0, 4), (2, 2), (6, 2), (6, 4), (7, 5)]
        self.assertEqual(get_all_positions(simple_pawns, Black), expected)
        print(f"✓ simple_pawns_black test passed")

    def test_white_pawns(self):
        expected = [(i, j) for i in range(9) for j in range(9)]
        self.assertEqual(get_all_positions(white_pawns, White), expected)
        print(f"✓ white_pawns test passed")
    
    def test_black_pawns(self):
        expected = [(i, j) for i in range(9) for j in range(9)]
        self.assertEqual(get_all_positions(black_pawns, Black), expected)
        print(f"✓ black_pawns test passed")
    
    def test_simple_board_white(self):
        expected = [(0, 6), (1, 6), (2, 6), (3, 3), (4, 3), (4, 4), (6, 6), (7, 6), (7, 7), (7, 8)]
        self.assertEqual(get_all_positions(simple_board, White), expected)
        print(f"✓ simple_board_white test passed")

    def test_simple_board_black(self):
        expected = [(0, 2), (0, 4), (2, 2), (5, 5), (5, 6), (5, 7), (5, 8), (6, 2), (6, 4), (7, 3), (7, 4), (7, 5), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (8, 8)]
        self.assertEqual(get_all_positions(simple_board, Black), expected)
        print(f"✓ simple_board_black test passed")

    def test_starting_board_white(self):
        expected = [(2, 4), (3, 4), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (5, 4), (6, 4)]
        self.assertEqual(get_all_positions(starting_board, White), expected)
        print(f"✓ starting_board_white test passed")
    
    def test_starting_board_black(self):
        expected = [(0, 3), (0, 4), (0, 5), (1, 4), (3, 0), (3, 8), (4, 0), (4, 1), (4, 7), (4, 8), (5, 0), (5, 8), (7, 4), (8, 3), (8, 4), (8, 5)]
        self.assertEqual(get_all_positions(starting_board, Black), expected)
        print(f"✓ starting_board_black test passed")


if __name__ == '__main__':
    unittest.main()