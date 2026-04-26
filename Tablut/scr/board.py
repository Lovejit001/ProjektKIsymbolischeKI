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

    random_StartPos = random.choice(list(all_possible_moves.keys()))
    random_GoalPos = random.choice(list(all_possible_moves[random_StartPos])) 
    
    start_row, start_col = random_StartPos
    
    goal_row, goal_col = random_GoalPos
    
    #Figuer merken die auf der Startposition ist: 
    figure = board[start_row][start_col]

    #Board an der Startposition, leeren:
    board[start_row][start_col] = 0
    
    #Board an der Startposition, aktualisieren:
    board[goal_row][goal_col] = figure
    

    board = attack(board,random_GoalPos)

    return board

#Funktion prüft üb nachdem erledigten Schachzug eine Figur geschlagen wird oder nicht ? 
#Dieser FALL wurde noch nicht behandelt 
#Befindet sich der König auf dem Thron und ist er auf drei Seiten von Angreifern und auf der vierten Seite von einem Verteidiger umzingelt, kann der Verteidiger geschlagen werden, indem man ihn zwischen einem Angreifer und dem König einkesselt (18)
def attack(board,Pos):
    
    row, col = Pos

    print(board[row][col])
    print(board[row][col] == (-1, -2))
    #Spieler Schwarz mit Move und Angriff dran
    if board[row][col] == 1:

        #Spieler drüber wird ggf. geschlagen
        if row > 0 and (board[row-1][col] in (-1, -2)) :

            #Wenn das gilt ist Gegner Figur am Rand des Boards
            if (row-1,col) in ((4,4),(4,3),(3,4),(4,5), (5,4)): 

                if isKingSurrounded(board,(row-1,col)) or isKingNextToThron(board,(row-1,col)):
                    board[row-1][col] = 0

            elif isAtCorner((row-2,col)):

                board[row-1][col] = 0
            elif board[row-2][col] == 1 :

            #Wenn das gilt ist Gegner Figur eingeschlossen von aktuellen Spieler    
                board[row-1][col] = 0
        
        #Spieler drunter wird ggf. geschlagen
        if row < 8 and (board[row+1][col] in (-1, -2)) :
            print("A")
            if (row+1,col) in ((4,4),(4,3),(3,4),(4,5),(5,4)): 
                print("B")
                if isKingSurrounded(board,(row+1,col)) or isKingNextToThron(board,(row+1,col)):
                    print("C")
                    board[row+1][col] = 0
            elif isAtCorner((row+2,col)):

                board[row+1][col] = 0
            elif board[row+2][col] == 1:

                board[row+1][col] = 0
        
        #Spieler links wird ggf. geschlagen
        if col > 0 and (board[row][col-1] in (-1, -2)):

            if (row,col-1) in ((4,4),(4,3),(3,4),(4,5), (5,4)): 
                if isKingSurrounded(board,(row,col-1)) or isKingNextToThron(board,(row,col-1)):

                    board[row][col-1] = 0
            elif isAtCorner((row,col-2)):

                board[row][col-1] = 0
            elif board[row][col-2] == 1 :

                board[row][col-1] = 0

        #Spieler rechts wird ggf. geschlagen
        if col < 8 and (board[row][col+1] in (-1, -2)) :

            if (row,col+1) in ((4,4),(4,3),(3,4),(4,5), (5,4)): 
                if isKingSurrounded(board,(row,col+1)) or isKingNextToThron(board,(row,col+1)):
                    board[row][col+1] = 0
            elif isAtCorner((row,col+2)):

                board[row][col+1] = 0
            elif board[row][col+2] == 1:

                board[row][col+1] = 0
    
    #Spieler Weiß mit Move und Angriff dran      
    elif board[row][col] in (-1, -2) : 
        #Spieler drüber wird ggf. geschlagen
        if row > 0 and (board[row-1][col] == 1) :
            if isAtCorner((row-2,col)):
                board[row-1][col] = 0
            elif board[row-2][col] in (-1, -2) :
                board[row-1][col] = 0
        
        #Spieler drunter wird ggf. geschlagen
        if row < 8 and (board[row+1][col] == 1) :
            if isAtCorner((row+2,col)):
                board[row+1][col] = 0
            elif board[row+2][col] in (-1, -2):
                board[row+1][col] = 0
        
        #Spieler links wird ggf. geschlagen
        if col > 0 and (board[row][col-1] == 1):
            if isAtCorner((row,col-2)):
                board[row][col-1] = 0
            elif board[row][col-2] in (-1, -2) :
                board[row][col-1] = 0

        #Spieler rechts wird ggf. geschlagen
        if col < 8 and (board[row][col+1] == 1) :
            if isAtCorner((row,col+2)):
                board[row][col+1] = 0
            elif board[row][col+2] in (-1, -2):
                board[row][col+1] = 0
    return board

# Funktion prüft ob könig im Thron, umzingelt ist
def isKingSurrounded(board,Pos):
    
    row, col = Pos
    
    return (board[4][4] == -2) and (Pos == (4,4)) and (board[row-1][col] == 1) and (board[row+1][col] == 1) and (board[row][col-1] == 1) and (board[row][col+1] == 1)

def isKingNextToThron(board,Pos):

    row, col = Pos
    #prüft ob König neben Thron ist
    if board[row][col] == -2:
        #befindet sich über den Thron
        if Pos == (3,4):
            return (board[row][col-1] == 1) and (board[row-1][col] == 1) and (board[row][col+1] == 1)
        #befindet sich unter den Thron
        elif Pos == (5,4):
            return (board[row][col-1] == 1) and (board[row+1][col] == 1) and (board[row][col+1] == 1)
        #befindet sich links vom Thron
        elif Pos == (4,3):
            print("HIERR")
            return (board[row-1][col] == 1) and (board[row][col-1] == 1) and (board[row+1][col] == 1)
        #befindet sich rechts vom Thron
        elif Pos == (4,5):
            return (board[row-1][col] == 1) and (board[row][col+1] == 1) and (board[row+1][col] == 1)
    
    return False



def isAtCorner(Pos):
    row , col= Pos
    #Ist Eckfeld
    flag1 = (row == 0 and col == 0 )
    flag2 = (row == 0 and col == 8 )
    flag3 = (row == 8 and col == 0 )
    flag4 = (row == 8 and col == 8 )
    flag5 = (col == -1)
    flag6 = (row == -1)
    flag7 = (col ==  9)
    flag8 = (row ==  9)
    #Ist Thron
    flag9 = (row == 4 and col == 4) 

    return flag1 or flag2 or flag3 or flag4 or flag5 or flag6 or flag7 or flag8



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


TestBoard= [
    [0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, -1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, -2, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0] 
]


attackBoard24 = [
    [0, -1, 0, 0, 0, 0, 0, -1, 0],
    [-2, 1, 0, 0, 0, 0, 0, 1, -1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, -1],
    [-1, 1, 0, 0, 0, 0, 0, -1, 1],
    [0, -1, 0, 0, 0, 0, -1, 1, 0] 
]

x=attack(attackBoard24,(7,1))

print_board(x)



