import config
from debug import print_board
## Funktion prüft ob nachdem erledigten Schachzug eine Figur geschlagen wird oder nicht ? 
## Dieser FALL wurde noch nicht behandelt 
## Befindet sich der König auf dem Thron und ist er auf drei Seiten von Angreifern 
## und auf der vierten Seite von einem Verteidiger umzingelt, 
## kann der Verteidiger geschlagen werden, indem man ihn zwischen einem Angreifer und dem König einkesselt (18)


def attack(board, Pos):
    #global W_pieces, B_pieces

    row, col = Pos
    
    # Spieler Schwarz hat gezogen und greift Weiß an
    if board[row][col] == config.B:
        # nach oben
        if row > 0 and (board[row-1][col] in (config.W, config.K)):
            if (board[row-1][col] == config.K) and ((row-1,col) in ((4,4),(4,3),(3,4),(4,5),(5,4))): 
                if isKingSurrounded(board,(row-1,col)) or isKingNextToThron(board,(row-1,col)): 
                    board[row-1][col] = 0
                    config.zugRegel = 0
                    config.W_pieces -= 1
                    config.K_pieces -= 1
            elif row-2 >= 0 and isAtCorner((row-2,col)):  
                board[row-1][col] = 0
                config.zugRegel = 0
                config.W_pieces -= 1
            elif row-2 >= 0 and board[row-2][col] == config.B:   
                board[row-1][col] = 0
                config.zugRegel = 0
                config.W_pieces -= 1
        
        # nach unten
        if row < 8 and (board[row+1][col] in (config.W, config.K)):
            if (board[row+1][col] == config.K) and (row+1,col) in ((4,4),(4,3),(3,4),(4,5),(5,4)): 
                if isKingSurrounded(board,(row+1,col)) or isKingNextToThron(board,(row+1,col)):
                    board[row+1][col] = 0
                    config.zugRegel = 0
                    config.W_pieces -= 1
                    config.K_pieces -= 1
            elif row+2 <= 8 and isAtCorner((row+2,col)):  
                board[row+1][col] = 0
                config.zugRegel = 0
                config.W_pieces -= 1
            elif row+2 <= 8 and board[row+2][col] == config.B:   
                board[row+1][col] = 0
                config.zugRegel = 0
                config.W_pieces -= 1
        
        # nach links
        if col > 0 and (board[row][col-1] in (config.W, config.K)):
            if (board[row][col-1] == config.K) and (row,col-1) in ((4,4),(4,3),(3,4),(4,5),(5,4)): 
                if isKingSurrounded(board,(row,col-1)) or isKingNextToThron(board,(row,col-1)):
                    board[row][col-1] = 0
                    config.zugRegel = 0
                    config.W_pieces -= 1
                    config.K_pieces -= 1
            elif col-2 >= 0 and isAtCorner((row,col-2)):  
                board[row][col-1] = 0
                config.zugRegel = 0
                config.W_pieces -= 1
            elif col-2 >= 0 and board[row][col-2] == config.B:   
                board[row][col-1] = 0
                config.zugRegel = 0
                config.W_pieces -= 1
        
        # nach rechts
        if col < 8 and (board[row][col+1] in (config.W, config.K)):
            if (board[row][col+1] == config.K) and (row,col+1) in ((4,4),(4,3),(3,4),(4,5),(5,4)): 
                if isKingSurrounded(board,(row,col+1)) or isKingNextToThron(board,(row,col+1)):
                    board[row][col+1] = 0
                    config.zugRegel = 0
                    config.W_pieces -= 1
                    config.K_pieces -= 1
            elif col+2 <= 8 and isAtCorner((row,col+2)):  
                board[row][col+1] = 0
                config.zugRegel = 0
                config.W_pieces -= 1
            elif col+2 <= 8 and board[row][col+2] == config.B:   
                board[row][col+1] = 0
                config.zugRegel = 0
                config.W_pieces -= 1
    
    # Spieler Weiß hat gezogen und greift an
    elif board[row][col] in (config.W, config.K):
        # nach oben
        if row > 0 and (board[row-1][col] == config.B):
            if row-2 >= 0 and isAtCorner((row-2,col)):  
                board[row-1][col] = 0
                config.zugRegel = 0
                config.B_pieces -= 1
            elif row-2 >= 0 and board[row-2][col] in (config.W, config.K):  
                board[row-1][col] = 0
                config.zugRegel = 0
                config.B_pieces -= 1
        
        # nach unten
        if row < 8 and (board[row+1][col] == config.B):
            if row+2 <= 8 and isAtCorner((row+2,col)):  
                board[row+1][col] = 0
                config.zugRegel = 0
                config.B_pieces -= 1
            elif row+2 <= 8 and board[row+2][col] in (config.W, config.K):  
                board[row+1][col] = 0
                config.zugRegel = 0
                config.B_pieces -= 1
        
        # nach links
        if col > 0 and (board[row][col-1] == config.B):
            if col-2 >= 0 and isAtCorner((row,col-2)):  
                board[row][col-1] = 0
                config.zugRegel = 0
                config.B_pieces -= 1
            elif col-2 >= 0 and board[row][col-2] in (config.W, config.K):  
                board[row][col-1] = 0
                config.zugRegel = 0
                config.B_pieces -= 1
        
        # nach rechts
        if col < 8 and (board[row][col+1] == config.B):
            if col+2 <= 8 and isAtCorner((row,col+2)):
                board[row][col+1] = 0
                config.zugRegel = 0
                config.B_pieces -= 1
            elif col+2 <= 8 and board[row][col+2] in (config.W, config.K):
                board[row][col+1] = 0
                config.zugRegel = 0
                config.B_pieces -= 1

    print("Der Board nach dem Attack:")
    print_board(board)

    return board

def isKingSurrounded(board, Pos):
    row, col = Pos
    return (
        board[4][4] == config.K
        and Pos == (4, 4)
        and board[row - 1][col] == config.B
        and board[row + 1][col] == config.B
        and board[row][col - 1] == config.B
        and board[row][col + 1] == config.B
    )

def isKingNextToThron(board, Pos):
    row, col = Pos
    if board[row][col] == config.K:
        if Pos == (3, 4):
            return (board[row][col - 1] == config.B and
                    board[row - 1][col] == config.B and
                    board[row][col + 1] == config.B)
        elif Pos == (5, 4):
            return (board[row][col - 1] == config.B and
                    board[row + 1][col] == config.B and
                    board[row][col + 1] == config.B)
        elif Pos == (4, 3):
            return (board[row - 1][col] == config.B and
                    board[row][col - 1] == config.B and
                    board[row + 1][col] == config.B)
        elif Pos == (4, 5):
            return (board[row - 1][col] == config.B and
                    board[row][col + 1] == config.B and
                    board[row + 1][col] == config.B)
    return False

def isAtCorner(Pos):
    row, col = Pos
    
    at_corner = (
        (row == 0 and col == 0) or
        (row == 0 and col == 8) or
        (row == 8 and col == 0) or
        (row == 8 and col == 8)
    )
    
    out_of_bounds = (row == -1 or row == 9 or col == -1 or col == 9)
    
    return at_corner or out_of_bounds
