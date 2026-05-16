import math
import time

from tests.definitions import starting_board, alphaBeta_FinalMove
from scr import alphaBeta
from scr import makeMove
from scr import config

def run_speedTest(board, on_turn, iterations: int = 10_000, depth: int = 10) -> None:
    """
    Benchmark für die alphaBeta-Suche.
    """

    start_time = time.perf_counter()

    for _ in range(iterations):
        alphaBeta.alphaBetaMax(
            board=board,
            alpha=-math.inf,
            beta=math.inf,
            depth=depth,
            all_Moves=makeMove.total_moves(board, on_turn),
            onTurn=on_turn,
            root=True
        )

    duration = time.perf_counter() - start_time

    print(f"\nBoard-Test: {board}")
    print(f"Iterations: {iterations}")
    print(f"Time: {duration * 1000:.2f} ms")
    print(f"Time: {duration:.6f} s")


def benchmark_alpha_beta() -> None:
    """
    Führt verschiedene Benchmark-Szenarien aus.
    """

    scenarios = [
        (starting_board, "Black"),
        (alphaBeta_FinalMove, "Black"),
        (alphaBeta_FinalMove, "White"),
    ]

    for board, turn in scenarios:
        run_speedTest(board, turn)


if __name__ == "__main__":
    benchmark_alpha_beta()