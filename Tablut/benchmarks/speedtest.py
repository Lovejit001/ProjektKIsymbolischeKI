"""
Hier wird die geschwindikeit der Zugsuche der jeweiligen 4 KI Versionen ermittelt, in abhängigkeit vom Board und ihre Komplexität
Um dies laufen zu lassen die folgende file runnen: visual_time.py 
"""

import math
import time
import copy
from src.gamelogic import debug
from src.models.MCTS_UCT_PB import MCTS
from src.models import alphaBeta
from src.models import alphaBetaWithTransposition
from src.models import alphaBetaWithPVS
from src.gamelogic import config
from .testboard_speedtest import all_boards


def iterative_deepening(board, onTurn, time_limit=10.0, max_depth=4,algo=1):

    best_move = None
    best_depth = 0
    start_time = time.perf_counter()
    config.stop_time = math.inf #Dieser Timer wird auf unenedlich gesetzt, da er für den Benchmark nicht relevant ist, beim tatsächtlichen Spielen schon.
    number_simulations=2000

    for depth in range(1, max_depth + 1 ):

        if depth != max_depth and algo != 3:
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

    print(f"{'$'*55}")
    print("alphaBeta")
    print(f"{'$'*55}")
 
    for board in all_boards:
        print(f"{'='*55}")
        #print(f"Stellung: {name} | Am Zug: {turn}")
        print(f"Stellung | Am Zug: {turn}")
        debug.print_board(board)
        _, _, values =iterative_deepening(board, turn, time_limit=120.0, max_depth=3,algo=1)
        temp.append(values)

    result.append(temp)
    temp = []

    print(f"{'$'*55}")
    print("alphaBeta + move Ordering + Transpostion table")
    print(f"{'$'*55}")

    for board in all_boards:
        print(f"{'='*55}")
        #print(f"Stellung: {name} | Am Zug: {turn}")
        print(f"Stellung | Am Zug: {turn}")
        debug.print_board(board)
        _, _, values =iterative_deepening(board, turn, time_limit=120.0, max_depth=3,algo=2)
        temp.append(values)
    
    result.append(temp)
    temp = []

    print(f"{'$'*55}")
    print("alphaBeta + move Ordering + Transpostion table + Principal Variation Search")
    print(f"{'$'*55}")

    for board in all_boards:
        print(f"{'='*55}")
        #print(f"Stellung: {name} | Am Zug: {turn}")
        print(f"Stellung | Am Zug: {turn}")
        debug.print_board(board)
        _, _, values =iterative_deepening(board, turn, time_limit=120.0, max_depth=3,algo=3)
        temp.append(values)
    
    result.append(temp)
    temp = []

    print(f"{'$'*55}")
    print("Monte Carlo Tree Search (MCTS) + Upper Confidence Bound (UCB) + Progressive Bias")
    print(f"{'$'*55}")

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
    

