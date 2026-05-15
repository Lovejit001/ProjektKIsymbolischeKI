import time

B_pieces = 0
W_pieces = 0
K_pieces = 0
zugRegel = 0
zugCounter = 0
boardHash = []
onTurn = "Black"
bestMove = None # Output ((startRow, startCol),(goalRow, goaldCol))

start_time = 0
end_time = 1

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
    global B_pieces, W_pieces, K_pieces, zugRegel, zugCounter, boardHash, onTurn, bestMove, start_time, end_time
    B_pieces = 0
    W_pieces = 0
    K_pieces = 0
    zugRegel = 0
    zugCounter = 0
    onTurn = "Black"
    bestMove = None