
def get_all_pos(board, player):
    """
    Sucht auf dem gesamten Spielfeld nach allen Figuren eines Spielers.

    Die Funktion durchläuft das 9x9-Board und sammelt alle Positionen,
    auf denen eine Figur des angegebenen Spielers steht.

    Args:
        board: 2D-Liste, die das Spielfeld repräsentiert.
        player: Spielername, z.B. "White" oder "Black".

    Returns:
        Eine Liste von Tupeln der Form (row, col) mit allen Positionen
        der Figuren dieses Spielers.
    """

    all_positions = []
    
    for i in range(9):
        for j in range(9):
            if check_figure(player, board[i][j]):
                all_positions.append((i, j))
            
    return all_positions
                 
# Prüft ob die Figur den nächsten zuspielende Figur gehört             
def check_figure(player, figure): 

    """
    Prüft, ob eine Figur zu dem Spieler gehört, der gerade am Zug ist.

    In dieser Implementierung gehören zu:
    - "White": die Figuren W und K
    - sonst: die Figur B

    Args:
        player: Spielername, z.B. "White" oder "Black".
        figure: Wert auf einem Feld des Boards.

    Returns:
        True, wenn die Figur dem Spieler gehört, sonst False.
    """

    #global W_pieces, B_pieces

    if player == "White":
        if figure in ('W', 'K'):
            #W_pieces += 1
            return True
        return False
    else:
        if figure == 'B':
            #B_pieces += 1
            return True
        return False