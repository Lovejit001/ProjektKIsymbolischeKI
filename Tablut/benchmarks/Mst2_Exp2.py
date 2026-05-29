import math
import time
from src import alphaBeta
from tests.definitions import starting_board, alphaBeta_FinalMove
from src import makeMove, config, debug


def iterative_deepening(board, onTurn, time_limit=1.0, max_depth=4):
    best_move = None
    best_depth = 0
    start_time = time.perf_counter()

    for depth in range(1, max_depth + 1):

        # Zeit prüfen BEVOR wir suchen
        elapsed = time.perf_counter() - start_time
        if elapsed >= time_limit:
            break

        config.init_pieces(board)
        config.bestMove = None
        config.eval_counter = 0  # ← Zähler zurücksetzen

        if onTurn == "White":
            alphaBeta.alphaBetaMax(board, -math.inf, math.inf, depth,
                                   makeMove.total_moves(board, "White"),
                                   "White", True)
        else:
            alphaBeta.alphaBetaMin(board, -math.inf, math.inf, depth,
                                   makeMove.total_moves(board, "Black"),
                                   "Black", True)

        # Zeit prüfen NACHDEM wir gesucht haben
        elapsed = time.perf_counter() - start_time

        if elapsed < time_limit:
            best_move = config.bestMove
            best_depth = depth
            print(f"  Tiefe {depth} ✓ in {elapsed:.3f}s → Zug: {best_move}")
            print(f"  Evaluierte Zustände: {config.eval_counter}")
        else:
            print(f"  Tiefe {depth} ✗ abgebrochen nach {elapsed:.3f}s")
            print(f"  Evaluierte Zustände: {config.eval_counter}")
            break

    print(f"  → Beste Tiefe: {best_depth}, Bester Zug: {best_move}\n")
    print(f"  Gesamte Zeit: {elapsed:.3f}s, Evaluierte Zustände gesamt: {config.eval_counter}")
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
        iterative_deepening(board, turn, time_limit=120.0, max_depth=4)