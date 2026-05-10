from scr import config

def eval(board):

    score = 0
    if config.onTurn == "White":
        pos = findKing(board)

        score += pts_eval(pos)

    return score


    

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

def pts_eval(KingPostion):
    if KingPostion in config.Throne:
        return 2
    elif KingPostion in config.surroundingThrone:
        return 1
    elif KingPostion in config.Goal:
        return 99
    elif KingPostion in config.Edge:
        return 3
    else:
        return -1

def findKing(board):

    for i in range(9):
        for j in range(9):
            if board[i][j] == config.K:
                return (i,j)

