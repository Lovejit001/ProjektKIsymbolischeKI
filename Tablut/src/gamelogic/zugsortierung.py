from src.gamelogic import config
from src.gamelogic import makeMove
from src.gamelogic import saveBoardState

import copy

B = 'B'
W = 'W'
K = 'K'
"""
Zugsortierung bevor Alpha-Beta gelaufen wird. 
Idee: Bevor jeder alpha-Beta läuft soll die Liste optimal sortiert werden, d.h hier wird versucht die besten Züge direkt ganz nach in der Liste zu pascken
=> Somit können die Cutoffs besser genutzt werden 


"""
#allMoves Syntax: allMoves = {(StartPos1):[GoalPos1], (StartPos2):[GoalPos2], (StartPos3):[GoalPos3], ..., }
def zugsortierung(board,allMoves : dict):
   
    config.init_pieces(board)
    #config.onTurn = 'Black'

    for startPos, possible_moves in allMoves.items():
        ordered_list = order(board,startPos,possible_moves)
        allMoves[startPos] = ordered_list


def order(board,startPos,possible_moves):

    moves_weighted = []
    final_list = []

  
    for move in possible_moves:
      
        score =  getScore(board,startPos,move)
        moves_weighted.append((move,score))

    if config.onTurn == 'White':
        moves_weighted.sort(key= lambda  item: item[1],reverse=True)
    else:
        moves_weighted.sort(key= lambda  item: item[1])

    final_list = [move for move, weight in moves_weighted]

    return final_list


def getScore(board,startPos,goalPos):
    sRow,sCol= startPos
    gRow,gCol= goalPos
    
    copyBoard = copy.deepcopy(board)

    if ((board[sRow][sCol]== config.K) and ((gRow,gCol) in config.Goal)):
        return 10
        
    if ((board[sRow][sCol]== config.K) and ((gRow,gCol) in config.Edge)):
        return 7
    
    
    saved_state = saveBoardState.save_global_state()
    makeMove.updateBoard(copyBoard, (startPos, goalPos))
    if (config.K_pieces == 0):
        saveBoardState.restore_global_state(saved_state)
        return -10
    saveBoardState.restore_global_state(saved_state)
    
    if (board[sRow][sCol]== config.B) and (isNextToKing(board,goalPos)):
        return -7
    
    return 0 


def isNextToKing(board,goalPos):
    row,col=goalPos
    flag1 = False
    flag2 = False
    flag3 = False
    flag4 = False

    if (row+1)<= 8: #8:Zeilenanzahl
        flag1 = (board[row+1][col]== config.K)
    if (row-1) >= 0: 
        flag2 = (board[row-1][col]== config.K)
    if (col+1) <= 8:#8:Spaltenanzahl
        flag3 = (board[row][col+1]== config.K)
    if (col-1) >= 0:
        flag4 = (board[row][col-1]== config.K)
    
    return flag1 or flag2 or flag3 or flag4
