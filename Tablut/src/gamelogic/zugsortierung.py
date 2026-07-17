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
   
   #config.init_pieces(board) --> muss beim Testen aktiviert werden weil globale Variablen nicht initialisiert, im richtigen Spiel schon
    
    #TODO: DAS IST REDUNDANT, trotzdem ist es mit initPieces schneller als ohne obwohl anzahl pieces wir kennen WARUM ist das so ?  
    config.init_pieces(board)
    #config.onTurn = 'Black'


    for startPos, possible_moves in allMoves.items():
        ordered_list = order(board,startPos,possible_moves)
        allMoves[startPos] = ordered_list


def order(board,startPos,possible_moves):

    moves_weighted = []
    final_list = []

    #Liste erstellen die Move und die Gewichtung mit hat. 
    for move in possible_moves:
        #Hier muss eine Art Bewertungsfunktion
        score =  getScore(board,startPos,move)
        moves_weighted.append((move,score))

    #print(f"GEWICHTETE LISTE: {moves_weighted}")
    #Liste nach dem Gewicht sortieren: Strukur der Liste: [((0,1),10), ((0,1),5), ((0,1),1) ]
    #Das Zweite Elemement in jedem Tupel ist die Gewichtung des jeweiligen Zuges. Weiß sucht nach hohen score, black für niedrigen Score
    if config.onTurn == 'White':
        moves_weighted.sort(key= lambda  item: item[1],reverse=True)
    else:
        moves_weighted.sort(key= lambda  item: item[1])

    #Gewichte abnehmen, da sie nicht in der ursprünglichen Dict sein sollte.
    final_list = [move for move, weight in moves_weighted]

    return final_list


def getScore(board,startPos,goalPos):
    sRow,sCol= startPos
    gRow,gCol= goalPos
    
    copyBoard = copy.deepcopy(board)

    #Beste Züge für Weiß: ==================================================
    #1.Fall: König gelangt ins Eckfeld
    if ((board[sRow][sCol]== config.K) and ((gRow,gCol) in config.Goal)):
        return 10
    #TODO: 2.Fall: Letzte Schwarze Figur wird geschlagen
    
    #3.Fall König hat freibahn zum Rand des Boards sich zu bewegen
    if ((board[sRow][sCol]== config.K) and ((gRow,gCol) in config.Edge)):
        return 7

    #TODO: 4.Fall König ist tödlichen Position und befreit sich    
    
    #Beste Züge für Schwarz: ================================================
    
    #1.Fall: Schwarze Figur schlägt König 
    saved_state = saveBoardState.save_global_state()
    makeMove.updateBoard(copyBoard, (startPos, goalPos))
    if (config.K_pieces == 0):
        saveBoardState.restore_global_state(saved_state)
        #print(f"KÖNIG GEKILLT {startPos}-->{goalPos}")
        return -10
    saveBoardState.restore_global_state(saved_state)
    
    #Guter Move für Schwarz wenn er sich neben King stellt
    if (board[sRow][sCol]== config.B) and (isNextToKing(board,goalPos)):
        return -7
    
    #Falls keiner der Falle zu trifft soll keine Gewichtung erhalten werden
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


board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [B, 0, 0, 0, K, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, B, 0, 0, 0, 0] 
]  



totalMoves = makeMove.total_moves(board,'Black')
#print("BEVOR ZUGSORTIERUNG")
#debug.print_dic(totalMoves)
zugsortierung(board,totalMoves)
#print("=====================================================")
#print("NACH ZUGSORTIERUNG")
#debug.print_dic(totalMoves)