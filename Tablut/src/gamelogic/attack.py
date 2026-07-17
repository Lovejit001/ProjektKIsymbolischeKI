from src.gamelogic import config
from src.gamelogic.debug import print_board
from tests.definitions import W,B,K
 

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
    changed_list = []
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
                    changed_list.append(((row-1,col),config.K))
            # Fall 2: Gegner ist direkt am Rand (nächste Position ist „Corner“)
            #elif isAtCorner((row-2,col),board):
            elif ((row-1,col) == (1,0) or (row-1,col) == (1,8)):     
                #Ist die geschlagene Figur
                if board[row-1][col] == config.K:
                    config.K_pieces -= 1
                    changed_list.append(((row-1,col),config.K))
                else:
                    changed_list.append(((row-1,col),config.W))
                board[row-1][col] = 0
                config.zugRegel = 0
                config.W_pieces -= 1
            # Fall 3: Weiße Figur neben Thron (besetzt den Thron) und König eingekesselt von anderen 3 Seiten
            elif (board[row-1][col] == config.W and ((row-2,col) == (4,4)) and board[row-2][col] == config.K ):
                #König umzingelt von Gegner (drüber, links und rechts) 
                if board[row-3][col] == config.B and board[row-2][col-1] == config.B and board[row-2][col+1] == config.B:
                    board[row-1][col] = 0 
                    config.zugRegel = 0
                    config.W_pieces -= 1  
                    changed_list.append(((row-1,col),config.W))
            # Fall 4: Gegner (Weiß Bauer) ist eingeschlossen vom Gegner und Thron
            elif (row-1,col) == (5,4) and board[row-1][col] == config.W:
                board[row-1][col] = 0
                config.zugRegel = 0
                config.W_pieces -= 1
                changed_list.append(((row-1,col),config.W))
            
            # Fall 5: Gegner (Weiß Bauer oder König) ist eingeschlossen von einer eigenen Figur (Schwarz)    
            elif (row -1 >= 1) and board[row-2][col] == config.B:
                if board[row-1][col] == config.K:
                    config.K_pieces -= 1  
                    changed_list.append(((row-1,col),config.K))
                else:
                    changed_list.append(((row-1,col),config.W))
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
                    changed_list.append(((row+1,col),config.K))
            #elif isAtCorner((row+2,col),board):
            elif ((row+1,col) == (7,0) or (row+1,col) == (7,8)):
                if board[row+1][col] == config.K:
                    config.K_pieces -= 1
                    changed_list.append(((row+1,col),config.K))
                else:
                    changed_list.append(((row+1,col),config.W))      
                board[row+1][col] = 0
                config.zugRegel = 0
                config.W_pieces -= 1

            ############ neuer Edge Case
            elif (board[row+1][col] == config.W and ((row+2,col) == (4,4)) and board[row+2][col] == config.K ):
                #König umzingelt von Gegner (drunter, links und rechts) 
                if board[row+3][col] == config.B and board[row+2][col-1] == config.B and board[row+2][col+1] == config.B:
                    board[row+1][col] = 0
                    config.zugRegel = 0
                    config.W_pieces -= 1 
                    changed_list.append(((row+1,col),config.W)) 
            
            # Fall 4: Gegner (Weiß Bauer) ist eingeschlossen vom Gegner und Thron
            elif (row+1,col) == (3,4) and board[row+1][col] == config.W:
                board[row+1][col] = 0
                config.zugRegel = 0
                config.W_pieces -= 1
                changed_list.append(((row+1,col),config.W))

            elif (row+1 <= 7) and board[row+2][col] == config.B:
                if board[row+1][col] == config.K:
                    config.K_pieces -= 1
                    changed_list.append(((row+1,col),config.K))
                else:
                    changed_list.append(((row+1,col),config.W))  
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
                    changed_list.append(((row,col-1),config.K) )
            #elif isAtCorner((row,col-2),board):
            elif ((row,col-1) == (0,1) or (row,col-1) == (8,1)):
                if board[row][col-1] == config.K:
                    config.K_pieces -= 1    
                    changed_list.append(((row,col-1),config.K)) 
                else:
                    changed_list.append(((row,col-1),config.W))
                board[row][col-1] = 0
                config.zugRegel = 0
                config.W_pieces -= 1
            
            ############ neuer Edge Case
            elif (board[row][col-1] == config.W and ((row,col-2) == (4,4)) and board[row][col-2] == config.K ):
                #König umzingelt von Gegner (drüber, links und unten) 
                if board[row][col-3] == config.B and board[row+1][col-2] == config.B and board[row-1][col-2] == config.B:
                    board[row][col-1] = 0
                    config.zugRegel = 0
                    config.W_pieces -= 1 
                    changed_list.append(((row,col-1),config.W)) 
            # Fall 4: Gegner (Weiß Bauer) ist eingeschlossen vom Gegner und Thron
            elif (row,col-1) == (4,5) and board[row][col-1] == config.W:
                board[row][col-1] = 0
                config.zugRegel = 0
                config.W_pieces -= 1
                changed_list.append(((row,col-1),config.W))

            elif (col-1 >= 1) and board[row][col-2] == config.B :
                if board[row][col-1] == config.K:
                    config.K_pieces -= 1
                    changed_list.append(((row,col-1),config.K))
                else:
                    changed_list.append(((row,col-1),config.W))
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
                    changed_list.append(((row,col+1),config.K))
            #elif isAtCorner((row,col+2),board):
            elif ((row,col+1) == (0,7) or (row,col+1) == (8,7)):
                if board[row][col+1] == config.K:
                    config.K_pieces -= 1
                    changed_list.append(((row,col+1),config.K))
                else:
                    changed_list.append(((row,col+1),config.W))                      
                board[row][col+1] = 0
                config.zugRegel = 0
                config.W_pieces -= 1
            ############ neuer Edge Case
            elif (board[row][col+1] == config.W and ((row,col+2) == (4,4)) and board[row][col+2] == config.K ):
                #König umzingelt von Gegner (drüber, links und rechts) 
                if board[row][col+3] == config.B and board[row+1][col+2] == config.B and board[row-1][col+2] == config.B:
                    board[row][col+1] = 0 
                    config.zugRegel = 0
                    config.W_pieces -= 1 
                    changed_list.append(((row,col+1),config.W))
            # Fall 4: Gegner (Weiß Bauer) ist eingeschlossen vom Gegner und Thron
            elif (row,col+1) == (4,3) and board[row][col+1] == config.W:
                board[row][col+1] = 0
                config.zugRegel = 0
                config.W_pieces -= 1
                changed_list.append(((row,col+1),config.W))

            elif (col +1 <= 7) and board[row][col+2] == config.B:
                if board[row][col+1] == config.K:                    
                    config.K_pieces -= 1
                    changed_list.append(((row,col+1),config.K)) 
                else: 
                    changed_list.append(((row,col+1),config.W))
                board[row][col+1] = 0
                config.zugRegel = 0
                config.W_pieces -= 1

    
    # Spieler Weiß hat gezogen und greift an 
    elif board[row][col] in (config.W, config.K) : 
        # nach oben
        if row > 0 and (board[row-1][col] == config.B) :
            #if isAtCorner((row-2,col),board):
            if ((row-1,col) == (1,0) or (row-1,col) == (1,8)):
                changed_list.append((row-1,col))
                board[row-1][col] = 0
                config.zugRegel = 0
                config.B_pieces -= 1
            # eingeschlossen vom Gegner und Thron
            elif (row-1,col) == (5,4) and board[row-1][col] == config.B:
                changed_list.append((row-1,col))
                board[row-1][col] = 0
                config.zugRegel = 0
                config.B_pieces -= 1
            elif (row-1 >= 1) and board[row-2][col] in (config.W, config.K) :
                changed_list.append((row-1,col))
                board[row-1][col] = 0
                config.zugRegel = 0
                config.B_pieces -= 1
        
        # nach unten
        if row < 8 and (board[row+1][col] == config.B) :
            #if isAtCorner((row+2,col),board):
            if ((row+1,col) == (7,0) or (row+1,col) == (7,8)):   
                changed_list.append((row+1,col)) 
                board[row+1][col] = 0
                config.zugRegel = 0
                config.B_pieces -= 1
            elif (row+1,col) == (3,4) and board[row+1][col] == config.B:
                changed_list.append((row+1,col))
                board[row+1][col] = 0
                config.zugRegel = 0
                config.B_pieces -= 1
            elif (row+1 <= 7) and board[row+2][col] in (config.W, config.K):
                changed_list.append((row+1,col)) 
                board[row+1][col] = 0
                config.zugRegel = 0
                config.B_pieces -= 1
        
        # nach links
        if col > 0 and (board[row][col-1] == config.B):
            #if isAtCorner((row,col-2),board):
            if ((row,col-1) == (0,1) or (row,col-1) == (8,1)):
                
                changed_list.append((row,col-1)) 
                board[row][col-1] = 0
                config.zugRegel = 0
                config.B_pieces -= 1

            elif (row,col-1) == (4,5) and board[row][col-1] == config.B:
                changed_list.append((row,col-1))
                board[row][col-1] = 0
                config.zugRegel = 0
                config.B_pieces -= 1

            elif (col-1 >= 1) and board[row][col-2] in (config.W, config.K) :
                
                changed_list.append((row,col-1)) 
                board[row][col-1] = 0
                config.zugRegel = 0
                config.B_pieces -= 1

        # nach rechts
        if col < 8 and (board[row][col+1] == config.B):
            #if isAtCorner((row,col+2),board):
            if ((row,col+1) == (0,7) or (row,col+1) == (8,7)):    
                changed_list.append((row,col+1)) 
                board[row][col+1] = 0
                config.zugRegel = 0
                config.B_pieces -= 1

            elif (row,col+1) == (4,3) and board[row][col+1] == config.B:
                changed_list.append((row,col+1))
                board[row][col+1] = 0
                config.zugRegel = 0
                config.B_pieces -= 1    

            elif (col+1 <= 7) and board[row][col+2] in (config.W, config.K):
                changed_list.append((row,col+1)) 
                board[row][col+1] = 0
                config.zugRegel = 0
                config.B_pieces -= 1

    #gibt alle korridanten Zurück von Felder die man vom Gegener geschlagen hat (relevant für UndoMove)
    return changed_list

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



