from scr import checkBoard
from scr import evaluateFunction
from scr import makeMove
from scr import config
from scr import debug
import math, copy, time

def alphaBetaTime(board, depth, onTurn):

    if config.timeout:
        return None
    
    all_moves = makeMove.total_moves(board, onTurn)

    config.move_start_time = time.time()
    remaining_game_time = config.game_max_duration - (time.time() - config.game_start_time)
    #move_time_limit = min(0.5, max(0.1, remaining_game_time)) # Maximale Zeit für einen Zug (kann auch weggelassen werden)
    move_time_limit = remaining_game_time
    config.move_end_time = config.move_start_time + move_time_limit
    
    print(f"  -> Zug-Zeitlimit: {move_time_limit:.2f}s (Verbleibende Spielzeit: {remaining_game_time:.1f}s)")

    if config.onTurn == "White":
        alphaBetaMax(board=board,alpha=-math.inf,beta=math.inf,depth=depth,all_Moves=all_moves,onTurn=config.onTurn,root=True)
    else:
        alphaBetaMin(board=board,alpha=-math.inf,beta=math.inf,depth=depth,all_Moves=all_moves,onTurn=config.onTurn,root=True)
    
    return config.bestMove
        

def alphaBetaMax(board,alpha,beta,depth,all_Moves,onTurn,root):
        
    maxVal = -math.inf

    if depth == 0 or (not checkBoard.checkBoard2(board)) or config.timeout:
        return evaluateFunction.eval_func(board, onTurn)

    i = 1
    
    if not all_Moves:
        return evaluateFunction.eval_func(board, onTurn)
    
    for startPos,allMoves in all_Moves.items(): 
        #print(f"all possible Moves: {allMoves}")
        for goalPos in allMoves:

            if time.time() >= config.move_end_time:
                config.timeout = True
                print(f"  -> Timeout in alphaBetaMax bei Tiefe {depth}")
                if maxVal != -math.inf:
                    return maxVal
                else:
                    evaluateFunction.eval_func(board, onTurn)

            #Macht den Zug
            #print(f"{i}-te Iteration !")
            #print(f"START- ZielPosition: {startPos} -> {goalPos}")
            
            saved_state = save_global_state()
            copyboard = copy.deepcopy(board)
            newBoard = makeMove.updateBoard(copyboard,(startPos,goalPos))
            #debug.print_board(newBoard)

            score = alphaBetaMin(newBoard,alpha,beta,depth-1, makeMove.total_moves(newBoard,switch(onTurn)),(switch(onTurn)),False)
            
            #undoMoveWithState(board,startPos,goalPos,saved_state)
            restore_global_state(saved_state)
            
            #print(f"{i}-te Iteration ! Der Score: {score}")
            
            i += 1
            if score > maxVal: 
                #print(root)
                if root: 
                    config.bestMove = (startPos,goalPos)
                    #print(f"BEST MOVE FÜR WEIß: {config.bestMove}")
                maxVal = score

            if score > alpha:
                alpha = score
            if score >= beta:
                return score
    
    return maxVal


def alphaBetaMin(board, alpha,beta,depth,all_Moves,onTurn,root):
    #print("MIN IST DRANNN")
    minVal = math.inf

    if depth == 0 or (not checkBoard.checkBoard2(board)) or config.timeout:
        #print("EVAL WIRD AUSGERUFEN !!!")
        return evaluateFunction.eval_func(board, onTurn)
    
    if not all_Moves:
        #print("EVAL WIRD AUSGERUFEN ABER KEINE MOVES VORHANDEN!")
        return evaluateFunction.eval_func(board, onTurn)
    
    i = 1
    
    for startPos,allMoves in all_Moves.items():
        #print(f"all possible Moves: {allMoves}") 
        for goalPos in allMoves:
            
            if time.time() >= config.move_end_time:
                config.timeout = True
                print(f"  -> Timeout in alphaBetaMin bei Tiefe {depth}")
                if minVal != math.inf:
                    return minVal
                else:
                    evaluateFunction.eval_func(board, onTurn)

            #print(f"START- ZielPosition: {startPos} -> {goalPos}")  

            saved_state = save_global_state()
            copyboard = copy.deepcopy(board)
            newBoard= makeMove.updateBoard(copyboard,(startPos,goalPos))                                        
            score = alphaBetaMax(newBoard,alpha,beta,depth-1, makeMove.total_moves(newBoard,switch(onTurn)),switch(onTurn),False)
            
            
            restore_global_state(saved_state)

            #print(f"{i}-te Iteration ! Der Score: {score}")

            i += 1

            if score < minVal:
                if root: 
                    config.bestMove = (startPos,goalPos)
                minVal = score
            if score < beta:
                beta = score
            if score <= alpha:
                return score
            
    
    return minVal


#SOLLTE MAN HIER LIEBER CONFIG ÄNDERN ODER LIEBER NICHT ?
def switch(onTurn): 
    if onTurn == "White":
        return "Black"
    else: 
        return "White"


def save_global_state():
    """Speichert alle relevanten globalen Variablen."""
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
    """Stellt die globalen Variablen aus einem gespeicherten Zustand wieder her."""
    config.B_pieces = saved_state['B_pieces']
    config.W_pieces = saved_state['W_pieces']
    config.K_pieces = saved_state['K_pieces']
    config.zugCounter = saved_state['zugCounter']
    config.zugRegel = saved_state['zugRegel']
    config.boardHash = saved_state['boardHash'].copy() if saved_state['boardHash'] else [] #HIER UNSICHER LOVEJIT WEIß WAS boardHASH macht
    config.onTurn = saved_state['onTurn']



