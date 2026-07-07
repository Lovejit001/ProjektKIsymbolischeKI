from src import checkBoard
from src import evaluateFunction
from src import makeMove
from src import config
from src import debug
from src import saveBoardState
from src import zugsortierung
import math
import time
import copy


def alphaBetaMax(board, alpha, beta, depth, all_Moves, onTurn, root):

    config.nodes += 1

    if (config.nodes % 1024 == 0): #Idee von der Stockfish Implementierung 
        if time.perf_counter() > config.stop_time: # Ist die ZUeit überschritten soll hier abgebrochen werden
            raise TimeoutError
            #return evaluateFunction.eval(board,depth)

    if depth == 0 or (checkBoard.checkBoard2(board) != -2) or not all_Moves:
        score = evaluateFunction.eval(board,depth)
        return evaluateFunction.eval(board,depth)

    maxVal = -math.inf
    #HIER MUSS ALLPHA BETA 
    zugsortierung.zugsortierung(board,all_Moves)

    for startPos, allMoves in all_Moves.items():
        #print(f"{all_Moves}")

        for goalPos in allMoves:

            
            saved_state = saveBoardState.save_global_state()
            changed_List = makeMove.updateBoard(board, (startPos, goalPos))
            
            row,col = startPos
            

            score = alphaBetaMin(
                board, alpha, beta, depth - 1,
                makeMove.total_moves(board, switch(onTurn)),
                switch(onTurn), False
            )
            
            saveBoardState.undoMove(board,changed_List)
            saveBoardState.restore_global_state(saved_state)

            if score > maxVal:
                maxVal = score
                if root:
                    config.bestMove = (startPos, goalPos)

            if score > alpha:
                alpha = score

            if score >= beta:
                return maxVal  # Beta-Cutoff        

    return maxVal  # ← NACH der Schleife


def alphaBetaMin(board, alpha, beta, depth, all_Moves, onTurn, root):

    config.nodes += 1

    if (config.nodes % 1024 == 0): #Idee von der Stockfish Implementierung 
        if time.perf_counter() > config.stop_time: # Ist die ZUeit überschritten soll hier abgebrochen werden
            raise TimeoutError
            #return evaluateFunction.eval(board,depth)

    if depth == 0 or (checkBoard.checkBoard2(board) != -2) or not all_Moves:
        score = evaluateFunction.eval(board,depth)
        return evaluateFunction.eval(board,depth)

    minVal = math.inf

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
                if root:
                    config.bestMove = (startPos, goalPos)

            if score < beta:
                beta = score

            if score <= alpha:
                return minVal  # Alpha-Cutoff
            

    return minVal  # ← NACH der Schleife


def switch(onTurn):
    if onTurn == "White":
        return "Black"
    else:
        return "White"


def getBestMove(board, onTurn, depth):
    
    if onTurn == "White":
        alphaBetaMax(
            board=board,
            alpha=-math.inf,
            beta=math.inf,
            depth=depth,
            all_Moves=makeMove.total_moves(board, onTurn),
            onTurn="White",
            root=True
        )
    else:
        alphaBetaMin(
            board=board,
            alpha=-math.inf,
            beta=math.inf,
            depth=depth,
            all_Moves=makeMove.total_moves(board, onTurn),
            onTurn="Black",
            root=True
        )


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
all_Moves=makeMove.randomMove(alphaBeta_FinalMove, onTurn)


bestMOve, _  =iterative_deepening(alphaBeta_FinalMove,onTurn,0.002)
print(bestMOve)

#makeMove.updateBoard(alphaBeta_FinalMove, ((3,2),(3,0)) )
#debug.print_board(alphaBeta_FinalMove)

#print("HEYYY")
#print(config.bestMove)
#alphaBetaMin(alphaBeta_FinalMove, -math.inf, math.inf, 2, makeMove.total_moves(alphaBeta_FinalMove, "Black"), "Black", True)
#print(config.bestMove)
#print("HEYYY")