def isAtCorner(pos,board):
    """
    Prüft, ob eine Position „außerhalb“ des Boards oder auf einem Eckfeld liegt.
    Dient als Bedingung, um Gegnerfiguren am Rand oder außerhalb des Boards zu schlagen.

    Args:
        Pos: Tuple (row, col).

    Returns:
        bool: True, wenn die Position außerhalb oder auf einem Eckfeld ist.
    """
    row , col= pos

    return (row == 0) or (row == 8) or (col== 0) or (col == 8)
"""
    # Normale Eckfelder (0,0), (0,8), (8,0), (8,8)
    #TODO: prüfen ob man einfach hier config.Goal nutzen kann, sieht hier redundant aus 
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

    empty_Thron = board[4][4] == 0
 
    return at_corner or out_of_bounds or (next_to_Thron and empty_Thron)
"""

"""
expected2 = [
            [0, W, 0, 0, 0, 0, 0, W, 0],
            [W, B, 0, 0, 0, 0, 0, B, W],
            [B, 0, 0, 0, 0, 0, 0, 0, B],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [B, 0, 0, 0, 0, 0, 0, 0, W],
            [W, B, 0, 0, 0, 0, 0, W, B],
            [0, W, 0, 0, 0, 0, W, B, 0] 
        ]

expected = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, B],
    [0, 0, 0, 0, B, 0, 0, 0, 0],
    [B, 0, 0, 0, W, 0, 0, 0, 0],
    [B, 0, B, W, 0, W, B, 0, B],
    [B, 0, 0, 0, W, 0, 0, B, 0],
    [K, 0, 0, 0, B, 0, 0, 0, 0],
    [B, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, B, B, B, W, 0, 0]
]

b=attack(expected,(2,4))
b=attack(expected,(4,2))
b=attack(expected,(6,4))
b=attack(expected,(4,6))
print_board(b)



expected2 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, B],
    [0, 0, 0, 0, W, 0, 0, 0, 0],
    [B, 0, 0, 0, B, 0, 0, 0, 0],
    [B, 0, W, B, 0, B, W, 0, B],
    [B, 0, 0, 0, B, 0, 0, B, 0],
    [K, 0, 0, 0, W, 0, 0, 0, 0],
    [B, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, B, B, B, W, 0, 0]
]


c=attack(expected2,(2,4))
c=attack(expected2,(4,2))
c=attack(expected2,(6,4))
c=attack(expected2,(4,6))
print_board(c)


expected3 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, B],
    [0, 0, 0, 0, B, 0, 0, 0, 0],
    [B, 0, 0, 0, K, 0, 0, 0, 0],
    [B, 0, B, K, 0, K, B, 0, B],
    [B, 0, 0, 0, K, 0, 0, B, 0],
    [K, 0, 0, 0, B, 0, 0, 0, 0],
    [B, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, B, B, B, W, 0, 0]
]

d=attack(expected3,(2,4))
d=attack(expected3,(4,2))
d=attack(expected3,(6,4))
d=attack(expected3,(4,6))
print_board(d)

"""