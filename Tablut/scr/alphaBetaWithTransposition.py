from scr import checkBoard
from scr import evaluateFunction
from scr import makeMove
from scr import config
from scr import debug
import math


def alphaBetaMax(board,alpha,beta,depth,all_Moves,onTurn,root):
    # DEBUG: Prüfe den Typ


    maxVal = -math.inf
    if depth == 0 or (not checkBoard.checkBoard2(board)):
        return evaluateFunction.eval(board)


    i = 1
    # Falls keine Züge vorhanden sind
    if not all_Moves:
        return evaluateFunction.eval(board)
    for startPos,allMoves in all_Moves.items(): 
        print(f"all possible Moves: {allMoves}")
        for goalPos in allMoves:

            #Macht den Zug
            print(f"{i}-te Iteration !")
            print(f"STARTPOSITION: {startPos}")
            print(f"ZIELPOSITION: {goalPos}")
            
            saved_state = save_global_state()
            newBoard = makeMove.updateBoard(board,(startPos,goalPos))
            debug.print_board(newBoard)
            ###BISSS HIERR PASST ALLLESS !!!!!
            score = alphaBetaMin(newBoard,alpha,beta,depth-1, makeMove.total_moves(newBoard,switch(onTurn)),(switch(onTurn)),False)
            
            #ALLE GLOBALEN VARIABLEN MÜSSEN RÜCKGÄNGIG GEMACHT WERDEN ?
            undoMoveWithState(board,startPos,goalPos,saved_state)

            print("OLDBOARD $$$$$$$$$$$$$$$$$$")
            debug.print_board(board)
            print("OLDBOARD $$$$$$$$$$$$$$$$$$")
            
            
            print(f"{i}-te Iteration ! Der Score: {score}")
            
            i += 1
            if score > maxVal: 

                #UNSICHER OB HIER DER BESTE ZUG GESPEICHERT WIRD
                print(root)
                if root == True : 
                    config.bestMove = (startPos,goalPos)
                maxVal = score
                print(f"BEST MOVE: {config.bestMove}")
            if score > alpha:
                alpha = score
            if score >= beta:
                return score # Beta-Cutoff
    


def alphaBetaMin(board, alpha,beta,depth,all_Moves,onTurn,root):
    print("MIN IST DRANNN")
    minVal = 100000000

    if depth == 0 or checkBoard.checkBoard2(board):
        print("EVAL WIRD AUSGERUFEN !!!")
        return evaluateFunction.eval(board)

    
    for startPos,allMoves in all_Moves.items():
        print(f"all possible Moves: {allMoves}") 
        for goalPos in allMoves:  


            saved_state = save_global_state()
            newBoard= makeMove.updateBoard(board,(startPos,goalPos))                                        
            score = alphaBetaMax(newBoard,alpha,beta,depth-1, makeMove.total_moves(newBoard,switch(onTurn)),switch(onTurn),False)
            #MUSS BOARD RÜCKGÄNGIG GEMACHT WERDEN ?
            undoMoveWithState(board,startPos,goalPos,saved_state)

            print("OLDBOARD $$$$$$$$$$$$$$$$$$")
            debug.print_board(board)
            print("OLDBOARD $$$$$$$$$$$$$$$$$$")

            if score < minVal:
                if root : 
                    config.bestMove = (startPos,goalPos)
                minVal = score
            if score < beta:
                beta = score
            if score <= alpha:
                return score # alpha-Cutoff
    



#SOLLTE MAN HIER LIEBER CONFIG ÄNDERN ODER LIEBER NICHT ?
def switch(onTurn): 
    if onTurn == "White":
        return "Black"
    else: 
        return "White"


board= [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 'B', 0, 0, 0, 0, 0],
    ['K', 0, 'B', 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 'B', 0, 0, 0, 0, 0],
    [0, 0, 0, 'B', 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0] 
]


#print(config.bestMove)
#onTurn = 'White'
#print("ALPHA BETA BEGINNT")
#makeMove.total_moves(board,onTurn)
#alphaBetaMax(board=board,alpha=-math.inf,beta=math.inf,depth=1,all_Moves=makeMove.total_moves(board,"White"),onTurn=onTurn,root=True)
#print("ALPHA BETA ZUENDE")
#print(config.bestMove)



def undoMoveWithState(board, startPos, goalPos, saved_state):
    """
    Macht einen Zug rückgängig UND stellt die globalen Variablen wieder her.
    """
    # Zuerst das Board rückgängig machen
    #wichtig goalPos zuerst weil das der gemacht Schritt ist der zurückgesetzt werden soll!
    undoMoveBoard(board, goalPos, startPos)
    
    # Dann die globalen Variablen wiederherstellen
    restore_global_state(saved_state)

def undoMoveBoard(board,startPos,goalPos):     

    start_row, start_col = startPos
    
    goal_row, goal_col = goalPos

    #print(f"StartPos: {random_StartPos} Zufälliger Zug: {random_GoalPos}")

    # Figur auf der Startposition merken
    figure = board[start_row][start_col]

    # Startposition leeren
    board[start_row][start_col] = 0
    
    # Zielposition mit der Figur belegen
    board[goal_row][goal_col] = figure
        
    ##UNSICHER OB NOCH WAS GEMACHT WERDEN SOLLTE !


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



