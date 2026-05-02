from scr import config
from scr.debug import print_board
 

def attack(board,Pos):
    """
    Prüft nach einem Zug, ob bedrohte Gegnerfiguren geschlagen werden sollen.
    Wenn ja, wird die Gegnerfigur Feld auf 0 gesetzt (geschlagen).

    Args:
        board: 2D‑Liste (9x9) mit Figuren.
        Pos: Tuple (row, col) der Zugziel‑Position.

    Returns:
        Aktualisiertes Board nach allen Angriffs‑/Schlag‑Regeln.
    """

    row, col = Pos
    
    # Spieler Schwarz hat gezogen und greift Weiß an
    if board[row][col] == config.B:

        # nach oben
        if row > 0 and (board[row-1][col] in (config.W, config.K)) :
            # Fall 1: Gegner steht im Thron‑Bereich (4,4 und Umgebung)
            #WAS IST MIT DEM FALL WEN NEBEN THORN EIN WEI?ER BAUER IST KANN ER EINGEKESSELT WERDEN ? 
                                                                    #HIER VARIAVLE SOUROUNDINGTHRONE
            if (board[row-1][col] == config.K) and ((row-1,col) in ((4,4),(4,3),(3,4),(4,5),(5,4))): 
                if isKingSurrounded(board,(row-1,col)) or isKingNextToThron(board,(row-1,col)): 
                    board[row-1][col] = 0
                    config.zugRegel = 0
                    config.W_pieces -= 1
                    config.K_pieces -= 1
            # Fall 2: Gegner ist direkt am Rand (nächste Position ist „Corner“)
            elif isAtCorner((row-2,col)):
                board[row-1][col] = 0
                config.zugRegel = 0
                config.W_pieces -= 1
            # Fall 3: Gegner ist eingeschlossen von einer eigenen Figur (Weiß)
            elif board[row-2][col] == config.B:
            #Wenn das gilt ist Gegner Figur eingeschlossen von aktuellen Spieler    
                board[row-1][col] = 0
                config.zugRegel = 0
                config.W_pieces -= 1
        
        
        # nach unten
        if row < 8 and (board[row+1][col] in (config.W, config.K)) :
                                                                    #SOUROUNDING THRONE
            if (board[row+1][col] == config.K) and (row+1,col) in ((4,4),(4,3),(3,4),(4,5),(5,4)): 
                if isKingSurrounded(board,(row+1,col)) or isKingNextToThron(board,(row+1,col)):
                    board[row+1][col] = 0
                    config.zugRegel = 0
                    config.W_pieces -= 1
                    config.K_pieces -= 1
            elif isAtCorner((row+2,col)):
                board[row+1][col] = 0
                config.zugRegel = 0
                config.W_pieces -= 1

            elif board[row+2][col] == config.B:
                board[row+1][col] = 0
                config.zugRegel = 0
                config.W_pieces -= 1

        # nach links
        if col > 0 and (board[row][col-1] in (config.W, config.K)):

            if (board[row][col-1] == config.K) and (row,col-1) in ((4,4),(4,3),(3,4),(4,5), (5,4)): 
                if isKingSurrounded(board,(row,col-1)) or isKingNextToThron(board,(row,col-1)):
                    board[row][col-1] = 0
                    config.zugRegel = 0
                    config.W_pieces -= 1
                    config.K_pieces -= 1
            elif isAtCorner((row,col-2)):
                board[row][col-1] = 0
                config.zugRegel = 0
                config.W_pieces -= 1

            elif board[row][col-2] == config.B :
                board[row][col-1] = 0
                config.zugRegel = 0
                config.W_pieces -= 1

        # nach rechts
        if col < 8 and (board[row][col+1] in (config.W, config.K)) :
            if (board[row][col+1] == config.K) and (row,col+1) in ((4,4),(4,3),(3,4),(4,5), (5,4)): 
                if isKingSurrounded(board,(row,col+1)) or isKingNextToThron(board,(row,col+1)):
                    board[row][col+1] = 0
                    config.zugRegel = 0
                    config.W_pieces -= 1
                    config.K_pieces -= 1
            elif isAtCorner((row,col+2)):
                board[row][col+1] = 0
                config.zugRegel = 0
                config.W_pieces -= 1
            elif board[row][col+2] == config.B:
                board[row][col+1] = 0
                config.zugRegel = 0
                config.W_pieces -= 1

    
    # Spieler Weiß hat gezogen und greift an 
    elif board[row][col] in (config.W, config.K) : 
        # nach oben
        if row > 0 and (board[row-1][col] == config.B) :
            if isAtCorner((row-2,col)):
                board[row-1][col] = 0
                config.zugRegel = 0
                config.B_pieces -= 1
            elif board[row-2][col] in (config.W, config.K) :
                board[row-1][col] = 0
                config.zugRegel = 0
                config.B_pieces -= 1
        
        # nach unten
        if row < 8 and (board[row+1][col] == config.B) :
            if isAtCorner((row+2,col)):
                board[row+1][col] = 0
                config.zugRegel = 0
                config.B_pieces -= 1
            elif board[row+2][col] in (config.W, config.K):
                board[row+1][col] = 0
                config.zugRegel = 0
                config.B_pieces -= 1
        
        # nach links
        if col > 0 and (board[row][col-1] == config.B):
            if isAtCorner((row,col-2)):
                board[row][col-1] = 0
                config.zugRegel = 0
                config.B_pieces -= 1
            elif board[row][col-2] in (config.W, config.K) :
                board[row][col-1] = 0
                config.zugRegel = 0
                config.B_pieces -= 1

        # nach rechts
        if col < 8 and (board[row][col+1] == config.B):
            if isAtCorner((row,col+2)):
                board[row][col+1] = 0
                config.zugRegel = 0
                config.B_pieces -= 1
            elif board[row][col+2] in (config.W, config.K):
                board[row][col+1] = 0
                config.zugRegel = 0
                config.B_pieces -= 1

    print("Der Board nach dem Attack:")
    print_board(board)

    return board

