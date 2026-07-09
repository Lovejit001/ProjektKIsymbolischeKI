from .testboards3 import boards
from src.debug import print_board

mein_board = boards
i = 0

for e in mein_board:
    i += 1
    print_board(e)


print(i)
