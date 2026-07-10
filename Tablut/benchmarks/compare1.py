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
from benchmarks import testboards5
import time
import math
import copy


#Problem liegt bei REMIS
#Problem liegt bei REMIS
#Problem liegt bei REMIS
#Problem liegt bei REMIS
#Problem liegt bei REMIS
#Problem liegt bei REMIS
#Problem liegt bei REMIS
#Problem liegt bei REMIS


def game(board):
    """
    In diesem Fall hat Spieler Schwarz das Feature von Transpostiontable
    """
    W = config.W
    B = config.B
    K = config.K

    #Zählt Anzahl aller Figuren jeweils vor Start des Spieles
    config.init_pieces(board)
    
    timeclock_White = 60
    timeclock_Black = 60
    config.onTurn ='Black'
    res = -math.inf
    board = copy.deepcopy(board)  # <-- DAS HAT GEFEHLT!

    
    while checkBoard.checkBoard2(board) == -2:
        #print("HELLLLLLOOOOOO$$$$$$$$$$$$$$$$$$$$$$$$$$$")

        oldBoard = [row[:] for row in board]

        if config.onTurn == 'Black':
            
            #alphaBetaWithTransposition.getBestMove(board,config.onTurn,depth=3)

            print(f"MY {config.onTurn} Remaining Time: {timeclock_Black}")
            bestMove, _, usedTime = alphaBetaWithTransposition.iterative_deepening(board, config.onTurn,timeclock_Black)
            timeclock_Black = timeclock_Black - usedTime
            print(f"{config.onTurn}  USED TIME {usedTime}")
            print(f"AFTER : MY {config.onTurn} Remaining Time: {timeclock_Black}")
            if timeclock_Black <= 0 :
                #Spieler hat keine Zeit mehr SChwarz verliert:
                print("Spieler Black hat keine Zeit mehr ")
                res = 1
                break
                

        else:
            #alphaBeta.getBestMove(board,config.onTurn,depth=3)
            print(f"MY {config.onTurn} Remaining Time: {timeclock_White}")
            bestMove, _, usedTime = alphaBeta.iterative_deepening(board, config.onTurn,timeclock_White)
            timeclock_White = timeclock_White - usedTime
            print(f"{config.onTurn}  USED TIME {usedTime}")
            print(f"AFTER : MY {config.onTurn} Remaining Time: {timeclock_White}")
            if timeclock_White <= 0 :
                #Spieler hat keine Zeit mehr Weiß verliert:
                print("Spieler Black hat keine Zeit mehr ")
                res = -1
                break
        
        makeMove.updateBoard(board,bestMove)
        

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
    
    #Falls das Spiel abgebrochen wurde weil ein Spieler keine Zeit mehr hat wird, direkt Gewinner ausgegben
    if res == -math.inf:
       
        res = checkBoard.checkBoard2(board)
        if res == 0 :
            print("DRAW")
        elif res == -1:
            print("WINNER BLACK")
        elif res == 1:
            print("WINNER WHITE")

    return res


def main():
    
    boards = testboards5.all_boards

    counter_black = 0 
    counter_white = 0 
    counter_draw = 0
    i = 0
    for board in boards:
        i+= 1
        if i < 50: 
            continue

        result = game(board)
        print(result)
        if result == -1 : 
            counter_black += 1
        elif result == 1:
            counter_white += 1
        elif result == 0:
            counter_draw += 1
        
            
    print(f"Anzahl gewonnener Spiele für Black: {counter_black} ")
    print(f"Anzahl gewonnener Spiele für White: {counter_white} ")
    print(f"Anzahl Unentschieden:               {counter_draw} ")

if __name__ == "__main__":
    main()