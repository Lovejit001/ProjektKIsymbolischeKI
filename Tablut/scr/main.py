from scr import config
from scr import checkBoard 
from scr import makeMove 
from scr import attack


def main():

    W = config.W
    B = config.B
    K = config.K
    #global W_pieces, B_pieces
    
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
        [0, 0, 0, 0, 0, 0, W, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, B, 0, B, 0, 0, W, 0, 0],
        [0, 0, W, 0, 0, W, 0, 0, 0],
        [0, 0, 0, 0, K, 0, W, 0, 0],
        [0, B, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, W, 0, W, 0, 0, 0],
        [0, B, 0, 0, 0, 0, 0, 0, B],
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

    #debug.print_board(test_noBlack)
    #print_board(test2)
    #print_board(test3)
    #print_board(remis50zug)
    #print_board(remis3Stellung)
    print("Game Starts!")

    #config.onTurn = "White"
    config.onTurn = "Black"
    #result = "Remis"

    #board = test_noBlack
    board = test2
    #board = test3
    #board = remis50zug
    #board = remis3Stellung

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

    print(f"Weiße Figuren auf dem Brett: {config.W_pieces}, Schwarze Figuren auf dem Brett: {config.B_pieces}")

    if config.K_pieces < 1:
        print(f"ERROR! Es ist kein König auf dem Spielfeld vorhanden")
        return

    while checkBoard.checkBoard2(board):
        oldBoard = [row[:] for row in board]
        
        all_moves = makeMove.total_moves(board, config.onTurn)
        board = makeMove.makeMove(board,all_moves)

        print(f"Weiße Figuren auf dem Brett: {config.W_pieces}, Schwarze Figuren auf dem Brett: {config.B_pieces}")
        print(f"Insgesamt Züge: {config.zugCounter}, 50-Züge-Regel: {config.zugRegel}")

        if config.onTurn == "White":
            config.onTurn = "Black"
        else:
            config.onTurn = "White"
        
        if oldBoard == board:
            print(f"ERROR! Es wurde kein Zug getätigt.")
            break
        
        print("Am Zug:" + config.onTurn)

    return
        
if __name__ == "__main__" :
    main()

