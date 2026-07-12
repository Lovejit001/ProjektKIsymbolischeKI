"""
Hier wird KI gegen KI Spielen.
KI Nr.1 hat die AlphaBeta pruning und KI 2 dasselbe mit dem Feature von Transposition Table (ermöglicht eine tiefere Suche durchzuführen)
"""
from src import config
from src import checkBoard 
from src import makeMove 
from src import attack
from src import debug
from src import alphaBetaWithTransposition
from src import alphaBeta
from benchmarks import testboards5
import time
import math
import copy


#Problem liegt bei REMIS
#Problem liegt bei REMIS
#Problem liegt bei REMIS
#Problem liegt bei REMIS
#Problem liegt bei REMIS
#Problem liegt bei REMIS
#Problem liegt bei REMIS
#Problem liegt bei REMIS


def get_move(board, onTurn, agent, time_limit, max_depth=4):
    """Ruft die Suchfunktion des angegebenen Agenten auf."""
    if agent == 'AB':
        from src import alphaBeta
        best_move, _, used_time = alphaBeta.iterative_deepening(
            board, onTurn, time_limit, max_depth
        )
    elif agent == 'AB_TT':
        from src import alphaBetaWithTransposition
        best_move, _, used_time = alphaBetaWithTransposition.iterative_deepening(
            board, onTurn, time_limit, max_depth
        )
    elif agent == 'AB_TT_PVS':
        from src import alphaBetaPVS   # passe den Import an
        best_move, _, used_time = alphaBetaPVS.iterative_deepening(
            board, onTurn, time_limit, max_depth
        )
    elif agent == 'MCTS':
        from src import mcts
        best_move, _, used_time = mcts.get_best_move(board, onTurn, time_limit)
        # MCTS liefert keine Tiefe, daher setzen wir sie auf 0
        _ = 0
    else:
        raise ValueError(f"Unbekannter Agent: {agent}")
    return best_move, used_time


def game1(board, black_agent, white_agent, time_limit=60, max_depth=4):
    """
    Spielt eine Partie zwischen zwei KI‑Agenten.
    black_agent, white_agent: Strings aus {'AB', 'AB_TT', 'AB_TT_PVS', 'MCTS'}
    Gibt zurück: 1 (Weiß gewinnt), -1 (Schwarz gewinnt), 0 (Remis)
    """
    config.reset_pieces()
    config.init_pieces(board)

    timeclock_White = time_limit
    timeclock_Black = time_limit
    config.onTurn = 'Black'
    res = -math.inf

    while checkBoard.checkBoard2(board) == -2:
        oldBoard = [row[:] for row in board]

        if config.onTurn == 'Black':
            agent = black_agent
            time_left = timeclock_Black
        else:
            agent = white_agent
            time_left = timeclock_White

        bestMove, usedTime = get_move(board, config.onTurn, agent, time_left, max_depth)

        # Zeit aktualisieren
        if config.onTurn == 'Black':
            timeclock_Black -= usedTime
            if timeclock_Black <= 0:
                print("⏰ Schwarz hat keine Zeit mehr → Weiß gewinnt!")
                return 1
        else:
            timeclock_White -= usedTime
            if timeclock_White <= 0:
                print("⏰ Weiß hat keine Zeit mehr → Schwarz gewinnt!")
                return -1

        makeMove.updateBoard(board, bestMove)

        # Zugwechsel
        config.onTurn = 'White' if config.onTurn == 'Black' else 'Black'

        if oldBoard == board:
            print("Fehler: Kein Zug ausgeführt!")
            break

    # Spiel zu Ende – Ergebnis aus der Brettbewertung
    res = checkBoard.checkBoard2(board)
    if res == 0:
        print("Remis")
    elif res == -1:
        print("Schwarz gewinnt")
    elif res == 1:
        print("Weiß gewinnt")
    
    return res


def play(board, agent1, agent2, time_limit=60, max_depth=4):
    """
    Spielt zwei Partien:
    1) agent1 = Schwarz, agent2 = Weiß
    2) agent1 = Weiß,  agent2 = Schwarz
    Gibt zurück: (ergebnis_1, ergebnis_2)
    Ergebnis: -1 = Schwarz gewinnt, 1 = Weiß gewinnt, 0 = Remis
    """
    # Partie 1: agent1 als Schwarz, agent2 als Weiß
    res1 = game1(board, agent1, agent2, time_limit, max_depth)
    # Partie 2: agent1 als Weiß, agent2 als Schwarz
    res2 = game1(board, agent2, agent1, time_limit, max_depth)
    return res1, res2


def add_result(res, agent_black, agent_white, scores):
    """
    Aktualisiert die Scores basierend auf dem Ergebnis einer Partie.
    scores = {'AB':0, 'AB_TT':0, 'AB_TT_PVS':0, 'MCTS':0, 'draw':0}
    """
    if res == -1:          # Schwarz gewinnt
        scores[agent_black] += 1
    elif res == 1:         # Weiß gewinnt
        scores[agent_white] += 1
    else:                  # Remis
        scores['draw'] += 1

def main():
    boards = testboards5.all_boards
    time_limit = 60
    max_depth = 4

    # Definiere die Paarungen, die du testen willst
    pairings = [
        ('AB', 'AB_TT'),
        ('AB', 'AB_TT_PVS'),
        ('AB_TT', 'AB_TT_PVS'),
        ('AB', 'MCTS'),
        ('AB_TT', 'MCTS'),
        ('AB_TT_PVS', 'MCTS'),
    ]

    # Für jede Paarung einen eigenen Score‑Zähler
    all_scores = {}

    for agent1, agent2 in pairings:
        scores = {agent1: 0, agent2: 0, 'draw': 0}
        for board in boards:

            # Zwei Partien (Farben getauscht)
            res1, res2 = play(board, agent1, agent2, time_limit, max_depth)
            add_result(res1, agent1, agent2, scores)
            add_result(res2, agent2, agent1, scores)  # Achtung: Farben getauscht!

        all_scores[(agent1, agent2)] = scores

    # Ergebnisse ausgeben
    for (a1, a2), scores in all_scores.items():
        total = scores[a1] + scores[a2] + scores['draw']
        print(f"\n📊 {a1} vs {a2}:")
        print(f"  {a1} Siege: {scores[a1]} ({scores[a1]/total*100:.1f}%)")
        print(f"  {a2} Siege: {scores[a2]} ({scores[a2]/total*100:.1f}%)")
        print(f"  Remis:    {scores['draw']} ({scores['draw']/total*100:.1f}%)")