import random
## die Funktion get_all_positions(State, White) erwartet eine 2D Liste "board" und 
## den Spieler (White oder Black) dessen alle Positionen auf dem Spielfeld übergeben werden soll 

def get_all_positions(board, player):
    """
    Sucht auf dem gesamten Spielfeld nach allen Figuren eines Spielers.

    Die Funktion durchläuft das 9x9-Board und sammelt alle Positionen,
    auf denen eine Figur des angegebenen Spielers steht.

    Args:
        board: 2D-Liste, die das Spielfeld repräsentiert.
        player: Spielername, z.B. "White" oder "Black".

    Returns:
        Eine Liste von Tupeln der Form (row, col) mit allen Positionen
        der Figuren dieses Spielers.
    """

    all_positions = []
    
    for i in range(9):
        for j in range(9):
            if check_valid_figure(player, board[i][j]):
                all_positions.append((i, j))
            
    return all_positions
                 
# Prüft ob die Figur den nächsten zuspielende Figur gehört             
def check_valid_figure(player, figure): 

    """
    Prüft, ob eine Figur zu dem Spieler gehört, der gerade am Zug ist.

    In dieser Implementierung gehören zu:
    - "White": die Figuren W und K
    - sonst: die Figur B

    Args:
        player: Spielername, z.B. "White" oder "Black".
        figure: Wert auf einem Feld des Boards.

    Returns:
        True, wenn die Figur dem Spieler gehört, sonst False.
    """

    if player == "White":
        return figure in [-1, -2]
    else:
        return figure in [1]                 




#Haupt-Funktion die dafür da ist alle Möglichen Spielzüge des jeweiligen Spielers zu bestimmen 
def total_moves(Board,White):
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

    all_player_positions = get_all_positions(Board,White)
    all_moves = {}
    
    for  (row,col) in all_player_positions:
        all_moves = merge_moves(all_moves,(get_figures_Moves(Board,White,(row,col))))
    
    return all_moves    

# Gibt alle möglichen Zug der jeweiligen Figur (Position) an    
def get_figures_Moves(Board,White,Pos): 

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
    
    start_line,start_row = Pos 
    
    #Berechnet alle möglichen Züge einer Figur nach oben        
    moves = merge_moves(moves,(all_moves_up_to_Figure(Board,Pos)))
    
    #Berechnet alle möglichen Züge einer Figur nach unten        
    moves= merge_moves(moves,(all_moves_right_to_Figure(Board,Pos)))
    
    #Berechnet alle möglichen Züge einer Figur nach rechts        
    moves= merge_moves(moves,(all_moves_down_to_Figure(Board,Pos)))

    #Berechnet alle möglichen Züge einer Figur nach links        
    moves= merge_moves(moves,(all_moves_left_to_Figure(Board,Pos)))
    
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
                #moves.append(((start_row,start_col),(row, col)))
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
                #moves.append(((start_line,start_row),(row, col)))
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
                #moves.append(((start_row,start_col),(row, col)))
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

    Nur der König (-2) darf auf ein Eckfeld ziehen.

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
    if (row,col) == (4,4):
        return False
        
    # Nur der König darf Eckfelder/Zielfelder betreten
    if (
        (row, col)    == (0, 0)
        or (row, col) == (0, 8)
        or (row, col) == (8, 0)
        or (row, col) == (8, 8)
    ):
        return board[start_row][start_col] == -2
    
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

###ADITIONAL: Printet nur Board, etc schöner im Terminal aus nicht wirklich der der Lögik

def print_board(board):
    size = len(board)

    for i, row in enumerate(board):
        # Zeilennummer links
        row_str = " ".join(f"{cell:>2}" for cell in row)
        print(f"{i}  {row_str}")

    print()

    # Spaltennummern unten
    col_numbers = "   " + " ".join(f"{i:>2}" for i in range(size))
    print(col_numbers)


def print_possible_Moves(list_Moves): 
    gruppen = {}
    
    #Erstellt eine dicitonary { (start ) : [alle möglichen Züge aus dieser Position] ... }
    for ((start),(goal)) in list_Moves:
        if start in gruppen:
            gruppen[start].append(goal)
        else:
            gruppen[start]=[goal]
            
    for key, value in gruppen.items():
        print(f"{key} -> {value}")
            

def print_dic(dict):
    for key, value in dict.items():
        print(f"{key}: {value},")


def print_board_colorful(board, old_board):
    RED = "\033[91m"
    RESET = "\033[0m"

    print("   ", end="")
    for i in range(len(board)):
        print(f"{i:2}", end=" ")
    print()

    for i in range(len(board)):
        print(f"{i:2} ", end="")
        for j in range(len(board[i])):
            
            val = board[i][j]

            # Wenn altes Board existiert → vergleichen
            if old_board and val != old_board[i][j]:
                print(f"{RED}{val:2}{RESET}", end=" ")
            else:
                print(f"{val:2}", end=" ")
        print()





