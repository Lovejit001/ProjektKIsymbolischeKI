from src import config
from src import checkBoard 
from src import makeMove 
from src import attack
from src import debug
from src import alphaBetaWithTransposition
from tests import definitions

import math


def main():
    #global W_pieces, B_pieces
    W = config.W
    B = config.B
    K = config.K

    config.onTurn = "Black"

    board = definitions.starting_board

    #Zählt Anzahl aller Figuren jeweils vor Start des Spieles
    config.init_pieces(board)

    print(f"Weiße Figuren auf dem Brett: {config.W_pieces}, Schwarze Figuren auf dem Brett: {config.B_pieces}")


    if config.K_pieces < 1:
        print(f"ERROR! Es ist kein König auf dem Spielfeld vorhanden")
        return
    
    print("Game Starts!")
        
    #WAS MACHT DAS ????
    if config.onTurn == "White":
        config.onTurn = "Black"
    else:
        config.onTurn = "White"

    while checkBoard.checkBoard2(board):
        
        #debug.print_board(board)

        oldBoard = [row[:] for row in board]
        
        #all_moves = makeMove.total_moves(board, config.onTurn) <-- ist in AlphaBeta Func drin
        alphaBetaWithTransposition.getBestMove(board,config.onTurn,depth=5)
        
        print(f"BESTER MOVE: {config.bestMove} Spieler am Zug: {config.onTurn}")

        board = makeMove.updateBoard(board,config.bestMove)
        
        debug.print_board(board)

        #print(f"Weiße Figuren auf dem Brett: {config.W_pieces}, Schwarze Figuren auf dem Brett: {config.B_pieces}")
        #print(f"Insgesamt Züge: {config.zugCounter}, 50-Züge-Regel: {config.zugRegel}")

        if config.onTurn == "White":
            config.onTurn = "Black"
        else:
            config.onTurn = "White"
        
        if oldBoard == board:
            print(f"ERROR! Es wurde kein Zug getätigt.")
            break
        
        
        #print("Am Zug:" + config.onTurn)

    print("Game Over: End Board:")
    print(" ")
    debug.print_board(board)


    return
        
if __name__ == "__main__" :
    main()

