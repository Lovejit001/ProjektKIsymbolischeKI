#import config

#from tests.definitions import B_pieces, W_pieces
## die Funktion get_all_pos(State, White) erwartet eine 2D Liste "board" und 
## den Spieler (White oder Black) dessen alle Positionen auf dem Spielfeld übergeben werden soll 

def get_all_pos(board, onTurn):
    #global W_pieces, B_pieces

    all_positions = []
    
    #if onTurn == "White":
    #    W_pieces = 0
    #else:
    #    B_pieces = 0

    for i in range(9):
        for j in range(9):
            if check_figure(onTurn, board[i][j]):
                all_positions.append((i, j))
    

    return all_positions
                 
# Prüft ob die Figur den nächsten zuspielende Figur gehört             
def check_figure(player, pos):
    #global W_pieces, B_pieces

    if player == "White":
        if pos in ('W', 'K'):
            #W_pieces += 1
            return True
        return False
    else:
        if pos == 'B':
            #B_pieces += 1
            return True
        return False
    

    