import copy
import time

from src import config, debug
from src.Node import MCTS
from tests.definitions import starting_board, alphaBeta_FinalMove


def benchmark_mcts(board, onTurn, number_simulations=100):
    board_copy = copy.deepcopy(board)

    config.init_pieces(board_copy)
    config.eval_counter = 0

    start_time = time.perf_counter()
    root = MCTS().run(
        state=board_copy,
        onTurn=onTurn,
        number_simulations=number_simulations
    )
    elapsed = time.perf_counter() - start_time

    best_move, best_child, best_score = root.best_child()
    visits = best_child.visit_count if best_child is not None else 0

    print(f"  Simulationen: {number_simulations}")
    print(f"  Bester Zug: {best_move}")
    print(f"  Score: {best_score}")
    print(f"  Visits bester Zug: {visits}")
    print(f"  Evaluierte Zustände: {config.eval_counter}")
    print(f"  Gesamte Zeit: {elapsed:.3f}s\n")

    return best_move, best_score, elapsed


if __name__ == "__main__":
    scenarios = [
        ("Startstellung", starting_board, "Black"),
        ("Endstellung", alphaBeta_FinalMove, "White"),
        ("Endstellung", alphaBeta_FinalMove, "Black"),
    ]

    for name, board, turn in scenarios:
        print(f"{'='*55}")
        print(f"Stellung: {name} | Am Zug: {turn}")
        debug.print_board(board)
        benchmark_mcts(board, turn, number_simulations=10000)
