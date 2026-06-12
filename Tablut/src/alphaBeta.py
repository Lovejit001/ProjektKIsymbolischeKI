from src import checkBoard
from src import evaluateFunction
from src import makeMove
from src import config
from src import debug
from src import saveBoardState
from src import zugsortierung
import math
import copy


def alphaBetaMax(board, alpha, beta, depth, all_Moves, onTurn, root):

    if depth == 0 or (checkBoard.checkBoard2(board) != -2) or not all_Moves:
        score = evaluateFunction.eval(board,depth)
        return evaluateFunction.eval(board,depth)

    maxVal = -math.inf
    #HIER MUSS ALLPHA BETA 
    zugsortierung.zugsortierung(board,all_Moves)

    for startPos, allMoves in all_Moves.items():
        #print(f"{all_Moves}")

        for goalPos in allMoves:
            


            boardCopy = copy.deepcopy(board)
            saved_state = saveBoardState.save_global_state()
            newBoard = makeMove.updateBoard(boardCopy, (startPos, goalPos))

            score = alphaBetaMin(
                newBoard, alpha, beta, depth - 1,
                makeMove.total_moves(newBoard, switch(onTurn)),
                switch(onTurn), False
            )

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

    if depth == 0 or (checkBoard.checkBoard2(board) != -2) or not all_Moves:
        score = evaluateFunction.eval(board,depth)

        return evaluateFunction.eval(board,depth)

    minVal = math.inf

    zugsortierung.zugsortierung(board,all_Moves)

    for startPos, allMoves in all_Moves.items():

        for goalPos in allMoves:
            

            boardCopy = copy.deepcopy(board)
            saved_state = saveBoardState.save_global_state()
            newBoard = makeMove.updateBoard(boardCopy, (startPos, goalPos))

            score = alphaBetaMax(
                newBoard, alpha, beta, depth - 1,
                makeMove.total_moves(newBoard, switch(onTurn)),
                switch(onTurn), False
            )

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


