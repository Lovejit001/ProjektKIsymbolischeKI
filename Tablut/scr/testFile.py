#Diese Funktion führt die Schritt aus und aktualisiert Board
import random
import alphaBeta
import math

from scr.attack import *
from scr.positions import get_all_pos
from scr.checkBoard import getHash
from scr.debug import print_board
from scr import config




def makeMove(board,all_possible_moves):
    """
    Wählt zufällig einen zulässigen Zug aus und führt ihn auf dem Board aus.
    Danach wird geprüft, ob durch den Zug Gegnerfiguren geschlagen werden.

    Args:
        board: 2D‑Liste (9x9) mit Figuren‑IDs (z.B. B = Schwarz, W, K = Weiß).
        all_possible_moves: dict {start_pos: [list of goal_pos]} mit allen möglichen Zügen.

    Returns:
        Aktualisiertes Board nach dem Zug und allen Angriffen.
    """
    
    # Wenn keine Züge gemacht werden können
    if all_possible_moves == {}:
        return board

    alphaBeta.alphBetaMax(board=board,alpha=(-math.inf),beta=math.inf,depth=5,allMoves=all_possible_moves,root=True)
    

    
    board = updateBoard(board)
    # Prüfen, ob nach dem Zug Figuren geschlagen werden
    board = attack(board,GoalPos)

    return board

def updateBoard(board):     

    startPos, goalPos = config.bestMove

    start_row, start_col = startPos
    
    goal_row, goal_col = goalPos

    #print(f"StartPos: {random_StartPos} Zufälliger Zug: {random_GoalPos}")

    # Figur auf der Startposition merken
    figure = board[start_row][start_col]

    # Startposition leeren
    board[start_row][start_col] = 0
    
    # Zielposition mit der Figur belegen
    board[goal_row][goal_col] = figure

    config.zugCounter += 1
    config.zugRegel += 1

    #print("Neuer Board nach dem Zug:")
    #print_board(board)

    # vor oder nach dem Angriff? Das muss geklärt werden.
    newBoardHash = getHash(board)
    config.boardHash.append(newBoardHash)

    if len(config.boardHash) > 20:
        config.boardHash.pop(0)

    return board