
## die Funktion get_all_positions(State, White) erwartet eine 2D Liste "board" und 
## den Spieler (White oder Black) dessen alle Positionen auf dem Spielfeld übergeben werden soll 

def get_all_positions(State,White):
    all_positions = []
    
    for i, line in enumerate(State):
        for j, element in enumerate(line):
            Figure = State[i][j]
            if check_valid_figure(White,Figure):
                #print(f"FIGURE IS WHITE TEAM  {Figure} on POSITIONS {i} {j}" ) 
                #all_moves.extend(get_figures_Moves(State, White, (i,j)))
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
    all_moves = []
    
    for  (row,col) in all_player_positions:
        all_moves.extend(get_figures_Moves(State,White,(row,col)))
    
    return all_moves    

# Gibt alle möglichen Zug der jeweiligen Figur (Position) an    
def get_figures_Moves(State,White,Pos): 
    moves = []
    start_line,start_row = Pos 
     
    moves.extend(all_moves_up_to_Figure(State,Pos))
    
    moves.extend(all_moves_down_to_Figure(State,Pos))
            
    moves.extend(all_moves_left_to_Figure(State,Pos))
    
    moves.extend(all_moves_right_to_Figure(State,Pos))
    
    return moves

def all_moves_up_to_Figure(State, StartPos):
    moves = []
    (start_line,start_row) = StartPos

    row, col = StartPos
    row -= 1

    while row >= 0:
            
        if isEmptyField(State,(row,col)):
            row -=1
            if row == 0 and isEmptyField(State,(row,col)) : moves.append(((start_line,start_row),(row, col)))
        else: 
            moves.append(((start_line,start_row),(row+1, col)))
            break
            
    
    return moves

def all_moves_down_to_Figure(State, StartPos):
    moves = []
    (start_line,start_row) = StartPos
    
    row, col = StartPos
    row += 1

    while row <= (len(State)-1):

        if isEmptyField(State,(row,col)):
            row += 1
            if row == 8 and isEmptyField(State,(row,col)) : 
                moves.append(((start_line,start_row),(row, col)))
        else: 
            moves.append(((start_line,start_row),(row-1, col)))
            print(moves)
            break
    return moves
    

def all_moves_left_to_Figure(State, StartPos):
    moves = []
    (start_line,start_row) = StartPos
    
    row, col = StartPos
    col -= 1
    while col >= 0:
        
        if isEmptyField(State,(row,col)):
            col -= 1
            if col == 0 and isEmptyField(State,(row,col)): moves.append(((start_line,start_row),(row, col)))
        else: 
            moves.append(((start_line,start_row),(row, col+1)))
            break
    
    
    
    return moves

def all_moves_right_to_Figure(State, StartPos):
    
    moves = []
    (start_line,start_row) = StartPos
    
    row, col = StartPos
    col += 1

    while col <= (len(State[0])-1):
        if isEmptyField(State,(row,col)):
            col += 1
            if col == 8 and isEmptyField(State,(row,col)) : moves.append(((start_line,start_row),(row, col)))
        else: 
            moves.append(((start_line,start_row),(row,col-1)))
            break
    
    
    return moves
    
#Prüft ob die jeweilige Position auf dem Feld leer ist
def isEmptyField(State,Pos): 
    row, col = Pos
    return State[row][col] == "E"




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


TestBoard = [
    ["W","E","E","E","E","E","E","E","E"],
    ["E","E","E","E","E","E","E","E","E"],
    ["E","E","E","E","E","E","E","E","E"],
    ["E","E","E","E","E","E","E","E","E"],
    ["E","E","E","E","W","E","E","E","E"],
    ["E","E","E","E","E","E","E","E","E"],
    ["B","E","E","E","E","E","E","E","E"],
    ["E","E","E","E","E","E","E","E","E"],
    ["E","E","E","E","E","E","E","E","W"],
]

print_board(TestBoard)

#x = Zuggenerator(TestBoard,True)
#print(x)

