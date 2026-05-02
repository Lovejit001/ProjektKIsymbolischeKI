#Diese Funktion führt die Schritt aus und aktualisiert Board
import random

from scr.attack import *
from scr.positions import get_all_pos
from scr.checkBoard import getHash
from scr.debug import print_board
from scr import config


def total_moves(board,onTurn):
    """
    Bestimmt alle möglichen Züge für den aktuellen Spieler.

    Die Funktion sammelt zuerst alle Positionen der Figuren des Spielers
    und berechnet dann für jede Figur alle legalen Zielpositionen.
    Am Ende werden alle Züge in einem Dictionary zusammengeführt.

    Args:
        Board: 2D-Liste des aktuellen Spielfelds.
        White: Spielerkennung, z.B. "White" oder "Black".

    Returns:
        Ein Dictionary der Form:
        {(start_row, start_col): [(ziel1_row, ziel1_col), ...]}
    """

    all_positions = get_all_pos(board,onTurn)
    
    if not all_positions: 
        return board
    
    all_moves = {}
    
    for  position in all_positions:
        all_moves = merge_moves(all_moves,(get_figures_Moves(board,position)))

    print(f"Alle mögliche Züge: {all_moves}")    
    
    return all_moves

    #return makeMove(board,all_moves)    

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

    # Zufälligen Startpunkt auswählen
    random_StartPos = random.choice(list(all_possible_moves.keys()))
    # Zufälligen Zielpunkt aus allen Zielen vom Startpunkt wählen
    random_GoalPos = random.choice(list(all_possible_moves[random_StartPos])) 
    
    start_row, start_col = random_StartPos
    
    goal_row, goal_col = random_GoalPos

    print(f"Zufälliger Zug: {random_GoalPos}")

    # Figur auf der Startposition merken
    figure = board[start_row][start_col]

    # Startposition leeren
    board[start_row][start_col] = 0
    
    # Zielposition mit der Figur belegen
    board[goal_row][goal_col] = figure

    config.zugCounter += 1
    config.zugRegel += 1

    print("Neuer Board nach dem Zug:")
    print_board(board)

    # vor oder nach dem Angriff? Das muss geklärt werden.
    newBoardHash = getHash(board)
    config.boardHash.append(newBoardHash)

    if len(config.boardHash) > 20:
        config.boardHash.pop(0)
    
    # Prüfen, ob nach dem Zug Figuren geschlagen werden
    board = attack(board,random_GoalPos)

    return board

def get_figures_Moves(board,pos): 

    """
    Berechnet alle möglichen Züge einer einzelnen Figur.

    Für die gegebene Startposition werden alle legalen Züge
    in vier Richtungen geprüft: oben, rechts, unten und links.

    Args:
        Board: 2D-Liste des Spielfelds.
        White: Spielerkennung, wird aktuell nicht direkt verwendet.
        Pos: Startposition der Figur als Tupel (row, col).

    Returns:
        Ein Dictionary mit genau einem Startfeld als Schlüssel und
        einer Liste aller möglichen Zielpositionen als Wert.
    """

    moves = {}
    
    #Berechnet alle möglichen Züge einer Figur nach oben        
    moves = merge_moves(moves,(all_moves_up_to_Figure(board,pos)))
    
    #Berechnet alle möglichen Züge einer Figur nach unten        
    moves= merge_moves(moves,(all_moves_right_to_Figure(board,pos)))
    
    #Berechnet alle möglichen Züge einer Figur nach rechts        
    moves= merge_moves(moves,(all_moves_down_to_Figure(board,pos)))

    #Berechnet alle möglichen Züge einer Figur nach links        
    moves= merge_moves(moves,(all_moves_left_to_Figure(board,pos)))
    
    return moves

