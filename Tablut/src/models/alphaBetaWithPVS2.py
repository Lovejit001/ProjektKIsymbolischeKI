from src import checkBoard
from src import evaluateFunction
from src import makeMove
from src import config
from src import debug
from src import zugsortierung
from src import saveBoardState
import copy, time, math


def alphaBetaMax(board, alpha, beta, depth, all_Moves, onTurn, root):

    if depth == 0 or (not checkBoard.checkBoard2(board)) or not all_Moves or config.timeout:
        return evaluateFunction.eval(board, depth)

    maxVal = -math.inf
    zugsortierung.zugsortierung(board, all_Moves)

    first_move = True

    for startPos, allMoves in all_Moves.items():
        for goalPos in allMoves:
     
            # --- Optional Time Check Block ---
            if config.timeout:
                return maxVal if maxVal != -math.inf else evaluateFunction.eval(board, depth)


            saved_state = saveBoardState.save_global_state()
            changed_List = makeMove.updateBoard(board, (startPos, goalPos))
            next_moves = makeMove.total_moves(board, switch(onTurn))

            if first_move:
                # 1. Full window search for the suspected PV-Node
                score = alphaBetaMin(board, alpha, beta, depth - 1, next_moves, switch(onTurn), False)
                first_move = False
            else:
                # 2. Null-window search to verify this move is worse than current alpha
                score = alphaBetaMin(board, alpha, alpha + 1, depth - 1, next_moves, switch(onTurn), False)
                
                # 3. If it fails high, we must re-search with the full window
                if alpha < score < beta:
                    score = alphaBetaMin(board, alpha, beta, depth - 1, next_moves, switch(onTurn), False)

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

    return maxVal


def alphaBetaMin(board, alpha, beta, depth, all_Moves, onTurn, root):

    if depth == 0 or (not checkBoard.checkBoard2(board)) or not all_Moves or config.timeout:
        return evaluateFunction.eval(board, depth)

    minVal = math.inf
    zugsortierung.zugsortierung(board, all_Moves)

    first_move = True

    for startPos, allMoves in all_Moves.items():
        for goalPos in allMoves:

            # --- Optional Time Check Block ---
            if config.timeout:
                return minVal if minVal != math.inf else evaluateFunction.eval(board, depth)


            saved_state = saveBoardState.save_global_state()
            changed_List = makeMove.updateBoard(board, (startPos, goalPos))
            next_moves = makeMove.total_moves(board, switch(onTurn))


            if first_move:
                # 1. Full window search for the suspected PV-Node
                score = alphaBetaMax(board, alpha, beta, depth - 1, next_moves, switch(onTurn), False)
                first_move = False
            else:
                # 2. Null-window search to verify this move is worse than current beta
                score = alphaBetaMax(board, beta - 1, beta, depth - 1, next_moves, switch(onTurn), False)
                
                # 3. If it fails low, we must re-search with the full window
                if alpha < score < beta:
                    score = alphaBetaMax(board, alpha, beta, depth - 1, next_moves, switch(onTurn), False)

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

    return minVal


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
    #print(f"Zeit für Zug {remaining_time}")

    best_move = None
    best_depth = 0
    start_time = time.perf_counter()

    for depth in range(1, max_depth + 1):

        # Zeit prüfen BEVOR wir suchen
        elapsed = time.perf_counter() - start_time
        if elapsed >= remaining_time:
            #print(f"Abbruch: verbrauchte ZEIT: {elapsed}")
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
            #print("Suche wegen Zeit beendet.")
            break

        #führt AlphaBeta aus
        # Zeit prüfen NACHDEM wir gesucht haben
        elapsed = time.perf_counter() - start_time

        if elapsed < remaining_time:
            #print(f"ONTIME: verbrauchte ZEIT: {elapsed}")
            best_move = config.bestMove
            best_depth = depth
            #print(f"BEST MOVE: {best_move} mit DEPTH : {best_depth}")
        else:
            break
        
        
    
    used_time = time.perf_counter() - x 
    #print( f"GESAMTE ZEIT: {used_time} ") 
    #Idee War wenn Zeit vorbei ist soll man einen random move geben aber macht wenig Sinn weil so dann auch bei 0 Sekunden ein Move gegeben wird
    #if(best_move == None):        
    #    best_move = makeMove.randomMove(board,onTurn)        
    return best_move, best_depth, used_time


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

bestMove, _ , _  =iterative_deepening(alphaBeta_FinalMove,onTurn,120)
print(bestMove)
