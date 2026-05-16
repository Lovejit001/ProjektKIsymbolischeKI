from scr import checkBoard
from scr import evaluateFunction
from scr import makeMove
from scr import config
from scr import debug
import math
import copy


def alphaBetaMax(board, alpha, beta, depth, all_Moves, onTurn, root):

    if depth == 0 or (not checkBoard.checkBoard2(board)) or not all_Moves:
        score = evaluateFunction.eval(board,depth)

        return evaluateFunction.eval(board,depth)

    maxVal = -math.inf

    for startPos, allMoves in all_Moves.items():
        #print(f"{all_Moves}")
        for goalPos in allMoves:
            

            boardCopy = copy.deepcopy(board)
            saved_state = save_global_state()
            newBoard = makeMove.updateBoard(boardCopy, (startPos, goalPos))

            score = alphaBetaMin(
                newBoard, alpha, beta, depth - 1,
                makeMove.total_moves(newBoard, switch(onTurn)),
                switch(onTurn), False
            )

            restore_global_state(saved_state)

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

    if depth == 0 or (not checkBoard.checkBoard2(board)) or not all_Moves:
        score = evaluateFunction.eval(board,depth)

        return evaluateFunction.eval(board,depth)

    minVal = math.inf

    for startPos, allMoves in all_Moves.items():

        for goalPos in allMoves:
            

            boardCopy = copy.deepcopy(board)
            saved_state = save_global_state()
            newBoard = makeMove.updateBoard(boardCopy, (startPos, goalPos))

            score = alphaBetaMax(
                newBoard, alpha, beta, depth - 1,
                makeMove.total_moves(newBoard, switch(onTurn)),
                switch(onTurn), False
            )

            restore_global_state(saved_state)
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