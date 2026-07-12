from .testboard_for2Graph import all_boards
from src.debug import print_board


i = 0
#for board in boards:
#    i += 1
#    print_board(board)
myB = None
for board in all_boards:
    i += 1
    print_board(board)

print(i)



