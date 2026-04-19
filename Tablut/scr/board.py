
## die Funktion get_all_positions(State, White) erwartet eine 2D Liste "board" und 
## den Spieler (White oder Black) dessen alle Positionen auf dem Spielfeld übergeben werden soll 

def get_all_positions(State,White):
    all_positions = []
    
    for i, line in enumerate(State):
        for j, element in enumerate(line):
            Figure = State[i][j]
            if check_valid_figure(White,Figure):
                all_positions.append((i,j))                
                
    return all_positions
                 
            
# Prüft ob die Figur den nächsten zuspielende Figur gehört             
def check_valid_figure(White,figure): 
    if White == True:
        return figure in ["W","K"]
    else:
        return figure in ["B"]                 

#Haupt-Funktion die dafür da ist alle Möglichen Spielzüge des jeweiligen Spielers zu bestimmen 
def Zuggenerator(State,White):
    all_player_positions = get_all_positions(State,White)
    all_moves = {}
    
    for  (row,col) in all_player_positions:
        all_moves = merge_moves(all_moves,(get_figures_Moves(State,White,(row,col))))
    
    return all_moves    

# Gibt alle möglichen Zug der jeweiligen Figur (Position) an    
def get_figures_Moves(State,White,Pos): 
    moves = {}
    
    start_line,start_row = Pos 
     
    moves = merge_moves(moves,(all_moves_up_to_Figure(State,Pos)))

    moves= merge_moves(moves,(all_moves_down_to_Figure(State,Pos)))
    
    moves= merge_moves(moves,(all_moves_left_to_Figure(State,Pos)))
    
    moves= merge_moves(moves,(all_moves_right_to_Figure(State,Pos)))
            
    
    
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
def isEmptyField(State,Pos): 
    row, col = Pos
    return State[row][col] == "E"

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
        return (board[start_row][start_col] == "K")
    

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
            

TestBoard = [
    ["E","E","E","E","E","E","E","E","E"],
    ["E","E","E","E","E","E","E","E","E"],
    ["E","E","E","E","E","E","E","E","E"],
    ["E","E","E","E","E","E","E","E","E"],
    ["B","E","E","E","E","E","E","E","E"],
    ["E","E","E","E","E","E","E","E","E"],
    ["E","E","E","E","E","E","E","E","E"],
    ["E","E","E","E","E","E","E","E","E"],
    ["E","E","E","E","E","E","E","E","E"],
]

#print_board(TestBoard)

def print_dic(dict):
    for key, value in dict.items():
        print(f"{key} --> {value}")

x = Zuggenerator(TestBoard,False)
print_dic(x)


#print("NUN Output, wenn man Dictionary als eine große Liste Nutzt:")
#print_possible_Moves(x)
