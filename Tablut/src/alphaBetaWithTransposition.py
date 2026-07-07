from src import checkBoard
from src import evaluateFunction
from src import makeMove
from src import config
from src import zugsortierung
from src.transpositionTable import trans_table
from src import saveBoardState
import math
import time


def alphaBetaMax(board, alpha, beta, depth, all_Moves, onTurn, root):
    """
    Alpha-Beta mit Transpositionstabelle für MAX-Spieler 
    """

    config.nodes += 1

    if (config.nodes % 1024 == 0): #Idee von der Stockfish Implementierung 
        if time.perf_counter() > config.stop_time: # Ist die ZUeit überschritten soll hier abgebrochen werden
            raise TimeoutError
            #return evaluateFunction.eval(board,depth)


    # Prüfe Transpositionstabelle
    found, tt_score, tt_flag, tt_best_move = trans_table.lookup(
        board, depth, alpha, beta, onTurn
    )
    
    if found:
        # Wenn wir einen gespeicherten besten Zug haben und es die Wurzel ist
        if tt_best_move is not None and root:
            config.bestMove = tt_best_move
        return tt_score

    if depth == 0 or (checkBoard.checkBoard2(board) != -2) or not all_Moves:
        score = evaluateFunction.eval(board, depth)
        # Speichere terminale Positionen
        trans_table.store(board, depth, score, 'exact', None, onTurn)
        return score

    maxVal = -math.inf
    best_move = None

    zugsortierung.zugsortierung(board,all_Moves)

    for startPos, allMoves in all_Moves.items():
        for goalPos in allMoves:
            
            
            saved_state = saveBoardState.save_global_state()
            changed_List = makeMove.updateBoard(board, (startPos, goalPos))

            score = alphaBetaMin(
                board, alpha, beta, depth - 1,
                makeMove.total_moves(board, switch(onTurn)),
                switch(onTurn), False
            )

            saveBoardState.undoMove(board,changed_List)
            saveBoardState.restore_global_state(saved_state)
            

            if score > maxVal:
                maxVal = score
                best_move = (startPos, goalPos)
                if root:
                    config.bestMove = best_move

            if score > alpha:
                alpha = score

            if score >= beta:
                # Beta-Cutoff - speichere als Lower Bound
                trans_table.store(board, depth, maxVal, 'lower', best_move, onTurn)
                return maxVal

    # Speichere exakten Wert
    flag = 'exact'
    trans_table.store(board, depth, maxVal, flag, best_move, onTurn)
    return maxVal


def alphaBetaMin(board, alpha, beta, depth, all_Moves, onTurn, root):
    """
    Alpha-Beta mit Transpositionstabelle für MIN-Spieler
    """

    config.nodes += 1

    if (config.nodes % 1024 == 0): #Idee von der Stockfish Implementierung 
        if time.perf_counter() > config.stop_time: # Ist die ZUeit überschritten soll hier abgebrochen werden
            raise TimeoutError
            #return evaluateFunction.eval(board,depth)
    
    # Prüfe Transpositionstabelle
    found, tt_score, tt_flag, tt_best_move = trans_table.lookup(
        board, depth, alpha, beta, onTurn
    )
    
    if found:
        return tt_score

    if depth == 0 or (checkBoard.checkBoard2(board) != -2) or not all_Moves:
        score = evaluateFunction.eval(board, depth)
        trans_table.store(board, depth, score, 'exact', None, onTurn)
        return score

    minVal = math.inf
    best_move = None

    #print(type(all_Moves))
    #print(f"THE MOVES: {all_Moves}")

    zugsortierung.zugsortierung(board,all_Moves)

    for startPos, allMoves in all_Moves.items():
        for goalPos in allMoves:
            
            
            saved_state = saveBoardState.save_global_state()
            changed_List = makeMove.updateBoard(board, (startPos, goalPos))

            score = alphaBetaMax(
                board, alpha, beta, depth - 1,
                makeMove.total_moves(board, switch(onTurn)),
                switch(onTurn), False
            )

            saveBoardState.undoMove(board,changed_List)
            saveBoardState.restore_global_state(saved_state)
            
            if score < minVal:
                minVal = score
                best_move = (startPos, goalPos)
                if root:
                    config.bestMove = best_move

            if score < beta:
                beta = score

            if score <= alpha:
                # Alpha-Cutoff - speichere als Upper Bound
                trans_table.store(board, depth, minVal, 'upper', best_move, onTurn)
                return minVal

    # Speichere exakten Wert
    trans_table.store(board, depth, minVal, 'exact', best_move, onTurn)
    return minVal


