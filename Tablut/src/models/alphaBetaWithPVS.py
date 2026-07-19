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
    + Principal Variation Search (PVS)
    """

    config.nodes += 1
    config.eval_counter += 1  # <-- JEDEN Knoten zählen


    if (config.nodes % 1024 == 0):
        if time.perf_counter() > config.stop_time:
            raise TimeoutError

    # Prüfe Transpositionstabelle
    found, tt_score, tt_flag, tt_best_move = trans_table.lookup(
        board, depth, alpha, beta, onTurn
    )

    if found:
        if tt_best_move is not None and root:
            config.bestMove = tt_best_move
        return tt_score

    if depth == 0 or (checkBoard.checkBoard(board) != -2) or not all_Moves:
        score = evaluateFunction.eval(board, depth)
        trans_table.store(board, depth, score, 'exact', None, onTurn)
        return score

    alpha_original = alpha   
    maxVal = -math.inf
    best_move = None

    zugsortierung.zugsortierung(board, all_Moves)

    first_move = True   

    for startPos, allMoves in all_Moves.items():
        for goalPos in allMoves:

            saved_state = saveBoardState.save_global_state()
            changed_List = makeMove.updateBoard(board, (startPos, goalPos))

            if first_move:   
                score = alphaBetaMin(
                    board, alpha, beta, depth - 1,
                    makeMove.total_moves(board, switch(onTurn)),
                    switch(onTurn), False
                )
                first_move = False
            else:
                # Nullfenster-Suche / Scout Search   # <<< PVS CHANGED
                score = alphaBetaMin(
                    board, alpha, alpha + 1, depth - 1,
                    makeMove.total_moves(board, switch(onTurn)),
                    switch(onTurn), False
                )

                # Falls der Zug alpha verbessert, aber noch kein Cutoff auslöst:
                # Re-Search mit vollem Fenster   # <<< PVS CHANGED
                if score > alpha and score < beta:
                    score = alphaBetaMin(
                        board, alpha, beta, depth - 1,
                        makeMove.total_moves(board, switch(onTurn)),
                        switch(onTurn), False
                    )

            saveBoardState.undoMove(board, changed_List)
            saveBoardState.restore_global_state(saved_state)

            if score > maxVal:
                maxVal = score
                best_move = (startPos, goalPos)
                if root:
                    config.bestMove = best_move

            if score > alpha:
                alpha = score

            if alpha >= beta:
                trans_table.store(board, depth, maxVal, 'lower', best_move, onTurn)
                return maxVal


    if maxVal <= alpha_original:
        flag = 'upper'
    elif maxVal >= beta:
        flag = 'lower'
    else:
        flag = 'exact'

    trans_table.store(board, depth, maxVal, flag, best_move, onTurn)
    return maxVal

def alphaBetaMin(board, alpha, beta, depth, all_Moves, onTurn, root):
    """
    Alpha-Beta mit Transpositionstabelle für MIN-Spieler
    + Principal Variation Search (PVS)
    """

    config.nodes += 1
    config.eval_counter += 1  


    if (config.nodes % 1024 == 0):
        if time.perf_counter() > config.stop_time:
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

    beta_original = beta   # <<< PVS CHANGED
    minVal = math.inf
    best_move = None

    zugsortierung.zugsortierung(board, all_Moves)

    first_move = True   

    for startPos, allMoves in all_Moves.items():
        for goalPos in allMoves:

            saved_state = saveBoardState.save_global_state()
            changed_List = makeMove.updateBoard(board, (startPos, goalPos))

            if first_move:   # <<< PVS CHANGED
                score = alphaBetaMax(
                    board, alpha, beta, depth - 1,
                    makeMove.total_moves(board, switch(onTurn)),
                    switch(onTurn), False
                )
                first_move = False
            else:
                # Nullfenster-Suche 
                score = alphaBetaMax(
                    board, beta - 1, beta, depth - 1,
                    makeMove.total_moves(board, switch(onTurn)),
                    switch(onTurn), False
                )

                # Falls der Zug beta senkt, aber noch kein Cutoff auslöst:
                # Re-Search mit vollem Fenster   
                if score < beta and score > alpha:
                    score = alphaBetaMax(
                        board, alpha, beta, depth - 1,
                        makeMove.total_moves(board, switch(onTurn)),
                        switch(onTurn), False
                    )

            saveBoardState.undoMove(board, changed_List)
            saveBoardState.restore_global_state(saved_state)

            if score < minVal:
                minVal = score
                best_move = (startPos, goalPos)
                if root:
                    config.bestMove = best_move

            if score < beta:
                beta = score

            if alpha >= beta:
                trans_table.store(board, depth, minVal, 'upper', best_move, onTurn)
                return minVal

    # TT-Flag sauber setzen   
    if minVal >= beta_original:
        flag = 'lower'
    elif minVal <= alpha:
        flag = 'upper'
    else:
        flag = 'exact'

    trans_table.store(board, depth, minVal, flag, best_move, onTurn)
    return minVal

def switch(onTurn):
    if onTurn == "White":
        return "Black"
    else:
        return "White"

def getBestMove(board, onTurn, depth):
    """Einstiegspunkt für die Alpha-Beta-Suche"""
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
    x = time.perf_counter()
    safety_buffer = 3

    usable_time = remaining_total_time - safety_buffer
    estimated_moves_left = 0
    phase_multiplier = 0

    pieces = config.B_pieces + config.W_pieces + config.K_pieces

    if pieces > 20:
        phase_multiplier = 0.7
        estimated_moves_left = 35
    elif pieces <= 20 and pieces >= 10:
        phase_multiplier = 1.25
        estimated_moves_left = 20
    else:
        phase_multiplier = 1.5
        estimated_moves_left = 10

    base_time = usable_time / estimated_moves_left
    remaining_time = base_time * phase_multiplier

    best_move = None
    best_depth = 0
    start_time = time.perf_counter()

    for depth in range(1, max_depth + 1):

        elapsed = time.perf_counter() - start_time
        if elapsed >= remaining_time:
            break

        config.init_pieces(board)
        config.eval_counter = 0

        config.reset_time()
        config.search_start = time.perf_counter()
        config.stop_time = config.search_start + remaining_time

        try:
            getBestMove(board, onTurn, depth)
        except TimeoutError:

            break

        elapsed = time.perf_counter() - start_time

        if elapsed < remaining_time:
            best_move = config.bestMove
            best_depth = depth
        else:
            break

    used_time = time.perf_counter() - x
    
    return best_move, best_depth, used_time
