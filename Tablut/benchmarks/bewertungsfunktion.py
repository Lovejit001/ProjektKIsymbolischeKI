import math
import time

from tests.definitions import starting_board, alphaBeta_FinalMove
from src.models import alphaBeta
from src.gamelogic import makeMove
from src.gamelogic import config
from src.gamelogic import evaluateFunction
from src.gamelogic import debug

"""
HIER WIRD DIE BEWERTUNGSFUNKTION 10000 durchlaufen
"""

def run_speedTest(board, on_turn, iterations: int = 10_000) -> None:
    """
    Benchmark für die alphaBeta-Suche.
    """
    config.init_pieces(board)
    start_time = time.perf_counter()

    for _ in range(iterations):
        evaluateFunction.eval(board)

    duration = time.perf_counter() - start_time

    print(f"\nBoard-Test:")
    debug.print_board(board)
    print(f"Iterations: {iterations}")
    print(f"Time: {duration * 1000:.2f} ms == {duration:.6f} s")



def benchmark_alpha_beta() -> None:
    """
    Führt verschiedene Benchmark-Szenarien aus.
    """

    scenarios = [
        (starting_board, "Black"),        
        (alphaBeta_FinalMove, "Black"),
        (alphaBeta_FinalMove, "White")
    ]

    for board, turn in scenarios:
        run_speedTest(board, turn)


if __name__ == "__main__":
    benchmark_alpha_beta()