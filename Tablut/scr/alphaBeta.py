from scr import checkBoard
from scr import evaluateFunction
from scr import makeMove
from scr import config
import math

def alphaBetaMax(board,alpha,beta,depth,all_Moves,onTurn,root):
    # DEBUG: Prüfe den Typ
    if not isinstance(all_Moves, dict):
        print(f"FEHLER: all_Moves ist {type(all_Moves)} statt dict")
        print(f"Inhalt: {all_Moves}")
        return evaluateFunction.eval(board)

    maxVal = -math.inf
    if depth == 0 or (not checkBoard.checkBoard2(board)):
        print("EVALLLLL ERREICHTTT")
        print(evaluateFunction.eval(board))
        return evaluateFunction.eval(board)
    #Remember its a dictionary {(startRow,startCol):[(goalRow,goalCol),....]}


    # Falls keine Züge vorhanden sind
    if not all_Moves:
        return evaluateFunction.eval(board)
    for startPos,allMoves in all_Moves.items(): 
        print("BBBBBBB")
        for goalPos in allMoves:
            print("CCCCCCC")                
            #Macht den Zug
            print(f"{switch(onTurn)}")
            newBoard = makeMove.updateBoard(board,(startPos,goalPos))
            print("ASKDNASLDNWANDLAKDNALKNDWLAKDN")
            score = alphaBetaMin(newBoard,alpha,beta,depth-1, makeMove.total_moves(newBoard,switch(onTurn)),(switch(onTurn)),False)
            #MUSS BOARD RÜCKGÄNGIG GEMACHT WERDEN ?

            print("SCORREE ISS:")
            print(score)

            if score > maxVal: 
                print("ALPHAAAAA")
                #UNSICHER OB HIER DER BESTE ZUG GESPEICHERT WIRD
                if root == True : 
                    print("BEST MOVEEE:")
                    print(startPos)
                    print(goalPos)
                    config.bestMove = (startPos,goalPos)

                maxVal = score
            if score > alpha:
                print("BESTEEE ASJDNOAWNDMOANDAOINDOAWNM")
                alpha = score
            if score >= beta:
                return score # Beta-Cutoff
    


def alphaBetaMin(board, alpha,beta,depth,all_Moves,onTurn,root):
    

    # DEBUG: Prüfe den Typ
    if not isinstance(all_Moves, dict):
        print(f"FEHLER: all_Moves ist {type(all_Moves)} statt dict")
        print(f"Inhalt: {all_Moves}")
        return evaluateFunction.eval(board)
    
    minVal = 100000000

    if depth == 0 or checkBoard.checkBoard2(board):
        return evaluateFunction.eval(board)

    

    for startPos,allMoves in all_Moves.items(): 
        for goalPos in allMoves:  
        
            newBoard= makeMove.updateBoard(board,(startPos,goalPos))                                        #DOPPEL ONTRURN RICHTIGT``
            score = alphaBetaMax(newBoard,alpha,beta,depth-1, makeMove.total_moves(newBoard,switch(onTurn)),switch(onTurn),False)
            #MUSS BOARD RÜCKGÄNGIG GEMACHT WERDEN ?

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