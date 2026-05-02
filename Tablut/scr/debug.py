from scr import config

def print_dic(dict):
    for key, value in dict.items():
        print(f"{key}: {value},")

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


def parse_fen_tail(fen: str):
    parts = fen.split()

    if len(parts) < 4:
        raise ValueError("Ungültiger FEN-String: zu wenige Teile")

    board_part = parts[0]
    side_to_move = parts[-3] #onTurn
    halfmove_clock = int(parts[-2]) #50 Züge rügel
    fullmove_number = int(parts[-1]) #

    if side_to_move == 's':
        config.onTurn = 'Black'
    else:
        config.onTurn = 'White'
    
    config.zugCounter = fullmove_number

    config.zugRegel = halfmove_clock

    return fen_to_array(board_part)

#konvertiert FEN-Notation zu einem 2d Array (Board)
def fen_to_array(fen: str):
    board_part = fen.split()[0]          # nur der Brett-Teil vor dem ersten Leerzeichen
    rows = board_part.split("/")

    board = []
    for row in rows:
        current_row = []
        for char in row:
            if char.isdigit():
                current_row.extend(["0"] * int(char))   # Leerfelder
            else:
                if char == 'r':    
                    current_row.append('B')
                elif char == 'R':
                    current_row.append('W')
                else:
                    current_row.append(char)                    # Figur
        board.append(current_row)
     
    return board

fen = "3rrr3/4r4/4R4/r3R3r/rrRRKRRrr/r3R3r/4R4/4r4/3rrr3 s 0 1"

print_board(parse_fen_tail(fen))


print(config.onTurn)

print(config.zugRegel)

print(config.zugCounter)

