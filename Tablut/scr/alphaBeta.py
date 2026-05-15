from scr import checkBoard
from scr import evaluateFunction
from scr import makeMove
from scr import config
from scr import debug
import math, copy

def alphaBetaMax(board,alpha,beta,depth,all_Moves,onTurn,root):
        
    maxVal = -math.inf
    if depth == 0 or (not checkBoard.checkBoard2(board)) or not all_Moves:
        return evaluateFunction.eval_func(board, onTurn)

    i = 1
    
    if not all_Moves:
        return evaluateFunction.eval_func(board, onTurn)
    
    for startPos,allMoves in all_Moves.items(): 
        print(f"all possible Moves: {allMoves}")
        for goalPos in allMoves:

            #Macht den Zug
            print(f"{i}-te Iteration !")
            print(f"START- ZielPosition: {startPos} -> {goalPos}")
            
            saved_state = save_global_state()
            copyboard = copy.deepcopy(board)
            newBoard = makeMove.updateBoard(copyboard,(startPos,goalPos))
            debug.print_board(newBoard)

            score = alphaBetaMin(newBoard,alpha,beta,depth-1, makeMove.total_moves(newBoard,switch(onTurn)),(switch(onTurn)),False)
            
            #undoMoveWithState(board,startPos,goalPos,saved_state)
            restore_global_state(saved_state)
            
            print(f"{i}-te Iteration ! Der Score: {score}")
            
            i += 1
            if score > maxVal: 
                print(root)
                if root == True : 
                    config.bestMove = (startPos,goalPos)
                maxVal = score
                print(f"BEST MOVE: {config.bestMove}")
            if score > alpha:
                alpha = score
            if score >= beta:
                return score
    
    return maxVal


def alphaBetaMin(board, alpha,beta,depth,all_Moves,onTurn,root):
    print("MIN IST DRANNN")
    minVal = math.inf

    if depth == 0 or (not checkBoard.checkBoard2(board)) or not all_Moves:
        print("EVAL WIRD AUSGERUFEN !!!")
        return evaluateFunction.eval_func(board, onTurn)
    
    if not all_Moves:
        print("EVAL WIRD AUSGERUFEN ABER KEINE MOVES VORHANDEN!")
        return evaluateFunction.eval_func(board, onTurn)
    
    i = 1
    
    for startPos,allMoves in all_Moves.items():
        print(f"all possible Moves: {allMoves}") 
        for goalPos in allMoves:

            print(f"START- ZielPosition: {startPos} -> {goalPos}")  

            saved_state = save_global_state()
            copyboard = copy.deepcopy(board)
            newBoard= makeMove.updateBoard(copyboard,(startPos,goalPos))                                        
            score = alphaBetaMax(newBoard,alpha,beta,depth-1, makeMove.total_moves(newBoard,switch(onTurn)),switch(onTurn),False)
            
            #undoMoveWithState(board,startPos,goalPos,saved_state)
            restore_global_state(saved_state)

            print(f"{i}-te Iteration ! Der Score: {score}")

            i += 1

            if score < minVal:
                if root : 
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



