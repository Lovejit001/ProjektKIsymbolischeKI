#Diese Funktion führt die Schritt aus und aktualisiert Board
import random
#from board import print_board

def makeMove(board,all_possible_moves):
    """
    Wählt zufällig einen zulässigen Zug aus und führt ihn auf dem Board aus.
    Danach wird geprüft, ob durch den Zug Gegnerfiguren geschlagen werden.

    Args:
        board: 2D‑Liste (9x9) mit Figuren‑IDs (z.B. B = Schwarz, W, K = Weiß).
        all_possible_moves: dict {start_pos: [list of goal_pos]} mit allen möglichen Zügen.

    Returns:
        Aktualisiertes Board nach dem Zug und allen Angriffen.
    """
    # Zufälligen Startpunkt auswählen
    random_StartPos = random.choice(list(all_possible_moves.keys()))
    # Zufälligen Zielpunkt aus allen Zielen vom Startpunkt wählen
    random_GoalPos = random.choice(list(all_possible_moves[random_StartPos])) 
    
    start_row, start_col = random_StartPos
    
    goal_row, goal_col = random_GoalPos
    
    # Figur auf der Startposition merken
    figure = board[start_row][start_col]

    # Startposition leeren
    board[start_row][start_col] = 0
    
    # Zielposition mit der Figur belegen
    board[goal_row][goal_col] = figure
    
    # Prüfen, ob nach dem Zug Figuren geschlagen werden
    board = attack(board,random_GoalPos)

    return board


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
    if board[row][col] == 1:

        # nach oben
        if row > 0 and (board[row-1][col] in (-1, -2)) :

            # Fall 1: Gegner steht im Thron‑Bereich (4,4 und Umgebung)
            #WAS IST MIT DEM FALL WEN NEBEN THORN EIN WEI?ER BAUER IST KANN ER EINGEKESSELT WERDEN ? 
            if (board[row-1][col] == -2) and ((row-1,col) in ((4,4),(4,3),(3,4),(4,5),(5,4))): 
                if isKingSurrounded(board,(row-1,col)) or isKingNextToThron(board,(row-1,col)): 
                    board[row-1][col] = 0
            # Fall 2: Gegner ist direkt am Rand (nächste Position ist „Corner“)
            elif isAtCorner((row-2,col)):
                board[row-1][col] = 0
            # Fall 3: Gegner ist eingeschlossen von einer eigenen Figur (Weiß)
            elif board[row-2][col] == 1:
            #Wenn das gilt ist Gegner Figur eingeschlossen von aktuellen Spieler    
                board[row-1][col] = 0
        
        # nach unten
        if row < 8 and (board[row+1][col] in (-1, -2)) :
            if (board[row+1][col] == -2) and (row+1,col) in ((4,4),(4,3),(3,4),(4,5),(5,4)): 
                if isKingSurrounded(board,(row+1,col)) or isKingNextToThron(board,(row+1,col)):
                    board[row+1][col] = 0
            elif isAtCorner((row+2,col)):
                board[row+1][col] = 0
            elif board[row+2][col] == 1:
                board[row+1][col] = 0
        
        # nach links
        if col > 0 and (board[row][col-1] in (-1, -2)):

            if (board[row][col-1] == -2) and (row,col-1) in ((4,4),(4,3),(3,4),(4,5), (5,4)): 
                if isKingSurrounded(board,(row,col-1)) or isKingNextToThron(board,(row,col-1)):
                    board[row][col-1] = 0
            elif isAtCorner((row,col-2)):
                board[row][col-1] = 0
            elif board[row][col-2] == 1 :
                board[row][col-1] = 0

        # nach rechts
        if col < 8 and (board[row][col+1] in (-1, -2)) :
            if (board[row][col+1] == -2) and (row,col+1) in ((4,4),(4,3),(3,4),(4,5), (5,4)): 
                if isKingSurrounded(board,(row,col+1)) or isKingNextToThron(board,(row,col+1)):
                    board[row][col+1] = 0
            elif isAtCorner((row,col+2)):
                board[row][col+1] = 0
            elif board[row][col+2] == 1:
                board[row][col+1] = 0
    
    # Spieler Weiß hat gezogen und greift an 
    elif board[row][col] in (-1, -2) : 
        # nach oben
        if row > 0 and (board[row-1][col] == 1) :
            if isAtCorner((row-2,col)):
                board[row-1][col] = 0
            elif board[row-2][col] in (-1, -2) :
                board[row-1][col] = 0
        
        # nach unten
        if row < 8 and (board[row+1][col] == 1) :
            if isAtCorner((row+2,col)):
                board[row+1][col] = 0
            elif board[row+2][col] in (-1, -2):
                board[row+1][col] = 0
        
        # nach links
        if col > 0 and (board[row][col-1] == 1):
            if isAtCorner((row,col-2)):
                board[row][col-1] = 0
            elif board[row][col-2] in (-1, -2) :
                board[row][col-1] = 0

        # nach rechts
        if col < 8 and (board[row][col+1] == 1) :
            if isAtCorner((row,col+2)):
                board[row][col+1] = 0
            elif board[row][col+2] in (-1, -2):
                board[row][col+1] = 0
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
        board[4][4] == -2  # König auf Thron
        and Pos == (4, 4)
        and board[row - 1][col] == 1   # oben
        and board[row + 1][col] == 1   # unten
        and board[row][col - 1] == 1   # links
        and board[row][col + 1] == 1   # rechts
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
    #prüft ob König neben Thron ist
    if board[row][col] == -2:  # Es ist tatsächlich der König
        # König direkt oberhalb des Thrones
        if Pos == (3, 4):
            return (board[row][col - 1] == 1    # links
                    and board[row - 1][col] == 1  # oben
                    and board[row][col + 1] == 1)  # rechts

        # König direkt unterhalb des Thrones
        elif Pos == (5, 4):
            return (board[row][col - 1] == 1    # links
                    and board[row + 1][col] == 1  # unten
                    and board[row][col + 1] == 1)  # rechts

        # König links vom Thron
        elif Pos == (4, 3):
            return (board[row - 1][col] == 1    # oben
                    and board[row][col - 1] == 1  # links
                    and board[row + 1][col] == 1)  # unten

        # König rechts vom Thron
        elif Pos == (4, 5):
            return (board[row - 1][col] == 1    # oben
                    and board[row][col + 1] == 1  # rechts
                    and board[row + 1][col] == 1)  # unten
    
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


TestBoard2= [
    [0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, -1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, -1, 0, 0, 0, 0],
    [0, 0, 1, -1, 0, 1, -1, 0, 0],
    [0, 0, 0, 0, -1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0] 
]