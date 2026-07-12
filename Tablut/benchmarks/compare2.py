"""
Hier wird die geschwindikeit der Zugsuche der jeweiligen 4 KI Versionen ermittelt, in abhängigkeit vom Board und ihre Komplexität
"""

import math
import time
import copy
from src.Node import MCTS
from src import alphaBeta
from src import alphaBetaWithTransposition
from src import alphaBetaWithPVS
from tests.definitions import starting_board, alphaBeta_FinalMove
from src import makeMove, config, debug
from .testboard_for2Graph import all_boards


def iterative_deepening(board, onTurn, time_limit=10.0, max_depth=4,algo=1):

    best_move = None
    best_depth = 0
    start_time = time.perf_counter()
    config.stop_time = math.inf #Dieser Timer wird auf unenedlich gesetzt, da er für den Benchmark nicht relevant ist, beim tatsächtlichen Spielen schon.
    number_simulations=2000

    for depth in range(1, max_depth + 1 ):

        if depth != max_depth:
            continue

        # Zeit prüfen BEVOR wir suchen
        elapsed = time.perf_counter() - start_time
        if elapsed >= time_limit:
            break
        
        config.init_pieces(board)
        
        config.eval_counter = 0  # ← Zähler zurücksetzen
        if algo == 1: #Alphabeta
            score = alphaBeta.getBestMove2(board,onTurn,depth)
        elif algo == 2:#AlphaBeta +move Order + TT
            score = alphaBetaWithTransposition.getBestMove2(board,onTurn,depth)
        elif algo == 3:
            score = alphaBetaWithPVS.getBestMove2(board,onTurn,depth)
        else: #MCTS
            b = copy.deepcopy(board)
            root = MCTS().run(
            state=b,
            onTurn=onTurn,
            number_simulations=number_simulations
            )
            best_move, _, score = root.best_child()
    

        # Zeit prüfen NACHDEM wir gesucht haben
        elapsed = time.perf_counter() - start_time

        if elapsed < time_limit:
            best_move = config.bestMove
            best_depth = depth
            number_simulations += 150
            print(f"  Tiefe {depth} ✓ in {elapsed:.3f}s → Zug: {best_move} --> SCORE {score}")
            print(f"  Evaluierte Zustände: {config.eval_counter}")
        else:
            print(f"  Tiefe {depth} ✗ abgebrochen nach {elapsed:.3f}s")
            print(f"  Evaluierte Zustände: {config.eval_counter}")
            break

        
    print(f"  → Beste Tiefe: {best_depth}, Bester Zug: {best_move}\n")
    print(f"  Gesamte Zeit: {elapsed:.3f}s, Evaluierte Zustände gesamt: {config.eval_counter}")
    
    elapsed = round(elapsed, 3)
    

    return best_move, best_depth, elapsed

def run():
    turn = 'White'
    result = []
    temp = []

  
    for board in all_boards:
        print(f"{'='*55}")
        #print(f"Stellung: {name} | Am Zug: {turn}")
        print(f"Stellung | Am Zug: {turn}")
        debug.print_board(board)
        _, _, values =iterative_deepening(board, turn, time_limit=120.0, max_depth=3,algo=1)
        temp.append(values)

    result.append(temp)
    temp = []

    for board in all_boards:
        print(f"{'='*55}")
        #print(f"Stellung: {name} | Am Zug: {turn}")
        print(f"Stellung | Am Zug: {turn}")
        debug.print_board(board)
        _, _, values =iterative_deepening(board, turn, time_limit=120.0, max_depth=3,algo=2)
        temp.append(values)
    
    result.append(temp)
    temp = []

    for board in all_boards:
        print(f"{'='*55}")
        #print(f"Stellung: {name} | Am Zug: {turn}")
        print(f"Stellung | Am Zug: {turn}")
        debug.print_board(board)
        _, _, values =iterative_deepening(board, turn, time_limit=120.0, max_depth=3,algo=3)
        temp.append(values)
    
    result.append(temp)
    temp = []

    for board in all_boards:
        print(f"{'='*55}")
        #print(f"Stellung: {name} | Am Zug: {turn}")
        print(f"Stellung | Am Zug: {turn}")
        debug.print_board(board)
        _, _, values =iterative_deepening(board, turn, time_limit=120.0, max_depth=3,algo=4)
        temp.append(values)
    
    result.append(temp)
    temp = []

    print(result)
    return result
    

#if __name__ == "__main__":
    #scenarios = [
    #    ("Startstellung", starting_board,      "Black"),
    #    ("Endstellung",   alphaBeta_FinalMove,  "White"),
    #    ("Endstellung",   alphaBeta_FinalMove,  "Black"),
    #]
    
    #turn = 'White'
    
    #for board in all_boards:
    #    print(f"{'='*55}")
    #    #print(f"Stellung: {name} | Am Zug: {turn}")
    #    print(f"Stellung | Am Zug: {turn}")
    #    debug.print_board(board)
    #    iterative_deepening(board, turn, time_limit=120.0, max_depth=4)