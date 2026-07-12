from .testboard_for2Graph import all_boards
#from .testboards5 import all_boards
from src.debug import print_board
from src.checkBoard import checkBoard2
from src import config


i = 0
#for board in boards:
#    i += 1
#    print_board(board)
myB = None
for board in all_boards:
    i += 1
    config.reset_pieces()
    config.init_pieces(board)
        
    print_board(board)

print(i)



