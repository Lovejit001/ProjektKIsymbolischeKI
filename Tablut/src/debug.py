from src import config
from tests import definitions

def print_dic(dict):
    for key, value in dict.items():
        print(f"{key}: {value},")

def print_board1(board):
    size = len(board)

    for i, row in enumerate(board):
        # Zeilennummer links
        row_str = " ".join(f"{cell:>2}" for cell in row)
        print(f"{i}  {row_str}")

    print()

    # Spaltennummern unten
    col_numbers = "   " + " ".join(f"{i:>2}" for i in range(size))
    print(col_numbers)


def print_board(board):
    size = len(board)
    
    # ANSI-Farbcodes
    BLUE = '\033[94m'    # Blau für König
    GREEN = '\033[92m'   # Grün für Weiß
    RED = '\033[91m'     # Rot für Schwarz
    RESET = '\033[0m'    # Reset
    
    for i, row in enumerate(board):
        # Zeilennummer links
        row_str = []
        for cell in row:
            if cell == 'K':
                row_str.append(f"{BLUE}{cell:>2}{RESET}")
            elif cell == 'W':
                row_str.append(f"{GREEN}{cell:>2}{RESET}")
            elif cell == 'B':
                row_str.append(f"{RED}{cell:>2}{RESET}")
            else:
                row_str.append(f"{cell:>2}")
        print(f"{i}  {' '.join(row_str)}")
    
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


def FenToBoard(fen: str):  

    if fen == "":        
        fen ="3aaa3/4a4/4d4/a3d3a/aaddkddaa/a3d3a/4d4/4a4/3aaa3 a 0 0"
    #print("1")
    parts = fen.split()
    #print("2")
    if len(parts) < 4:
        raise ValueError("Ungültiger FEN-String: zu wenige Teile")
    #print("3")
    board_part = parts[0]
    #print("4")
    side_to_move = parts[-3] #onTurn
    #print("5")
    halfmove_clock = int(parts[-2]) #50 Züge rügel
    #print("6")
    fullmove_number = int(parts[-1]) #
    #print("7")
    #Wird in Client.py festgelegt wer drann ist, denn wer vom Server "Start" erhält wird diese Art von Figur sein.
    #if side_to_move == 'a':
    #    config.onTurn = 'Black'
    #else:
    #    config.onTurn = 'White'
    #print("8")
    config.zugCounter = fullmove_number
    #print("9")
    config.zugRegel = halfmove_clock
    #print("10")
    return fen_to_array(board_part), side_to_move

#konvertiert FEN-Notation zu einem 2d Array (Board)
def fen_to_array(fen: str):
    board_part = fen.split()[0]          # nur der Brett-Teil vor dem ersten Leerzeichen
    rows = board_part.split("/")

    board = []
    for row in rows:
        current_row = []
        for char in row:
            if char.isdigit():
                current_row.extend([0] * int(char))   # Leerfelder
            else:
                if char == 'a':    
                    current_row.append('B')
                elif char == 'd':
                    current_row.append('W')
                elif char == 'k':
                    current_row.append('K')                    
        board.append(current_row)

    return board

def countMoves(moves :dict):
    counter = 0
    for startPos,list_moves in moves.items():
        counter += len(list_moves)
    return counter
 


#fenStr = "9/9/4d4/a3d3a/aadd1ddaa/a3d3a/4d4/4a4/3aka3 a 0 0"

#board = FenToBoard(fenStr)

#print_board(board)
#print(config.onTurn)
#print(config.zugCounter)
#print(config.zugRegel)