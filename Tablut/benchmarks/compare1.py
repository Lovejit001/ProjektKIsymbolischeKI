"""
Hier wird KI gegen KI Spielen.
KI Nr.1 hat die AlphaBeta pruning und KI 2 dasselbe mit dem Feature von Transposition Table (ermöglicht eine tiefere Suche durchzuführen)
"""
from src import config
from src import checkBoard 
from src import makeMove 
from src import attack
from src import debug
from src import alphaBetaWithTransposition
from src import alphaBeta
from benchmarks import testboards

def game1(board):
    """
    In diesem Fall hat Spieler Schwarz das Feature von Transpostiontable
    """
    W = config.W
    B = config.B
    K = config.K

    config.onTurn = "Black"

    #Zählt Anzahl aller Figuren jeweils vor Start des Spieles
    config.init_pieces(board)
    
    config.onTurn ='Black'

    #print(board)
    #print(type(board))
    #debug.print_board(board)
    #print(board[0][0])
    #print(board[0][8])
    #print(board[8][0])
    #print(board[8][8])
    
    while checkBoard.checkBoard2(board) == -2:
        #print("HELLLLLLOOOOOO$$$$$$$$$$$$$$$$$$$$$$$$$$$")

        oldBoard = [row[:] for row in board]

        if config.onTurn == 'Black':
            alphaBetaWithTransposition.getBestMove(board,config.onTurn,depth=3)
        else:
            alphaBeta.getBestMove(board,config.onTurn,depth=3)

        #print("BEST MOVE")
        #print(config.bestMove)


        makeMove.updateBoard(board,config.bestMove)
        #debug.print_board(board)


        if config.onTurn == "White":
            config.onTurn = "Black"
        else:
            config.onTurn = "White"    


        if oldBoard == board:
            print(f"ERROR! Es wurde kein Zug getätigt.")
            break
    


    print("Game Over: End Board:")
    print(" ")
    debug.print_board(board)

    res = checkBoard.checkBoard2(board)
    if res == 0 :
        print("DRAW")
    elif res == -1:
        print("WINNER BLACK")
    elif res == 1:
        print("WINNER WHITE")

    return res


def main():
    
    boards = testboards.generated_boards

    counter_black = 0 
    counter_white = 0 
    counter_draw = 0

    for board in boards:
        result = game1(board)
        print(result)
        if result == -1 : 
            counter_black += 1
        elif result == 1:
            counter_white += 1
        elif result == 0:
            counter_draw += 1
        
            
    print(f"Anzahl gewonnener Spiele für Black: {counter_black} ")
    print(f"Anzahl gewonnener Spiele für White: {counter_white} ")

if __name__ == "__main__":
    main()