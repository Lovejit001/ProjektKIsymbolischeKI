from src.gamelogic import config

def save_global_state():
    return {
        'B_pieces': config.B_pieces,
        'W_pieces': config.W_pieces,
        'K_pieces': config.K_pieces,
        'zugCounter': config.zugCounter,
        'zugRegel': config.zugRegel,
        'boardHash': config.boardHash.copy() if config.boardHash else [],
        'onTurn': config.onTurn
    }


def restore_global_state(saved_state):
    config.B_pieces = saved_state['B_pieces']
    config.W_pieces = saved_state['W_pieces']
    config.K_pieces = saved_state['K_pieces']
    config.zugCounter = saved_state['zugCounter']
    config.zugRegel = saved_state['zugRegel']
    config.boardHash = saved_state['boardHash'].copy() if saved_state['boardHash'] else []
    config.onTurn = saved_state['onTurn']

#changed_List = [ ((...),...), ((...),...), ((...),...), ...  ]
def undoMove(board,changed_list):
    #der Schritt den der Spieler macht wird zurückgesetzt

    figure = changed_list[0]
    bestmove = changed_list[1]
    move_track = changed_list[2]

    (oldPos, newPos) = bestmove

    newRow,newCol = newPos
    oldRow,oldCol = oldPos

    board[newRow][newCol]= 0
    board[oldRow][oldCol]= figure

    #Einfügen aller gekillten Figuren
    if (figure == config.K) or figure == config.W:
        for (row,col) in move_track:
            board[row][col] = config.B

    else:
        for ((row,col),fig) in move_track:
            board[row][col] = fig