def merge_moves(oldMoves :dict ,newMoves: dict):
    """
    Führt zwei Zug-Dictionaries zusammen.

    Falls ein Startfeld bereits im alten Dictionary existiert,
    werden die neuen Zielpositionen an die bestehende Liste angehängt.
    Andernfalls wird der Eintrag neu angelegt.

    Args:
        oldMoves: Bereits bekannte Züge.
        newMoves: Neu berechnete Züge.

    Returns:
        Das zusammengeführte Dictionary aller Züge.
    """
    
    for key, values in newMoves.items():
        if key in oldMoves:
            oldMoves[key].extend(values)
        else:
            oldMoves[key] = values
    
    return oldMoves



def all_moves_up_to_Figure(board, StartPos):
    moves = {}
    (start_row,start_col) = StartPos

    row, col = StartPos
    row -= 1

    while row >= 0:
            
        if isEmptyField(board,(row,col)):
            if validMove(board,(row,col),StartPos):
                moves = merge_moves(moves,{(start_row,start_col):[(row, col)]})
            row -=1
        else: 
            break
            
    return moves

def all_moves_down_to_Figure(board, StartPos):
    moves = {}
    (start_row,start_col) = StartPos
    
    row, col = StartPos
    row += 1

    while row <= (len(board)-1):

        if isEmptyField(board,(row,col)):
            if validMove(board,(row,col),StartPos):
                moves = merge_moves(moves,{(start_row,start_col):[(row, col)]})
            row += 1
        else: 
            break

    return moves
    

def all_moves_left_to_Figure(board, StartPos):
    moves = {}
    (start_row,start_col) = StartPos
    
    row, col = StartPos
    col -= 1
    while col >= 0:
        
        if isEmptyField(board,(row,col)):
            if validMove(board,(row,col),StartPos):
                moves = merge_moves(moves,{(start_row,start_col):[(row, col)]})
            col -= 1                
        else: 
            break
    
    return moves

def all_moves_right_to_Figure(board, StartPos):
    
    moves = {}
    (start_row,start_col) = StartPos
    
    row, col = StartPos
    col += 1

    while col <= (len(board[0])-1):
        if isEmptyField(board,(row,col)):
            if validMove(board,(row,col),StartPos):
                moves = merge_moves(moves,{(start_row,start_col):[(row, col)]})
            col += 1
        else: 
            break
    
    
    return moves
    
#Prüft ob die jeweilige Position auf dem Feld leer ist
def isEmptyField(Board,Pos): 
    row, col = Pos
    return Board[row][col] == 0

def validMove(board,Pos,StartPos):
    """
    Prüft, ob eine Zielposition ein legaler Zug ist.

    Ein Zug ist ungültig, wenn:
    - die Figur auf das Thronfeld (4,4) ziehen möchte
    - eine normale Figur eines der Eckfelder betreten möchte

    Nur der König darf auf ein Eckfeld ziehen.

    Args:
        board: 2D-Liste des Spielfelds.
        Pos: Zielposition als Tupel (row, col).
        StartPos: Startposition der ziehenden Figur.

    Returns:
        True, wenn der Zug erlaubt ist, sonst False.
    """
    
    start_row, start_col = StartPos
    row,col = Pos
    
    #Thronfeld wird versucht zu betreten, illegaler Move
    if (row,col) == config.Throne:
        return False
        
    # Nur der König darf Eckfelder/Zielfelder betreten
    if ((row,col) in config.Goal):
        return board[start_row][start_col] == config.K
    
    return True



Start = [
    
    ["E","E","E","B","B","B","E","E","E"],
    ["E","E","E","E","B","E","E","E","E"],
    ["E","E","E","E","W","E","E","E","E"],
    ["B","E","E","E","W","E","E","E","B"],
    ["B","B","W","W","K","W","W","B","B"],
    ["B","E","E","E","W","E","E","E","B"],
    ["E","E","E","E","W","E","E","E","E"],
    ["E","E","E","E","B","E","E","E","E"],
    ["E","E","E","B","B","B","E","E","E"],

]




