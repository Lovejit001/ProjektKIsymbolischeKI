from .testboards5 import all_boards
from src.debug import print_board
from benchmarks.compare1 import game
from src.checkBoard import checkBoard2

i = 0
#for board in boards:
#    i += 1
#    print_board(board)
myB = None
for board in all_boards:
    i += 1
    if i == 100:
        myB = board

#print(f"Anzahl der Durchläufe {i}")
#print("MEIN BOARD:")
#print_board(myB)
#res = game(myB)
#res = checkBoard2(myB)
#print_board(myB)
#print(f"Ergebnis ist {res}")


