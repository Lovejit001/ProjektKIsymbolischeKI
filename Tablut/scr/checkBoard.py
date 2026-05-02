from scr import config

## Hier wird überprüft ob der König sich nicht mehr auf dem Board befindet => Der König wurde geschlagen
## + ob der König sich auf den Eckfeldern befindet => Weiß gewinnt
## + ob keine Gegnerischen Schwarzen Figuren mehr vorhanden sind => Weiß gewinnt
## - ob nach 50 Züge keine Spielfigur geschlagen wird => Remis
## - ob eine 3-fache Stellungswiederholung auftritt => Remis

def checkBoard2(board):

    # Prüfung ob es noch Spielfiguren auf dem Spielfeld vorhanden sind
    if config.B_pieces == 0 and config.W_pieces == 0:
        print(f"ERROR! Es sind keine (weiteren) Spielfiguren auf dem Spielfeld vorhanden.")
        return False
    # Prüfung ob mehrere Könige auf dem Spielfeld vorhanden sind
    elif config.K_pieces > 1:
        print(f"ERROR! Es sind mehr als ein König auf dem Spielfeld vorhanden.")
        return False
    # Prüfung ob ein König auf dem Spielfeld vorhanden ist
    elif config.K_pieces < 1:
        print(f"Winner: Black")
        return False
    # Prüfung ob König sich auf den Eckfeldern befindet
    elif board[0][0] == config.K or board[0][8] == config.K or board[8][0] == config.K or board[8][8] == config.K:
        print(f"Winner: White")
        return False
    # Prüfung ob es noch schwarze Spielfiguren auf dem Spielfeld vorhanden sind
    elif config.B_pieces == 0:
        print(f"Winner: White")
        return False
    # Prüfung ob es noch weiße Spielfiguren auf dem Spielfeld vorhanden sind
    elif config.W_pieces == 0:
        print(f"Winner: Black")
        return False
    # Prüfung ob nach 50 Zügen eine Spielfigur geschlagen wurde
    elif config.zugRegel == 50:
        print(f"REMIS! Nach 50 Zügen wurde kein einziges Spielfigur geschlagen.")
        return False
    # Prüfung ob drei Stellungswiderholungen vorkommen
    elif recent_moves(board):
        print(f"REMIS! 3-fache Stellungswiderholung.")
        return False

    return True


def recent_moves(board):
    #if len(config.whiteStellung) == 5 or len(config.blackStellung) == 5:
    #    if config.whiteStellung[0] == config.whiteStellung[2] and config.whiteStellung[0] == config.whiteStellung[4]:
    #        return True
    #    else:
    #        config.whiteStellung.pop(0)
    #    if config.blackStellung[0] == config.blackStellung[2] and config.blackStellung[0] == config.blackStellung[4]:
    #        return True
    #    else:
    #        config.blackStellung.pop(0)

    curr = getHash(board)

    count = 0

    for past in config.boardHash:
        if past == curr:
            count += 1
    #print(config.boardHash)
    print(f"Stellung kommt {count}-mal vor.")
    return count >= 3


# Soll ein Hash erstellen für die dreifache Stellungswiederholung

def getHash(board):
    return tuple(tuple(row) for row in board)