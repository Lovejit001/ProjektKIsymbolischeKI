from src.gamelogic import checkBoard
from src.gamelogic import evaluateFunction
from src.gamelogic import makeMove
from src.gamelogic import config
from src.gamelogic import zugsortierung
from src.gamelogic.transpositionTable import trans_table
from src.gamelogic import saveBoardState
import math
import time
import copy


def alphaBetaMax(board, alpha, beta, depth, all_Moves, onTurn, root):
    """
    Alpha-Beta mit Transpositionstabelle für MAX-Spieler 
    """

    config.nodes += 1

    if (config.nodes % 1024 == 0): #Idee von der Stockfish Implementierung 
        if time.perf_counter() > config.stop_time: # Ist die Zeit überschritten soll hier abgebrochen werden
            raise TimeoutError
            


    # Prüfe Transpositionstabelle
    found, tt_score, tt_flag, tt_best_move = trans_table.lookup(
        board, depth, alpha, beta, onTurn
    )
    
    if found:
        # Wenn wir einen gespeicherten besten Zug haben und es die Wurzel ist
        if tt_best_move is not None and root:
            config.bestMove = tt_best_move
        return tt_score

    if depth == 0 or (checkBoard.checkBoard(board) != -2) or not all_Moves:
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
    
    # Prüfe Transpositionstabelle
    found, tt_score, tt_flag, tt_best_move = trans_table.lookup(
        board, depth, alpha, beta, onTurn
    )
    
    if found:
        return tt_score

    if depth == 0 or (checkBoard.checkBoard(board) != -2) or not all_Moves:
        score = evaluateFunction.eval(board, depth)
        trans_table.store(board, depth, score, 'exact', None, onTurn)
        return score

    minVal = math.inf
    best_move = None


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
    
    return result


def getBestMove2(board, onTurn, depth):
    score = 0
    if onTurn == "White":
        score = alphaBetaMax(
            board=board,
            alpha=-math.inf,
            beta=math.inf,
            depth=depth,
            all_Moves=makeMove.total_moves(board, onTurn),
            onTurn="White",
            root=True
        )
    else:
        score = alphaBetaMin(
            board=board,
            alpha=-math.inf,
            beta=math.inf,
            depth=depth,
            all_Moves=makeMove.total_moves(board, onTurn),
            onTurn="Black",
            root=True
        )
    return score

def iterative_deepening(board, onTurn, remaining_total_time, max_depth=4):
    board = copy.deepcopy(board)
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

    best_move = None
    best_depth = 0
    start_time = time.perf_counter()

    for depth in range(1, max_depth + 1):

        # Zeit prüfen BEVOR wir suchen
        elapsed = time.perf_counter() - start_time
        if elapsed >= remaining_time:

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
            break

        #führt AlphaBeta aus
        # Zeit prüfen NACHDEM wir gesucht haben
        elapsed = time.perf_counter() - start_time

        if elapsed < remaining_time:            
            best_move = config.bestMove
            best_depth = depth
        else:
            break        
    
    used_time = time.perf_counter() - x 
 
    return best_move, best_depth, used_time
