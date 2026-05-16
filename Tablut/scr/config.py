B_pieces = 0
W_pieces = 0
K_pieces = 0
zugRegel = 0
zugCounter = 0
eval_counter = 0
boardHash = []
onTurn = "Black"
bestMove: tuple[tuple[int, int], tuple[int, int]] | None = None # Output ((startRow, startCol),(goalRow, goaldCol))

W = 'W'
K = 'K'
B = 'B'

Throne = (4, 4)
surroundingThrone = (4,4), (4,3), (3,4), (4,5), (5,4)
Goal = [(0,0), (0,8), (8,0), (8,8)]
Edge = [
    # Obere Kante (ohne Ecken)
    (0,1), (0,2), (0,3), (0,4), (0,5), (0,6), (0,7),
    # Untere Kante (ohne Ecken)
    (8,1), (8,2), (8,3), (8,4), (8,5), (8,6), (8,7),
    # Linke Kante (ohne Ecken)
    (1,0), (2,0), (3,0), (4,0), (5,0), (6,0), (7,0),
    # Rechte Kante (ohne Ecken)
    (1,8), (2,8), (3,8), (4,8), (5,8), (6,8), (7,8)
]

#HIER VIELLEICHT AUCH EIN VARIABLE CORNER DIE GUCKT OB MAN AN SEITENRAND IST !

def reset_pieces():
    global B_pieces, W_pieces, K_pieces, zugRegel, zugCounter, boardHash, onTurn, bestMove, eval_counter 
    B_pieces = 0
    W_pieces = 0
    K_pieces = 0
    eval_counter = 0
    zugRegel = 0
    zugCounter = 0
    onTurn = "Black"
    bestMove = None

def init_pieces(board):
    global B_pieces, W_pieces, K_pieces
    B_pieces = 0
    W_pieces = 0
    K_pieces = 0
    for i in range(9):
        for j in range(9):
            if board[i][j] == B:
                B_pieces += 1
            elif board[i][j] == K:
                K_pieces += 1
                W_pieces += 1
            elif board[i][j] == W:
                W_pieces += 1