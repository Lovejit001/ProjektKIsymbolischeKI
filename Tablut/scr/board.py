
## die Funktion positions(board, player) erwartet eine 2D Liste "board" und 
## den Spieler (player) dessen möglichen Züge ausgegeben werden soll  

def positions(board, player):
    if player == 'White':
        result = [(3, 0), (2, 0), (1, 0), (4, 1), (4, 2), (4, 3), (5, 0), (6, 0), (7, 0)]
    else:
        result = [(2, 0), (1, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (4, 0), (5, 0), (6, 0), (7, 0)]
    return result