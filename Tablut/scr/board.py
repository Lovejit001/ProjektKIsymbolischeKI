import random
## die Funktion get_all_positions(State, White) erwartet eine 2D Liste "board" und 
## den Spieler (White oder Black) dessen alle Positionen auf dem Spielfeld übergeben werden soll 

def get_all_positions(board, player):
    all_positions = []
    
    for i in range(9):
        for j in range(9):
            if check_valid_figure(player, board[i][j]):
                all_positions.append((i, j))
            
    return all_positions
                 
# Prüft ob die Figur den nächsten zuspielende Figur gehört             
def check_valid_figure(player, figure): 
    if player == "White":
        return figure in [-1, -2]
    else:
        return figure in [1]                 




#Haupt-Funktion die dafür da ist alle Möglichen Spielzüge des jeweiligen Spielers zu bestimmen 
def total_moves(Board,White):
    all_player_positions = get_all_positions(Board,White)
    all_moves = {}
    
    for  (row,col) in all_player_positions:
        all_moves = merge_moves(all_moves,(get_figures_Moves(Board,White,(row,col))))
    
    return all_moves    

# Gibt alle möglichen Zug der jeweiligen Figur (Position) an    
def get_figures_Moves(Board,White,Pos): 
    moves = {}
    
    start_line,start_row = Pos 
     
    moves = merge_moves(moves,(all_moves_up_to_Figure(Board,Pos)))
    
    moves= merge_moves(moves,(all_moves_right_to_Figure(Board,Pos)))
    
    moves= merge_moves(moves,(all_moves_down_to_Figure(Board,Pos)))

    moves= merge_moves(moves,(all_moves_left_to_Figure(Board,Pos)))
    
    return moves

def merge_moves(oldMoves :dict ,newMoves: dict):
    
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

#Funktion prüft, ob die die Zielposition ein valider Zug ist, ein Zug is INVALIDE wenn gilt:
#Position Thronfeld ist
#Ein Bauer (Schwarz oder Weiß) versucht eins der Eckfelder/Zielfelder betreten versucht
def validMove(board,Pos,StartPos):
    
    start_row, start_col = StartPos
    row,col = Pos
    
    #Thronfeld wird versucht zu betreten, illegaler Move
    if (row,col) == (4,4):
        return False
        
    #Bauer versucht Eckfeld/Zielfeld zu betreten, illegaler Move
    if ((row,col) == (0,0) or (row,col) == ( 0,(len(board[0])-1) ) or (row,col) == (len(board)-1,0) or (row,col) == (len(board)-1,(len(board[8])-1)) ):
        return (board[start_row][start_col] == -2)
    

    return True

# Konvertertiert Zeilen Bezeichnung des Brettes in Zahl um:
# z.B a -> 0

def convert_row(spelling):
    return ord(spelling.lower()) - ord('a')


#Funktion da damit man das Board einmal sich ausgeben kann:

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


#Das Spiel ist beendet wenn einer der folgenden Ereignisse eintretet:
#   -Schwarz gewinnt, wenn König wurde geschlagen                       Output: -1
#   -Weiß gewinnt, wenn König erreicht einer der vier Eckfelder         Output:  1
#   -Unentschieden, wenn:
#                   sich eine Stellung, 
#                   wenn ein Spieler keinen Zug mehr machen kann, 
#                   50 Züge keine figur geschlagen wurde                Output:  0
#    -Spiel läuft weiter                                                output: 10
def isGameOver():...

#


#Diese Funktion führt die Schritt aus und aktualisiert Board
def makeMove(board,all_possible_moves):

    random_move= random.choice(list(all_possible_moves.items()))

    start_Pos, goal_Pos = random_move
    
    start_row, start_col = start_Pos
    
    goal_row, goal_col = goal_Pos
    

    #Figuer merken die auf der Startposition ist: 
    figure = board[start_row][start_col]

    #Board an der Startposition, leeren:
    board[start_row][start_col] = "E"
    
    #Board an der Startposition, aktualisieren:
    board[goal_row][goal_col] = figure
    

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

print("NUN SCHÖNERE VERSION:")
print_possible_Moves(x)
