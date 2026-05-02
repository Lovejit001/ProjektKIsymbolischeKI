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