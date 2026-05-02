B_pieces = 0
W_pieces = 0
K_pieces = 0
zugRegel = 0
zugCounter = 0
boardHash = []
onTurn = "Black"

W = 'W'
K = 'K'
B = 'B'

Throne = (4, 4)
surroundingThrone = (4,4), (4,3), (3,4), (4,5), (5,4)
Goal = [(0,0), (0,8), (8,0), (8,8)]

def reset_pieces():
    global B_pieces, W_pieces, K_pieces, zugRegel, zugCounter, boardHash, onTurn
    B_pieces = 0
    W_pieces = 0
    K_pieces = 0
    zugRegel = 0
    zugCounter = 0
    onTurn = "Black"