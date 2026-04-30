import config
from positions import *
from attack import *
from debug import *
from checkBoard import getHash
import random

## makeMove output:  [[(0, 1), […,(0,2),…]]] => [[startpos, [möglichen züge]],...]

def makeMove(board, onTurn):
    moves = []
    all_positions = get_all_pos(board, onTurn)

    print(f"Alle Positionen: {all_positions}")

    if not all_positions:
        return board

    for position in all_positions:
        possible_moves = get_figures_Moves(board, position)
        if possible_moves:
            moves.append([position, possible_moves])
    
    print(f"Alle möglichen Züge: {moves}")

    return doMove(board, moves)


def doMove(board, moves):
    #global B_pieces, W_pieces

    valid_moves = [move for move in moves if move[1]]

    if not valid_moves:   ## wenn keine Züge gemacht werden können, weil es keine Züge gibt
        return board
    
    random_select = random.choice(valid_moves)  ##später wird es mit einer logik ersetzt

    print(f"Zufällige Figur für den Zug: {random_select}")

    random_StartPos = random_select[0]
    random_GoalPos = random.choice(random_select[1])

    print(f"Zufälliger Zug: {random_GoalPos}")
    
    start_row, start_col = random_StartPos
    goal_row, goal_col = random_GoalPos
    
    #Figuer merken die auf der Startposition ist: 
    figure = board[start_row][start_col]

    #Board an der Startposition, leeren:
    board[start_row][start_col] = 0
    
    #Board an der Startposition, aktualisieren:
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


    board = attack(board, random_GoalPos)

    return board

# Gibt alle möglichen Zug der jeweiligen Figur (position) an    
def get_figures_Moves(board, pos): 
    moves_dict = {}
    
    start_line, start_row = pos 
     
    moves_dict = merge_moves(moves_dict, (all_moves_up_to_Figure(board, pos)))
    
    moves_dict= merge_moves(moves_dict, (all_moves_right_to_Figure(board, pos)))
    
    moves_dict= merge_moves(moves_dict, (all_moves_down_to_Figure(board, pos)))

    moves_dict= merge_moves(moves_dict, (all_moves_left_to_Figure(board, pos)))

    moves_list = []
    for start, goals in moves_dict.items():
        for goal in goals:
            moves_list.append(goal)

    return moves_list

def merge_moves(oldMoves :dict ,newMoves: dict):
    
    for key, values in newMoves.items():
        if key in oldMoves:
            oldMoves[key].extend(values)
        else:
            oldMoves[key] = values
    
    return oldMoves
    

def all_moves_up_to_Figure(board, Startpos):
    moves = {}
    (start_row,start_col) = Startpos

    row, col = Startpos
    row -= 1

    while row >= 0:
            
        if isEmptyField(board,(row,col)):
            if validMove(board,(row,col),Startpos):
                moves = merge_moves(moves,{(start_row,start_col):[(row, col)]})
                #moves.append(((start_row,start_col),(row, col)))
            row -=1
        else: 
            break
            
    return moves

def all_moves_down_to_Figure(board, Startpos):
    moves = {}
    (start_row,start_col) = Startpos
    
    row, col = Startpos
    row += 1

    while row <= (len(board)-1):

        if isEmptyField(board,(row,col)):
            if validMove(board,(row,col),Startpos):
                moves = merge_moves(moves,{(start_row,start_col):[(row, col)]})
                #moves.append(((start_line,start_row),(row, col)))
            row += 1
        else: 

            break
    
    return moves
    

def all_moves_left_to_Figure(board, Startpos):
    moves = {}
    (start_row,start_col) = Startpos
    
    row, col = Startpos
    col -= 1
    while col >= 0:
        
        if isEmptyField(board,(row,col)):
            if validMove(board,(row,col),Startpos):
                moves = merge_moves(moves,{(start_row,start_col):[(row, col)]})
                #moves.append(((start_row,start_col),(row, col)))
            col -= 1                
        else: 
            break
    
    return moves

def all_moves_right_to_Figure(board, Startpos):
    
    moves = {}
    (start_row,start_col) = Startpos
    
    row, col = Startpos
    col += 1

    while col <= (len(board[0])-1):
        if isEmptyField(board,(row,col)):
            if validMove(board,(row,col),Startpos):
                moves = merge_moves(moves,{(start_row,start_col):[(row, col)]})
            col += 1
        else: 
            break
    
    
    return moves
    
#Prüft ob die jeweilige position auf dem Feld leer ist
def isEmptyField(board,pos): 
    row, col = pos
    return board[row][col] == 0

#Funktion prüft, ob die die Zielposition ein valider Zug ist, ein Zug is INVALIDE wenn gilt:
#position Thronfeld ist
#Ein Bauer (Schwarz oder Weiß) versucht eins der Eckfelder/Zielfelder betreten versucht
def validMove(board,pos,Startpos):
    
    start_row, start_col = Startpos
    row,col = pos
    
    #Thronfeld wird versucht zu betreten, illegaler Move
    if (row,col) == config.Throne:
        return False
        
    #Bauer versucht Eckfeld/Zielfeld zu betreten, illegaler Move
    if ((row,col) in config.Goal):
        return (board[start_row][start_col] == config.K)
    

    return True
