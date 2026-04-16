import unittest

from scr.board import positions

## Für die Erstellung der Unit Tests wurde folgendes Link verwendet:
## https://docs.python.org/3/library/unittest.html
## auch wurde als Inspiration das selbst geschriebene Code, aus dem Modul SWTPP verwendet

## Hier werden die Unit Tests für die Funktion positionen() definiert

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