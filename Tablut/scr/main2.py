import time

from makeMove import makeMove

def isGameOver(x):
    return x == 10 

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

    player = "Black"

    gameOver = False

    counter = 0

    while not isGameOver(counter):
        
        print(f"{player} ist dran %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")

        # 🟢 ALTES BOARD SPEICHERN
        old_board = [row[:] for row in board]

        #allMoves = total_moves(board,player)
        #board =makeMove(board,allMoves)

        time.sleep(5) # pausiert 5 Sekunden 

        # 🔥 NEUES BOARD MIT MARKIERUNG
        #print_board_colorful(board, old_board)
            
        if player == "White":
            player = "Black"
        else:
            player = "White"

        counter += 1

    
    print("GAME OVER")



    
    
if __name__ == "__main__" :
    main()