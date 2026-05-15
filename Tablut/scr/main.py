from scr import config
from scr import checkBoard 
from scr import makeMove 
from scr import attack
from scr import debug
from scr import alphaBeta

import math, copy


def main():

    W = config.W
    B = config.B
    K = config.K
    #global W_pieces, B_pieces
    
    starting_board = [
    [0, 0, 0, B, B, B, 0, 0, 0],
    [0, 0, 0, 0, B, 0, 0, 0, 0],
    [0, 0, 0, 0, W, 0, 0, 0, 0],
    [B, 0, 0, 0, W, 0, 0, 0, B],
    [B, B, W, W, K, W, W, B, B],
    [B, 0, 0, 0, W, 0, 0, 0, B],
    [0, 0, 0, 0, W, 0, 0, 0, 0],
    [0, 0, 0, 0, B, 0, 0, 0, 0],
    [0, 0, 0, B, B, B, 0, 0, 0]
    ]
    
    test_noBlack = [
        [0, 0, 0, 0, 0, 0, W, 0, 0],
        [0, 0, 0, 0, 0, 0, W, 0, 0],
        [0, 0, 0, 0, 0, 0, W, 0, 0],
        [0, 0, 0, W, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, W, 0, 0, W, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    test2 = [
        [0, 0, 0, 0, 0, B, W, 0, 0],
        [0, 0, 0, 0, B, 0, 0, 0, 0],
        [0, B, B, B, B, 0, W, 0, 0],
        [0, 0, W, 0, 0, B, 0, 0, 0],
        [0, 0, B, 0, K, 0, W, 0, 0],
        [0, B, B, 0, B, B, 0, 0, 0],
        [0, 0, B, W, B, B, 0, 0, 0],
        [0, B, 0, B, 0, B, 0, 0, B],
        [0, 0, 0, 0, B, 0, 0, 0, 0]
    ]
    test3 = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, B, 0, 0, 0, 0],
        [0, 0, 0, B, 0, B, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, B, 0],
        [0, 0, B, 0, B, 0, 0, B, 0],
        [K, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    remis50zug = [
        [0, B, B, B, B, B, B, B, 0],
        [B, B, B, B, B, B, B, B, B],
        [B, B, B, B, B, B, B, B, B],
        [B, B, B, B, B, B, B, B, B],
        [B, B, B, B, 0, B, B, 0, B],
        [W, W, W, W, W, W, 0,  K, W],
        [W, W, W, W, W, W, W, W, W],
        [W, W, W, W, W, W, W, W, W],
        [0, W, W, W, W, W, W, W, 0]
    ]
    remis3Stellung = [
        [0, W, W, W, W, W, W, W, 0],
        [W, B, 0, W, W, W, W, W, W],
        [W, W, W, W, W, W, W, W, W],
        [W, W, W, W, W, W, W, W, W],
        [W, W, W, W, 0, W, W, W, W],
        [W, W, W, W, W, W, W, K, W],
        [W, W, W, W, W, W, W, W, W],
        [W, W, W, W, W, W, W, W, W],
        [0, W, W, W, W, W, W, W, 0]
    ]

    alphaBetaBoard= [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [K, 0, 0, B, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0] 
    ]

    #debug.print_board(test_noBlack)
    #print_board(test2)
    #print_board(test3)
    #print_board(remis50zug)
    #print_board(remis3Stellung)
    print("Game Starts!")

    config.onTurn = "White"
    #config.onTurn = "Black"
    #result = "Remis"

    #board = test_noBlack
    board = alphaBetaBoard
    #board = test2
    #board = remis50zug
    #board = remis3Stellung

    depth = 5

    # kann weg wenn in config das Startboard Anzahl angegeben wird
    for i in range(9):
        for j in range(9):
            if board[i][j] == 'W':
                config.W_pieces += 1
            elif board[i][j] == 'K':
                config.K_pieces += 1
                config.W_pieces += 1
            elif board[i][j] == 'B':
                config.B_pieces += 1

    #print(f"Weiße Figuren auf dem Brett: {config.W_pieces}, Schwarze Figuren auf dem Brett: {config.B_pieces}")

    if config.K_pieces < 1:
        print(f"ERROR! Es ist kein König auf dem Spielfeld vorhanden")
        return

    #while checkBoard.checkBoard2(board):
    i = 0
    while i < 1:
        print(f"Der Beste Zug: {config.bestMove}. (Sollte None zum Anfang)")
        
        debug.print_board(board)

        oldBoard = copy.deepcopy(board)
        
        print("ALPHA BETA BEGINNT")

        if config.onTurn == "White":
            alphaBeta.alphaBetaMax(board=board,alpha=-math.inf,beta=math.inf,depth=depth,all_Moves=makeMove.total_moves(board,config.onTurn),onTurn=config.onTurn,root=True)
        else:
            alphaBeta.alphaBetaMin(board=board,alpha=-math.inf,beta=math.inf,depth=depth,all_Moves=makeMove.total_moves(board,config.onTurn),onTurn=config.onTurn,root=True)
        
        print("ALPHA BETA ZUENDE")
        board = makeMove.updateBoard(board, config.bestMove)
        print(f"Der beste Move welches nun durchgeführt wird: {config.bestMove}")
        
        debug.print_board(board)

        print(f"Weiße Figuren auf dem Brett: {config.W_pieces}, Schwarze Figuren auf dem Brett: {config.B_pieces}")
        print(f"Insgesamt Züge: {config.zugCounter}, 50-Züge-Regel: {config.zugRegel}")

        if config.onTurn == "White":
            config.onTurn = "Black"
        else:
            config.onTurn = "White"
        
        if oldBoard == board:
            print(f"ERROR! Es wurde kein Zug getätigt.")
            break

        i += 1

    return
        
if __name__ == "__main__" :
    main()

