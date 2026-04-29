from board import * 
from makeMove import makeMove






#Muss noch ausgebessert werden
def main():

    board = [
    [0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, -1, 0, 0, 0, 0],
    [1, 0, 0, 0, -1, 0, 0, 0, 1],
    [1, 1, -1, -1, -2, -1, -1, 1, 1],
    [1, 0, 0, 0, -1, 0, 0, 0, 1],
    [0, 0, 0, 0, -1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 0, 0]
    ]

    White = "Black"

    gameOver = False

    while not gameOver:
        
        print_board(board)
        allMoves = total_moves(board,White)
        board =makeMove(board,allMoves)
        print_board(board)
        break

    print("GAME OVER")



    
    
if __name__ == "__main__" :
    main()