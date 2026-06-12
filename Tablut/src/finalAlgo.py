from src import checkBoard
from src import evaluateFunction
from src import makeMove
from src import config
from src import debug
from src import zugsortierung
from src import saveBoardState
import copy, time, math

def alphaBetaMax(board, alpha, beta, depth, all_Moves, onTurn, root):

    if depth == 0 or (checkBoard.checkBoard2(board) != -2) or not all_Moves or config.timeout:
        return evaluateFunction.eval(board, depth)

    maxVal = -math.inf
    zugsortierung.zugsortierung(board, all_Moves)

    first_move = True

    for startPos, allMoves in all_Moves.items():
        for goalPos in allMoves:

            current_time = time.time()

            if current_time >= config.endTime:
                config.timeout = True
                
                if maxVal != -math.inf:
                    return maxVal
                else:
                    return evaluateFunction.eval(board,depth)
            

            boardCopy = copy.deepcopy(board)
            saved_state = saveBoardState.save_global_state()
            newBoard = makeMove.updateBoard(boardCopy, (startPos, goalPos))
            next_moves = makeMove.total_moves(newBoard, switch(onTurn))

            if first_move:
                score = alphaBetaMin(newBoard, alpha, beta, depth - 1, next_moves, switch(onTurn), False)
                first_move = False

            else:
                score = alphaBetaMin(newBoard, alpha, alpha + 1, depth - 1, next_moves, switch(onTurn), False)
                if alpha < score < beta:
                    score = alphaBetaMin(newBoard, alpha, beta, depth - 1, next_moves, switch(onTurn), False)

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

    if depth == 0 or (checkBoard.checkBoard2(board) != -2) or not all_Moves or config.timeout:
        return evaluateFunction.eval(board, depth)

    minVal = math.inf
    zugsortierung.zugsortierung(board, all_Moves)

    first_move = True

    for startPos, allMoves in all_Moves.items():
        for goalPos in allMoves:

            current_time = time.time()

            if current_time >= config.endTime:
                config.timeout = True
                if minVal != math.inf:
                    return minVal
                else:
                    return evaluateFunction.eval(board,depth)
                            

            boardCopy = copy.deepcopy(board)
            saved_state = saveBoardState.save_global_state()
            newBoard = makeMove.updateBoard(boardCopy, (startPos, goalPos))
            next_moves = makeMove.total_moves(newBoard, switch(onTurn))

            if first_move:
                score = alphaBetaMax(newBoard, alpha, beta, depth - 1, next_moves, switch(onTurn), False)
                first_move = False

            else:
                score = alphaBetaMax(newBoard, beta - 1, beta, depth - 1, next_moves, switch(onTurn), False)
                if alpha < score < beta:
                    score = alphaBetaMax(newBoard, alpha, beta, depth - 1, next_moves, switch(onTurn), False)

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
    return "Black" if onTurn == "White" else "White"


def getBestMove(board, onTurn, depth):

    if config.timeout:
        return None
    
    config.startingTime = time.time()
    
    if(onTurn == "White"):
        remainingTime = config.remainingWhiteTime
    else:
        remainingTime = config.remainingBlackTime
    
    move_time_limit = max(1.0, remainingTime * 1)

    config.endTime = config.startingTime + move_time_limit
    
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