def switch(onTurn):
    if onTurn == "White":
        return "Black"
    else:
        return "White"


def getBestMove(board, onTurn, depth):
    """Einstiegspunkt für die Alpha-Beta-Suche"""
    # Transpositionstabelle für diese Suche zurücksetzen
    trans_table.clear()
    
    #print(f"Starte Alpha-Beta-Suche mit Tiefe {depth}")
    #print(f"Anzahl möglicher Züge: {debug.countMoves(makeMove.total_moves(board, onTurn))}")
    
    if onTurn == "White":
        result = alphaBetaMax(
            board=board,
            alpha=-math.inf,
            beta=math.inf,
            depth=depth,
            all_Moves=makeMove.total_moves(board, onTurn),
            onTurn="White",
            root=True
        )
    else:
        result = alphaBetaMin(
            board=board,
            alpha=-math.inf,
            beta=math.inf,
            depth=depth,
            all_Moves=makeMove.total_moves(board, onTurn),
            onTurn="Black",
            root=True
        )
    
    # Statistiken ausgeben
    stats = trans_table.get_stats()
    #print(f"Transposition Table Stats: {stats}")
    #print(f"Eval-Aufrufe insgesamt: {config.eval_counter}")
    
    return result


def iterative_deepening(board, onTurn, remaining_total_time, max_depth=4):
    x  = time.perf_counter()
    safety_buffer = 3 # 3 Sekunden

    usable_time = remaining_total_time - safety_buffer
    estimated_moves_left = 0
    phase_multiplier = 0

    pieces = config.B_pieces + config.W_pieces + config.K_pieces
    
    if pieces > 20 : 
        #Anfangszustände vom Board
        phase_multiplier = 0.7
        estimated_moves_left = 35
    elif pieces <= 20 and pieces >= 10 : 
        #Mitelspiel
        phase_multiplier = 1.25
        estimated_moves_left = 20
    else:
        #Endspiel
        phase_multiplier = 1.5
        estimated_moves_left = 10

    base_time =  usable_time / estimated_moves_left #sek

    remaining_time = base_time * phase_multiplier
    print(f"Zeit für Zug {remaining_time}")

    best_move = None
    best_depth = 0
    start_time = time.perf_counter()

    for depth in range(1, max_depth + 1):

        # Zeit prüfen BEVOR wir suchen
        elapsed = time.perf_counter() - start_time
        if elapsed >= remaining_time:
            print(f"Abbruch: verbrauchte ZEIT: {elapsed}")
            break

        config.init_pieces(board)
        #config.bestMove = None
        config.eval_counter = 0  # ← Zähler zurücksetzen

        #TODO gucken ob es Fehler gibt
        config.reset_time()
        config.search_start = time.perf_counter()
        config.stop_time = config.search_start + remaining_time

        try:
            getBestMove(board, onTurn, depth)
        except TimeoutError:
            print("Suche wegen Zeit beendet.")
            break

        #führt AlphaBeta aus
        # Zeit prüfen NACHDEM wir gesucht haben
        elapsed = time.perf_counter() - start_time

        if elapsed < remaining_time:
            print(f"ONTIME: verbrauchte ZEIT: {elapsed}")
            best_move = config.bestMove
            best_depth = depth
            print(f"BEST MOVE: {best_move} mit DEPTH : {best_depth}")
        else:
            break
        
    
    gesamtZeit = time.perf_counter() - x 
    print( f"GESAMTE ZEIT: {gesamtZeit} ") 
    if(best_move == None):        
        best_move = makeMove.randomMove(board,onTurn)        
    return best_move, best_depth


B = 'B'
W = 'W'
K = 'K'

alphaBeta_FinalMove = [
    [0, 0, B, 0, 0, 0, W, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, B, 0, 0, 0, W, 0, 0],
    [0, 0, 0, W, 0, 0, 0, 0, 0],
    [K, 0, 0, B, 0, 0, 0, 0, 0],
    [B, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, B, 0, B, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, W, 0, 0],
    [0, 0, 0, B, 0 ,0 ,0, 0, 0]
]

onTurn = 'White'

iterative_deepening(alphaBeta_FinalMove,onTurn,120)
print(config.bestMove)
print("ENDE TRANSPOSITON")