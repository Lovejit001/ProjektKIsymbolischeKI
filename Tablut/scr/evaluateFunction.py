from scr import config
from scr import positions

# Die Bewertungsfunktion soll die Bewertung des Boards angeben,
# dabei hat die Weiße Figur den Wert 1, die Schwarze Figur den Wert 2 und der König den Wert 100

def eval_func(board, onTurn):
    
    white_score = 0
    black_score = 0

    for i in range(9):
        for j in range(9):
            piece = board[i][j]
            if piece == config.W:
                white_score += 1
            elif piece == config.K:
                white_score += 4
            elif piece == config.B:
                black_score += 1.5
    
    king_pos = findKing(board)
    
    if king_pos:
        white_score += pts_eval(king_pos)
    else:
        white_score = -1000 # wenn kein König auf dem Feld vorhanden ist dann hat Schwarz gewonnen
    
    total_score = white_score - black_score

    if onTurn == "White":
        return total_score
    else:
        return -total_score

    
def pts_eval(KingPostion):   ## warum überall KingPosition == config.Throne??? warum nicht prüfen ob es IN einer vorhanden ist
    if KingPostion == config.Throne:  ## == kann man so lassen, weil es nur einen Throne gibt
        return 2
    elif KingPostion in config.surroundingThrone:
        return 1
    elif KingPostion in config.Goal:
        return 99
    elif KingPostion in config.Edge:
        return 3
    else:
        return 0

def findKing(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == config.K:
                return (i,j)
    return None



#
#pst = [
#    [99,  3,  3,  3,  3,  3,  3,  3, 99],
#    [ 3, -1, -1, -1, -1, -1, -1, -1,  3],
#    [ 3, -1, -1, -1, -1, -1, -1, -1,  3],
#    [ 3, -1, -1, -1,  1, -1, -1, -1,  3],
#    [ 3, -1, -1,  1,  2,  1, -1, -1,  3],
#    [ 3, -1, -1, -1,  1, -1, -1, -1,  3],
#    [ 3, -1, -1, -1, -1, -1, -1, -1,  3],
#    [ 3, -1, -1, -1, -1, -1, -1, -1,  3],
#    [99,  3,  3,  3,  3,  3,  3,  3, 99]
#]