import unittest

from scr.debug import total_moves, print_dic
from scr.tests.definitions import White, Black, simple_pawns, white_pawns, black_pawns, simple_board, starting_board

## Hier werden die Unit Tests für die Funktion moves() definiert
## Es wird getestet ob die Funktion moves() die richtigen Züge der Figuren zurückgibt

class TestMoves(unittest.TestCase):
    
    def test_simple_pawns_white(self):
        expected = {
            (0, 6): [(0, 7), (0, 5)],
            (1, 6): [(1, 7), (1, 8), (1, 5), (1, 4), (1, 3), (1, 2), (1, 1), (1, 0)],
            (2, 6): [(2, 7), (2, 8), (3, 6), (4, 6), (5, 6), (2, 5), (2, 4), (2, 3)],
            (3, 3): [(2, 3), (1, 3), (0, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 2), (3, 1), (3, 0)],
            (4, 3): [(4, 5), (4, 6), (4, 7), (4, 8), (5, 3), (6, 3), (7, 3), (8, 3), (4, 2), (4, 1), (4, 0)],
            (6, 6): [(5, 6), (4, 6), (3, 6), (6, 7), (6, 8), (7, 6), (8, 6), (6, 5)],
        }
        self.assertEqual(total_moves(simple_pawns, White), expected)
        print(f"✓ simple_pawns_white test passed")
    
    def test_simple_pawns_black(self):
        expected = {
            (0, 2): [(0, 3), (1, 2), (0, 1)],
            (0, 4): [(0, 5), (1, 4), (2, 4), (3, 4), (5, 4), (0, 3)],
            (2, 2): [(1, 2), (2, 3), (2, 4), (2, 5), (3, 2), (4, 2), (5, 2), (2, 1), (2, 0)],
            (6, 2): [(5, 2), (4, 2), (3, 2), (6, 3), (7, 2), (8, 2), (6, 1), (6, 0)],
            (6, 4): [(5, 4), (3, 4), (2, 4), (1, 4), (6, 5), (7, 4), (8, 4), (6, 3)],
            (7, 5): [(6, 5), (5, 5), (4, 5), (3, 5), (2, 5), (1, 5), (0, 5), (7, 6), (7, 7), (7, 8), (8, 5), (7, 4), (7, 3), (7, 2), (7, 1), (7, 0)],
        }
        self.assertEqual(total_moves(simple_pawns, Black), expected)
        print(f"✓ simple_pawns_black test passed")

if __name__ == '__main__':
    unittest.main()