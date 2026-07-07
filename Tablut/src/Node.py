import copy
import math
import random

from . import makeMove
from . import debug
from . import config
from . import saveBoardState
from .checkBoard import checkBoard2
from .config import init_pieces
from .evaluateFunction import eval
from tests.definitions import starting_board



B = 'B'
W = 'W'
K = 'K'




def print_path_to_best(node):
    """Gibt den Pfad zum Knoten mit der besten Bewertung aus."""
    best_node = node
    depth = 0
    path = []
    
    while best_node.expanded():
        # Finde besten Kindknoten
        best_score = -float('inf')
        best_child = None
        best_move = None
        
        for move, child in best_node.children.items():
            score = child.score_sum / child.visit_count if child.visit_count > 0 else 0
            if score > best_score:
                best_score = score
                best_child = child
                best_move = move
        
        if best_child:
            path.append((best_move, best_score))
            best_node = best_child
            depth += 1
        else:
            break
    
    print(f"\nBester Pfad ({depth} Züge tief):")
    for i, (move, score) in enumerate(path):
        print(f"  Schritt {i+1}: {move[0]} -> {move[1]} (Score: {score:.3f})")
    print(f"Endknoten: Besuche={best_node.visit_count}, ∅={best_node.score_sum/best_node.visit_count if best_node.visit_count > 0 else 0:.3f}")

def pathed(list):
    for e in list :
        print(f"--> {len(e.children)}" , end=" ")

def switchTurn(onTurn):
        if onTurn == 'White':
            return 'Black'
        else: 
            return 'White'
        

def ucb_score(parent, child):

    #Explorationskonstante
    C=1
    progressive_bias_weight = 0.5

    if child.visit_count == 0:
        return math.inf
    
    value = -child.value() if child.visit_count > 0 else 0
    explore = C * math.sqrt(math.log(parent.visit_count + 1) / child.visit_count)

    progressive_bias = 0
    if child.state is not None:
        heuristic = eval(child.state, 0)
        if parent.onTurn == 'Black':
            heuristic = -heuristic

        normalized_heuristic = math.tanh(heuristic / 100000)
        progressive_bias = (
            progressive_bias_weight
            * normalized_heuristic
            / (child.visit_count + 1)
        )

    return value + explore + progressive_bias


def legal_moves(board, onTurn):
    all_Moves = makeMove.total_moves(board, onTurn)
    if not isinstance(all_Moves, dict):
        return {}

    return {
        startPos: moves
        for startPos, moves in all_Moves.items()
        if moves
    }

class Node:

    def __init__(self,onTurn):
        self.score_sum = 0
        self.visit_count = 0
        self.state = None
        self.children = {}
        self.onTurn = onTurn  

    def expanded(self):
        return len(self.children) > 0 
    
    def value(self):
        if self.visit_count == 0:
            return 0 
        return self.score_sum / self.visit_count

    #Funktion da damit alle Unterknoten eines knoten erstellt werden (Jeder Unterknoten hat einen anderen Zug, d.h einen anderen Board
    def expand(self,state,onTurn):
        
        # Spiel bereits beendet
        if checkBoard2(state) != -2:   
            return
        
        self.state = state
        self.onTurn = onTurn

        #allmoves = {(startRow,startCol):[ ( (startRow,StartCol) , (goalRow,Row) ) ] }  
        all_Moves=legal_moves(self.state, onTurn)

        for startPos, movesList in all_Moves.items():

            for goalPos in movesList :

                self.children[(startPos, goalPos)] = Node(switchTurn(onTurn))


    def add_child(self,node):
        self.child.append(node)


    def avg_value(self):
        return self.value()

    def select_child(self):
        
        best_score= -math.inf
        best_score2= math.inf
        bestChild = None 
        bestMove = None

        for move,child in self.children.items():
            #TODO UCB Logik implementieren !
            
            #if child.visit_count == 0 :
            #    return move, child
            #score = child.score_sum / child.visit_count #TODO: AUSBAUFÄHIG Das erste Knoten das nie besucht wurde wird als erstes besucht ohne Ausnahme 
            score = ucb_score(self,child)

            if score > best_score or (score == best_score and random.random() < 0.5):
                best_score = score
                bestChild = child
                bestMove = move
        
        return bestMove, bestChild    

    def best_child(self):
        best_score = -math.inf
        bestChild = None
        bestMove = None

        for move, child in self.children.items():
            if child.visit_count == 0:
                continue

            # child.value() ist aus Sicht des Spielers im Kindknoten.
            # Der Elternknoten bewertet denselben Wert mit umgedrehtem Vorzeichen.
            score = -child.value()
            if score > best_score or (score == best_score and random.random() < 0.5):
                best_score = score
                bestChild = child
                bestMove = move

        if bestMove is None and self.children:
            bestMove, bestChild = max(
                self.children.items(),
                key=lambda item: item[1].visit_count
            )
            best_score = -bestChild.value()

        return bestMove, bestChild, best_score
    
    
        