# Funktion prüft ob könig im Thron, umzingelt ist
def isKingSurrounded(board,Pos):
    """
    Prüft, ob der König auf dem Thron (4,4) steht und auf allen vier Seiten
    von gegnerischen Figuren (Schwarz) umzingelt ist.

    Args:
        board: 2D‑Liste (9x9).
        Pos: Tuple (row, col) der zu prüfenden Position.

    Returns:
        bool: True, wenn König auf Thron ist und von allen Seiten umzingelt; sonst False.
    """
    
    row, col = Pos
    return (
        board[4][4] == config.K  # König auf Thron
        #####GEHT DAS 
        and Pos == config.Throne
        and board[row - 1][col] == config.B   # oben
        and board[row + 1][col] == config.B   # unten
        and board[row][col - 1] == config.B   # links
        and board[row][col + 1] == config.B   # rechts
    )


def isKingNextToThron(board,Pos):
    """
    Prüft, ob der König neben dem Thron (4,4) steht und auf drei Seiten von
    gegnerischen Figuren (Schwarz) umgeben ist, sodass eine Verteidigungsfigur geschlagen wird.

    Args:
        board: 2D‑Liste (9x9).
        Pos: Tuple (row, col) der zu prüfenden Position.

    Returns:
        bool: True, wenn König neben Thron steht und gegebenenfalls eine Figur geschlagen werden kann.
    """
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
    """
    Prüft, ob eine Position „außerhalb“ des Boards oder auf einem Eckfeld liegt.
    Dient als Bedingung, um Gegnerfiguren am Rand oder außerhalb des Boards zu schlagen.

    Args:
        Pos: Tuple (row, col).

    Returns:
        bool: True, wenn die Position außerhalb oder auf einem Eckfeld ist.
    """
    row , col= Pos

    # Normale Eckfelder (0,0), (0,8), (8,0), (8,8)
    at_corner = (
        (row == 0 and col == 0) or
        (row == 0 and col == 8) or
        (row == 8 and col == 0) or
        (row == 8 and col == 8)
    )

    # „Außerhalb“ des Boards (z.B. für Prüfungen der nächsten Position)
    out_of_bounds = (
        (row == -1) or
        (row == 9) or
        (col == -1) or
        (col == 9)
    )
    next_to_Thron = ((row,col) == (4,4))
 
    return at_corner or out_of_bounds or next_to_Thron




TestBoard= [
    [0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, -1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, -1, 0, 0, 0, 0],
    [1, -1, 0, -1, 1, 0, 0, 0, 0],
    [0, 0, -1, 1, 0, 1, -1, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, -1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0] 
]


expected1 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, -2, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0] 
]


TestBoard2 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, config.W, config.B, config.W, config.B, config.W, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0] 
]

x = attack(TestBoard2,(3,3))

print_board(x)