from src import checkBoard
from src import evaluateFunction
from src import makeMove
from src import config
from src import debug
from src import zugsortierung
from src.transpositionTable import trans_table
#from src import transpositionTable_array
#trans_table = transpositionTable_array.ArrayTranspositionTable(size_mb=128)
from src import saveBoardState
import math
import copy


def alphaBetaMax(board, alpha, beta, depth, all_Moves, onTurn, root):
    """
    Alpha-Beta mit Transpositionstabelle für MAX-Spieler (Schwarz)
    """
    
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
    Alpha-Beta mit Transpositionstabelle für MIN-Spieler (Weiß)
    """
    
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