class MCTS:

    def score_for_player(self, board, depth, onTurn):
        score = eval(board, depth)

        if onTurn == 'White':
            return score
        else:
            return -score

    def run(self,state,onTurn,number_simulations = 10000):
        #alle Globalen Variablen merken, da nun alles nachdem MCTS gleich bleiben soll und die Simulationen nix am Spiel ändern dürfen

        #PROVISORSCH TO DO WEIL NOCH NICHT IN GAME LOGIK DRIN IST 
        init_pieces(state)
        
        saved_state = saveBoardState.save_global_state()
        #print("VORHER ")
        #print(config.B_pieces)
        #print(config.W_pieces)
        #print(config.K_pieces)
        #TODO EINE ART UNDOMOVE muss rein weil sonst tatsächtliches Board modifiziert wird

        #root = Node(state, onTurn)
        root = Node(onTurn)  
        #Knoten wird expandiert, d.h alle Kinder Knoten generiert 
        root.expand(state, onTurn)

        #Beginn der Simulation:

        for _ in range(number_simulations):
            node = root
            searched_path=[node]

            #durch traveserieren bis man zum neuen unbekannten Knoten kommt
            #LOGIK UNKLAR WANN FÜREN WIR DEN MOVE AUS ? 
            while node.expanded():                
                move, node = node.select_child()                
                searched_path.append(node)
                     
            parent = searched_path[-2]
            #TODO alternitve finden kann ineffizent sein
            new_state = copy.deepcopy(parent.state)             
            makeMove.updateBoard(new_state,move)
                        
            init_pieces(new_state)

            #Falls das Spiel nicht nun zu Ende findet eine Simulation statt.
            #if checkBoard2(new_state) == -2:
            score  = self.simulate(new_state,node.onTurn)


            node.expand(new_state,node.onTurn)

            self.backpropagate(searched_path,score)
            #print("\nPATH:")
            #pathed(searched_path)

        saveBoardState.restore_global_state(saved_state)

        #print_path_to_best(root)


        #print("FINALER MOVE")
        #print(root.score_sum)
        #print(root.visit_count)
        #debug.print_debug(root.state)


        #print("NACHHER  ")
        #print(config.B_pieces)
        #print(config.W_pieces)
        #print(config.K_pieces)

        move, _, _ = root.best_child()   
        #print("BEST MOVE:")
        #print(move)
        #for move,node in root.children.items():
            #print(f"{move} -- {node.score_sum}")

        #print("BEST MOVE")
        best_move = max(root.children.items(), key=lambda item: item[1].visit_count)[0]
        #print(best_move)


        
        # Wähle den Zug mit dem höchsten Score, aber nur wenn er oft genug besucht wurde
        best_move, _, best_score = root.best_child()

        # Fallback: Falls kein Zug die Mindestbesuche hat, nimm den meistbesuchten
        if best_move is None:
            best_move = max(root.children.items(), key=lambda item: item[1].visit_count)[0]
    
        #print(f"BEST MOVE: {best_move} (Score: {best_score})")

        return root


    def backpropagate(self, searched_path, score):

        for node in reversed(searched_path):             
            node.visit_count += 1 
            #Ich glaube Score kann man einfach einsetzen ohne etwas zu ändern 
            node.score_sum += score 
            score = -score   # Perspektivenwechsel


    def simulate(self,state,onTurn):

        saved_state = saveBoardState.save_global_state()
        score = 0
        currentPlayer = onTurn
        board = copy.deepcopy(state)
        i = 0 

        while(checkBoard2(board) == -2 ):
            
            #Wenn nach 100 Zügen das Spiel nicht zuende ist wird  wird Unentschieden 0 zurückgegeben
            if i == 30: 
                saveBoardState.restore_global_state(saved_state)
                return 0 
            
            #Zufälligen Zug wählen
            all_Moves = legal_moves(board,currentPlayer)

            if not all_Moves:
                score = self.score_for_player(board, -i, onTurn)
                saveBoardState.restore_global_state(saved_state)
                return score

            startPos = random.choice(list(all_Moves.keys()))
            goalPos = random.choice(all_Moves[startPos])
            
            #Zufälligen Zug machen
            makeMove.updateBoard(board,(startPos,goalPos))

            #ander Spieler ist dran 
            currentPlayer  = switchTurn(currentPlayer )
            i += 1 

            #debug.print_board(board)

        #Wenn Spielzuende ist wird nochmal einmal zu viel gemacht daher muss man hier einmal zurücksetzen
        
        #print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        #debug.print_board(board)
        # In MCTS ist i die Anzahl bereits gespielter Simulationszuege.
        # evaluateFunction.eval erwartet aber: groesserer depth = frueherer Gewinn.
        score = self.score_for_player(board, -i, onTurn)
        #print(f"Score IST {score} onTurn: {onTurn} ")
        
        saveBoardState.restore_global_state(saved_state)
        return score

    
    

movingBoard1 = [
    [0, 0, 0, 0, 0, 0, B, 0, 0],
    [B, 0, 0, B, 0, 0, 0, 0, 0],
    [0, B, 0, 0, 0, 0, 0, 0, 0],
    [0, B, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, B, 0, 0, 0, 0, K],
    [0, 0, 0, B, 0, 0, 0, 0, 0],
    [0, B, B, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0] 
]


#if __name__ == "__main__":
    #board = movingBoard1
    #board = starting_board
    #onTurn = 'White'

    #mcts = MCTS()
    #root = mcts.run(state=board,onTurn=onTurn)
    #print("Ende")
    #print(root.avg_value())
