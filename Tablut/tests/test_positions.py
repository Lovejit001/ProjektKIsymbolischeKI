import unittest

from scr.board import get_all_positions
from tests.definitions import White, Black, simple_pawns, white_pawns, black_pawns, simple_board, starting_board
from scr.board import positions

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

## Die Variablen die verwendet werden:
## A - Angreifende
## V - Verteidigende
## K - König
## T - Thron
## KT - König auf dem Thron
## Z - Zielfeld
## Empty - Leeres Feld
## White - Spieler Weiß ist am Zug

Z = 'Z'
Empty = 'Empty'
V = 'V'
A = 'A'
Throne = 'Throne'
White = 'White'
Black = 'Black'

## Wir gehen davon aus das uns von dem Game Server ein BOARD übergeben wird
## also eine 2D Liste mit den entsprechenden Variablen
## Hierbei hat die obere linke Ecke die Koordinaten (0, 0) und die untere rechte Ecke die Korrdinaten (8, 8)



class TestPositions(unittest.TestCase):

    simple_attacker = [
            [Z, Empty, Empty, Empty, Empty, Empty, Empty, Empty, Z],
            [Empty, Empty, Empty, Empty, Empty, Empty, Empty, Empty, Empty],
            [Empty, Empty, Empty, Empty, Empty, Empty, Empty, Empty, Empty],
            [Empty, Empty, Empty, Empty, Empty, Empty, Empty, Empty, Empty],
            [A, Empty, Empty, Empty, Throne, Empty, Empty, Empty, Empty],
            [Empty, Empty, Empty, Empty, Empty, Empty, Empty, Empty, Empty],
            [Empty, Empty, Empty, Empty, Empty, Empty, Empty, Empty, Empty],
            [Empty, Empty, Empty, Empty, Empty, Empty, Empty, Empty, Empty],
            [Z, Empty, Empty, Empty, Empty, Empty, Empty, Empty, Z]
    ]

    simple_defender = [
            [Z, Empty, Empty, Empty, Empty, Empty, Empty, Empty, Z],
            [Empty, Empty, Empty, Empty, Empty, Empty, Empty, Empty, Empty],
            [Empty, Empty, Empty, Empty, Empty, Empty, Empty, Empty, Empty],
            [V, Empty, Empty, Empty, Empty, Empty, Empty, Empty, Empty],
            [Empty, Empty, Empty, Empty, Throne, Empty, Empty, Empty, Empty],
            [Empty, Empty, Empty, Empty, Empty, Empty, Empty, Empty, Empty],
            [Empty, Empty, Empty, Empty, Empty, Empty, Empty, Empty, Empty],
            [Empty, Empty, Empty, Empty, Empty, Empty, Empty, Empty, Empty],
            [Z, Empty, Empty, Empty, Empty, Empty, Empty, Empty, Z]
        ]
    
    def test_simple_attacker(self):
        expected = [(3, 0), (2, 0), (1, 0), (4, 1), (4, 2), (4, 3), (5, 0), (6, 0), (7, 0)]
        self.assertEqual(positions(self.simple_attacker, White), expected)
        print(f"✓ simple_attacker test passed")

    def test_simple_defender(self):
        expected = [(2, 0), (1, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (4, 0), (5, 0), (6, 0), (7, 0)]
        self.assertEqual(positions(self.simple_defender, Black), expected)
        print(f"✓ simple_defender test passed")


if __name__ == '__main__':
    unittest.main()