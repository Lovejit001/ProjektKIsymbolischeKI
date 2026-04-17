
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
    
def get_figures_Moves(State,White,Pos): 
    moves = []
    start_line,start_row = Pos 
     
    row, col = Pos
    row -= 1
    print(f"ZEILE: {row} ")
    while row >= 0:
        print("BIN DRIN")    
            
        if isEmptyField(State,(row,col)):
            print(f"FIELD IS FREE {row} {col}")
            row -=1
            if row == 0 and isEmptyField(State,(row,col)) : moves.append(((start_line,start_row),(row, col)))
        else: 
            moves.append(((start_line,start_row),(row+1, col)))
            break
            
    
    row, col = Pos
    row += 1
    print(f"JETZT alles unter mir {row} {col}" )            
    while row <= (len(State)-1):

        if isEmptyField(State,(row,col)):
            print(f"FIELD IS FREE {row} {col}")
            row += 1
            print(f"TO TEST FIELD {row} {col}")
            if row == 8 and isEmptyField(State,(row,col)) : 
                print("WIR SIND AM ENDE")
                moves.append(((start_line,start_row),(row, col)))
        else: 
            print(f"KANNST HÖCHSTENS BIS {row-1} {col}")
            moves.append(((start_line,start_row),(row-1, col)))
            print(moves)
            break
        print(f"TO TEST FIELD {row} {col}")
        print(f"{row} <= ? {(len(State)-1)}")
    
        
    row, col = Pos
    col -= 1
    while col >= 0:
        
        if isEmptyField(State,(row,col)):
            col -= 1
            if col == 0 and isEmptyField(State,(row,col)): moves.append(((start_line,start_row),(row, col)))
        else: 
            moves.append(((start_line,start_row),(row, col+1)))
            break
    
    row, col = Pos
    col += 1

    while col <= (len(State[0])-1):
        if isEmptyField(State,(row,col)):
            col += 1
            if col == 8 and isEmptyField(State,(row,col)) : moves.append(((start_line,start_row),(row, col)))
        else: 
            moves.append(((start_line,start_row),(row,col-1)))
            break
    return moves


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
    ["W","E","W","E","E","E","E","E","E"],
    ["E","E","E","E","E","E","E","E","E"],
    ["E","E","E","E","E","E","E","E","E"],
    ["E","E","E","E","E","E","E","E","E"],
    ["E","E","E","E","E","E","E","E","E"],
    ["E","E","E","E","E","E","E","E","E"],
    ["E","E","E","E","E","E","E","E","E"],
    ["E","E","E","E","E","E","E","E","E"],
    ["B","E","E","E","E","E","E","E","W"],
]



x = Zuggenerator(TestBoard,False)
print(x)

