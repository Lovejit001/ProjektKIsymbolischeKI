from scr import checkBoard
from scr import evaluateFunction
from scr import makeMove
from scr import config
from scr import debug
import math
import copy


def alphaBetaMax(board, alpha, beta, depth, all_Moves, onTurn, root, i):

    if depth == 0 or (not checkBoard.checkBoard2(board)) or not all_Moves:
        score = evaluateFunction.eval(board)
        print(f"WHITE reached child Note {i}-te Iteration: onTrun = {onTurn} depth={ depth} isGameOver= {not checkBoard.checkBoard2(board)} Moves ={all_Moves} score ={score}" )
        return evaluateFunction.eval(board)

    maxVal = -math.inf

    for startPos, allMoves in all_Moves.items():
        print(f"{all_Moves}")
        for goalPos in allMoves:
            
            i += 1 
            print(f"{i}-Iteration MAX $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")


            boardCopy = copy.deepcopy(board)
            saved_state = save_global_state()
            newBoard = makeMove.updateBoard(boardCopy, (startPos, goalPos))
            #print(f"Nach updateBoard: B={config.B_pieces}, W={config.W_pieces}, K={config.K_pieces}")
            score = alphaBetaMin(
                newBoard, alpha, beta, depth - 1,
                makeMove.total_moves(newBoard, switch(onTurn)),
                switch(onTurn), False, i
            )
            if startPos == (4, 0) and goalPos == (8, 0):
                print(f"GEWINNZUG gefunden! score={score}, maxVal={maxVal}, alpha={alpha}, beta={beta}, root={root}")

            restore_global_state(saved_state)
            #print(f"Nach restore: B={config.B_pieces}, W={config.W_pieces}, K={config.K_pieces}")

            if score > maxVal:
                maxVal = score
                #if root:
                #    config.bestMove = (startPos, goalPos)

            if score > alpha:
                alpha = score
                config.bestMove = (startPos, goalPos)

            if score >= beta:
                print("BETA CUT OFF")
                return maxVal  # Beta-Cutoff
            print(f"{startPos} ---> {goalPos} aktuelle Werte: maxVal={maxVal} alpha={alpha} beta= {beta}")

    return maxVal  # ← NACH der Schleife


def alphaBetaMin(board, alpha, beta, depth, all_Moves, onTurn, root,i):

    if depth == 0 or (not checkBoard.checkBoard2(board)) or not all_Moves:
        score = evaluateFunction.eval(board)
        print(f"reached child Note {i}-te Iteration: onTurn = {onTurn} depth={ depth} isGameOver= {not checkBoard.checkBoard2(board)} Moves ={all_Moves} score={score} " )
        return evaluateFunction.eval(board)

    minVal = math.inf

    for startPos, allMoves in all_Moves.items():
        print(f"{all_Moves}")
        for goalPos in allMoves:
            i += 1 
            print(f"{i}-Iteration MIN $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
            

            boardCopy = copy.deepcopy(board)
            saved_state = save_global_state()
            newBoard = makeMove.updateBoard(boardCopy, (startPos, goalPos))
            #print(f"Nach updateBoard: B={config.B_pieces}, W={config.W_pieces}, K={config.K_pieces}")
            score = alphaBetaMax(
                newBoard, alpha, beta, depth - 1,
                makeMove.total_moves(newBoard, switch(onTurn)),
                switch(onTurn), False, i
            )


            restore_global_state(saved_state)
            #print(f"Nach restore: B={config.B_pieces}, W={config.W_pieces}, K={config.K_pieces}")
            if score < minVal:
                minVal = score
                #if root:
                #    config.bestMove = (startPos, goalPos)
                #    print(f"NEUER BESTER MOVE: {config.bestMove}")

            if score < beta:
                beta = score
                config.bestMove = (startPos, goalPos)

            if score <= alpha:
                return minVal  # Alpha-Cutoff
            
            print(f"{startPos} ---> {goalPos} aktuelle Werte: minVal={minVal} alpha={alpha} beta= {beta}")
            


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
            all_Moves=makeMove.total_moves(board, "White"),
            onTurn="White",
            root=True
        )
    else:
        alphaBetaMin(
            board=board,
            alpha=-math.inf,
            beta=math.inf,
            depth=depth,
            all_Moves=makeMove.total_moves(board, "Black"),
            onTurn="Black",
            root=True
        )


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


board= [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 'B', 0, 0, 0, 0, 0],
    ['K', 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 'B', 0, 0, 0, 0, 0],
    [2, 0, 0, 'B', 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0] 
]


#print(config.bestMove)
#onTurn = 'White'
#print("ALPHA BETA BEGINNT")
#alphaBetaMax(board=board,alpha=-math.inf,beta=math.inf,depth=1,all_Moves=makeMove.total_moves(board,onTurn),onTurn=onTurn,root=True)
#print("ALPHA BETA ZUENDE")
#print(config.bestMove)