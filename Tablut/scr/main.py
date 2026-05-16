from scr import config
from scr import checkBoard 
from scr import makeMove 
from scr import attack
from scr import debug
from scr import alphaBeta

import math, copy, time


def main():

    config.game_start_time = time.time()
    config.game_max_duration = 30  #30 sekunden als Beispiel
    #config.game_max_duration = 1
    config.timeout = False

    W = config.W
    B = config.B
    K = config.K
    #global W_pieces, B_pieces
    
    starting_board = [
    [0, 0, 0, B, B, B, 0, 0, 0],
    [0, 0, 0, 0, B, 0, 0, 0, 0],
    [0, 0, 0, 0, W, 0, 0, 0, 0],
    [B, 0, 0, 0, W, 0, 0, 0, B],
    [B, B, W, W, K, W, W, B, B],
    [B, 0, 0, 0, W, 0, 0, 0, B],
    [0, 0, 0, 0, W, 0, 0, 0, 0],
    [0, 0, 0, 0, B, 0, 0, 0, 0],
    [0, 0, 0, B, B, B, 0, 0, 0]
    ]
    
    test_noBlack = [
        [0, 0, 0, 0, 0, 0, W, 0, 0],
        [0, 0, 0, 0, 0, 0, W, 0, 0],
        [0, 0, 0, 0, 0, 0, W, 0, 0],
        [0, 0, 0, W, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, W, 0, 0, W, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    test2 = [
        [0, 0, 0, 0, 0, B, W, 0, 0],
        [0, 0, 0, 0, B, 0, 0, 0, 0],
        [0, B, B, B, B, 0, W, 0, 0],
        [0, 0, W, 0, 0, B, 0, 0, 0],
        [0, 0, B, 0, K, 0, W, 0, 0],
        [0, B, B, 0, B, B, 0, 0, 0],
        [0, 0, B, W, B, B, 0, 0, 0],
        [0, B, 0, B, 0, B, 0, 0, B],
        [0, 0, 0, 0, B, 0, 0, 0, 0]
    ]
    test3 = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, B, 0, 0, 0, 0],
        [0, 0, 0, B, 0, B, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, B, 0],
        [0, 0, B, 0, B, 0, 0, B, 0],
        [K, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    remis50zug = [
        [0, B, B, B, B, B, B, B, 0],
        [B, B, B, B, B, B, B, B, B],
        [B, B, B, B, B, B, B, B, B],
        [B, B, B, B, B, B, B, B, B],
        [B, B, B, B, 0, B, B, 0, B],
        [W, W, W, W, W, W, 0,  K, W],
        [W, W, W, W, W, W, W, W, W],
        [W, W, W, W, W, W, W, W, W],
        [0, W, W, W, W, W, W, W, 0]
    ]
    remis3Stellung = [
        [0, W, W, W, W, W, W, W, 0],
        [W, B, 0, W, W, W, W, W, W],
        [W, W, W, W, W, W, W, W, W],
        [W, W, W, W, W, W, W, W, W],
        [W, W, W, W, 0, W, W, W, W],
        [W, W, W, W, W, W, W, K, W],
        [W, W, W, W, W, W, W, W, W],
        [W, W, W, W, W, W, W, W, W],
        [0, W, W, W, W, W, W, W, 0]
    ]

    alphaBetaBoard= [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, B, 0, 0, 0, 0, 0],
    [0, 0, K, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, B, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0] 
    ]

    #debug.print_board(test_noBlack)
    #print_board(test2)
    #print_board(test3)
    #print_board(remis50zug)
    #print_board(remis3Stellung)
    print("Game Starts!")
    print(f"Maximale Spielzeit: {config.game_max_duration} Sekunden")
    config.onTurn = "White"
    #config.onTurn = "Black"
    #result = "Remis"

    #board = test_noBlack
    #board = alphaBetaBoard
    #board = test2
    #board = remis50zug
    #board = remis3Stellung
    board = starting_board

    depth = 3

    # kann weg wenn in config das Startboard Anzahl angegeben wird
    for i in range(9):
        for j in range(9):
            if board[i][j] == 'W':
                config.W_pieces += 1
            elif board[i][j] == 'K':
                config.K_pieces += 1
                config.W_pieces += 1
            elif board[i][j] == 'B':
                config.B_pieces += 1

    #print(f"Weiße Figuren auf dem Brett: {config.W_pieces}, Schwarze Figuren auf dem Brett: {config.B_pieces}")

    if config.K_pieces < 1:
        print(f"ERROR! Es ist kein König auf dem Spielfeld vorhanden")
        return

    while checkBoard.checkBoard2(board) and not config.timeout:
    #i = 0
    #while i < 2:
        #print(f"Der Beste Zug: {config.bestMove}. (Sollte None zum Anfang)")
        
        #debug.print_board(board)

        elapsed_time = time.time() - config.game_start_time
        
        if elapsed_time >= config.game_max_duration:
            print(f"\n=== SPIELZEIT ABGELAUFEN! ({elapsed_time:.1f} Sekunden) ===")
            print("Spiel endet mit aktuellem Stand")
            break
            
        print(f"\n--- Zug {config.zugCounter} (Verstrichene Zeit: {elapsed_time:.1f}/{config.game_max_duration}s) ---")
        print(f"Spieler: {config.onTurn}")        

        oldBoard = copy.deepcopy(board)
        
        print("ALPHA BETA BEGINNT")

        move_start = time.time()
        ## Hier kommt das andere
        config.bestMove = alphaBeta.alphaBetaTime(board, depth, config.onTurn)

        move_duration = time.time() - move_start

        if config.bestMove is None:
            print("Kein gültiger Zug gefunden!")
            break

        if config.timeout:
            print("ZEIT IST ABGELAUFEN! Spiel wurde beendet.")
            print(f"Der Beste Move für den Spieler {config.onTurn} welches ermittelt wurde: {config.bestMove}")
            break

        print(f"ALPHA BETA ZUENDE (Zug dauerte: {move_duration:.3f} Sekunden)")

        #print("ALPHA BETA ZUENDE")
        board = makeMove.updateBoard(board, config.bestMove)
        print(f"Der beste Move welches nun durchgeführt wird: {config.bestMove}")
        
        debug.print_board(board)

        print(f"Weiße Figuren auf dem Brett: {config.W_pieces}, Schwarze Figuren auf dem Brett: {config.B_pieces}")
        print(f"Insgesamt Züge: {config.zugCounter}, 50-Züge-Regel: {config.zugRegel}")

        if config.onTurn == "White":
            config.onTurn = "Black"
        else:
            config.onTurn = "White"
        
        if oldBoard == board:
            print(f"ERROR! Es wurde kein Zug getätigt.")
            break

        i += 1
    
    print("\n=== SPIEL ENDE ===")
    if config.timeout:
        print("Grund: Zeitlimit überschritten")  
    
    print(f"Benötigte Zeit gesamt: {time.time() - config.game_start_time}")

    return
        
if __name__ == "__main__" :
    main()

