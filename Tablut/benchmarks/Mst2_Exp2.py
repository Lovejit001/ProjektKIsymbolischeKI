import math
import time
from tests.definitions import starting_board, alphaBeta_FinalMove
from scr import alphaBeta, makeMove, config, debug
from scr import config

"Prüft MST 2 mit Depth 4, kann noch geändert werden!"
def iterative_deepening(board, onTurn, time_limit=1.0,depth=4):
    best_move = None
    best_depth = 0
    start_time = time.perf_counter()
    #FÜR SPALTE R-U EINFACH RANGE auf 4 setzen

    elapsed = time.perf_counter() - start_time
    if elapsed >= time_limit:
        return 
            
    config.init_pieces(board)
    config.bestMove = None

    if onTurn == "White":
        alphaBeta.alphaBetaMax(board, -math.inf, math.inf, depth,
                                makeMove.total_moves(board, "White"),
                                "White", True)
    else:
        alphaBeta.alphaBetaMin(board, -math.inf, math.inf, depth,
                                makeMove.total_moves(board, "Black"),
                                "Black", True)

    elapsed = time.perf_counter() - start_time

    if elapsed < time_limit:
        best_move = config.bestMove
        best_depth = depth
        print(f"  Tiefe {depth} ✓ in {elapsed:.3f}s → Zug: {best_move}")
    else:
        print(f"  Tiefe {depth} ✗ abgebrochen nach {elapsed:.3f}s")
            
    
    print(f"Evaluierte Zustände: {config.eval_counter}")
    print(f"  → Beste Tiefe: {best_depth}, Bester Zug: {best_move}\n")
    return best_move, best_depth


if __name__ == "__main__":
    scenarios = [
        ("Startstellung", starting_board,      "Black"),
        ("Endstellung",   alphaBeta_FinalMove,  "White"),
        ("Endstellung",   alphaBeta_FinalMove,  "Black"),
    ]

    for name, board, turn in scenarios:
        print(f"{'='*55}")
        print(f"Stellung: {name} | Am Zug: {turn}")
        debug.print_board(board)
        config.reset_pieces
        iterative_deepening(board, turn, time_limit=1.0)