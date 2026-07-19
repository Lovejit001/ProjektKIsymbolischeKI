#!/usr/bin/env python3
"""
match_example.py - Einzelner Match-Durchlauf zwischen zwei KI-Engines.
Am Anfang kann einfach eingestellt werden, welche KI gegen welche spielt.
Das Startboard wird angezeigt, jeder Zug wird ausführlich ausgegeben.
"""

import sys
import os
import time
import copy
import math

# Füge Projekt-Root zum Pfad hinzu
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.gamelogic import config
from src.gamelogic import checkBoard
from src.gamelogic import makeMove
from src.gamelogic import debug
from src.gamelogic import saveBoardState
from tests import definitions


# ============================================================================
# KONFIGURATION - HIER EINSTELLEN!
# ============================================================================

# Verfügbare Engines:
#   "AB"           - Alpha-Beta (einfach)
#   "AB_TT"        - Alpha-Beta mit Transposition Table
#   "AB_TT_PVS"    - Alpha-Beta mit Transposition Table + PVS
#   "MCTS"         - Monte-Carlo-Tree-Search (mit UCT + Progressive Bias)

# Welche Engine spielt als Schwarz?
BLACK_ENGINE = "AB_TT"

# Welche Engine spielt als Weiß?
WHITE_ENGINE = "AB_TT_PVS"

# Maximale Suchtiefe für Alpha-Beta-Engines
MAX_DEPTH = 4

# Bedenkzeit pro Spieler in Sekunden
TIME_LIMIT = 120

# Soll das Board nach jedem Zug angezeigt werden?
SHOW_EVERY_MOVE = True

# ============================================================================


def get_engine_move(board, onTurn, agent, time_limit, max_depth=4):
    """
    Ruft die Suchfunktion des angegebenen Agenten auf.
    Gibt zurück: (best_move, used_time)
    """
    board = copy.deepcopy(board)
    
    if agent == 'AB':
        from src.models import alphaBeta
        best_move, _, used_time = alphaBeta.iterative_deepening(
            board, onTurn, time_limit, max_depth
        )
        
    elif agent == 'AB_TT':
        from src.models import alphaBetaWithTransposition
        best_move, _, used_time = alphaBetaWithTransposition.iterative_deepening(
            board, onTurn, time_limit, max_depth
        )
        
    elif agent == 'AB_TT_PVS':
        from src.models import alphaBetaWithPVS
        best_move, _, used_time = alphaBetaWithPVS.iterative_deepening(
            board, onTurn, time_limit, max_depth
        )
        
    elif agent == 'MCTS':
        from src.models import MCTS_UCT_PB
        mcts = MCTS_UCT_PB.MCTS()
        start_time = time.perf_counter()
        root = mcts.run(board, onTurn, number_simulations=1000)
        end_time = time.perf_counter()
        used_time = end_time - start_time
        
        # Besten Zug aus root.children holen
        best_move, _, _ = root.best_child()
        if best_move is None and root.children:
            best_move = max(root.children.items(), key=lambda item: item[1].visit_count)[0]
            
    else:
        raise ValueError(f"Unbekannter Agent: {agent}")
    
    return best_move, used_time





def print_move_info(move_number, player, agent, best_move, used_time, eval_count):
    """Gibt Informationen zu einem Zug aus."""
    print("\n" + "-" * 60)
    print(f"Zug {move_number}: {player} ({agent}) am Zug")
    print("-" * 60)
    
    if best_move is None:
        print("  ❌ Kein Zug gefunden!")
        return
    
    start_pos, goal_pos = best_move
    print(f"  Von: {start_pos}  →  Nach: {goal_pos}")
    print(f"  Zeit: {used_time:.3f}s")
    
    if agent.startswith("AB"):
        print(f"  Suchtiefe: {MAX_DEPTH}")
        print(f"  Eval-Aufrufe: {eval_count}")


def print_game_result(result, move_count, total_time):
    """Gibt das Spielergebnis aus."""
    print("\n" + "=" * 70)
    print("SPIEL BEENDET!")
    print("=" * 70)
    
    if result == 1:
        print("WEISS GEWINNT!")
    elif result == -1:
        print("SCHWARZ GEWINNT!")
    else:
        print("REMIS!")
    
    print(f"Anzahl Züge: {move_count}")
    print(f"Spieldauer: {total_time:.2f}s")
    print("=" * 70)


def play_match(black_agent, white_agent):
    """
    Führt einen Match zwischen zwei KI-Agenten durch.
    """
    # Board initialisieren
    board = copy.deepcopy(definitions.starting_board)
    config.reset_pieces()
    config.init_pieces(board)
    
    # Spielkopf ausgeben
    
    # Startboard anzeigen
    print("\nSTARTBOARD:")
    debug.print_board(board)
    print(f"Weiße Figuren: {config.W_pieces}, Schwarze Figuren: {config.B_pieces}, König: {config.K_pieces}")
    
    # Zeitlimits für beide Spieler
    time_white = TIME_LIMIT
    time_black = TIME_LIMIT
    
    # Spielvariablen
    current_player = "Black"
    move_count = 0
    max_moves = 500
    move_history = []
    
    start_time = time.perf_counter()
    
    while checkBoard.checkBoard(board) == -2 and move_count < max_moves:
        
        # Bestimme Agent und verbleibende Zeit
        if current_player == "Black":
            agent = black_agent
            time_left = time_black
        else:
            agent = white_agent
            time_left = time_white
        
        # Zug von der KI holen
        try:
            best_move, used_time = get_engine_move(
                board, current_player, agent, time_left, MAX_DEPTH
            )
        except Exception as e:
            print(f"FEHLER bei {agent}: {e}")
            import traceback
            traceback.print_exc()
            break
        
        # Zeit aktualisieren
        if current_player == "Black":
            time_black -= used_time
            if time_black <= 0:
                print("\nSchwarz hat keine Zeit mehr → Weiß gewinnt!")
                result = 1
                break
        else:
            time_white -= used_time
            if time_white <= 0:
                print("\nWeiß hat keine Zeit mehr → Schwarz gewinnt!")
                result = -1
                break
        
        # Zuginformationen ausgeben
        move_count += 1
        print_move_info(move_count, current_player, agent, best_move, used_time, config.eval_counter)
        
        # Falls kein Move gefunden wurde
        if best_move is None or best_move == ((), ()):
            print("Kein gültiger Zug gefunden! Spiel wird abgebrochen.")
            break
        
        # Board sichern (für Fehlererkennung)
        old_board = copy.deepcopy(board)
        
        # Zug ausführen
        makeMove.updateBoard(board, best_move)
        move_history.append((current_player, best_move))
        
        # Board nach dem Zug anzeigen
        if SHOW_EVERY_MOVE:
            print(f"\nBoard nach Zug {move_count}:")
            debug.print_board(board)
            print(f"  Figuren: Weiß={config.W_pieces}, Schwarz={config.B_pieces}, König={config.K_pieces}")
        
        # Prüfen ob sich etwas verändert hat
        if old_board == board:
            print("Fehler: Board hat sich nicht verändert!")
            break
        
        # Spieler wechseln
        current_player = "Black" if current_player == "White" else "White"
    
    # Spielende
    total_time = time.perf_counter() - start_time
    
    # Ergebnis ermitteln
    result = checkBoard.checkBoard(board)
    if result == -2:
        result = 0  # Abbruch ohne Sieger
    
    # Ergebnis ausgeben
    print_game_result(result, move_count, total_time)
    print("\nENDBOARD:")
    print("RESSSSS")
    print(checkBoard.checkBoard(board))
    debug.print_board(board)
    
    # Zusammenfassung
    print("\n" + "-" * 60)
    print("ZUSAMMENFASSUNG")
    print("-" * 60)
    print(f"Schwarz ({black_agent}): {time_black:.2f}s verbleibend")
    print(f"Weiß   ({white_agent}): {time_white:.2f}s verbleibend")
    print(f"Anzahl Eval-Aufrufe gesamt: {config.eval_counter}")
    print("-" * 60)
    
    return {
        "winner": "White" if result == 1 else "Black" if result == -1 else "Draw",
        "moves": move_count,
        "total_time": total_time,
        "history": move_history,
        "black_agent": black_agent,
        "white_agent": white_agent,
    }



if __name__ == "__main__":
    print("\n" + "=" * 70)
    print("TABLUT - KI-VERGLEICH")
    print("=" * 70)
    print(f"Konfiguration:")
    print(f"  Schwarz: {BLACK_ENGINE}")
    print(f"  Weiß:    {WHITE_ENGINE}")
    print(f"  Tiefe:   {MAX_DEPTH}")
    print(f"  Zeit:    {TIME_LIMIT}s")
    print("=" * 70)
    
    # Match starten
    result = play_match(BLACK_ENGINE, WHITE_ENGINE)
    
    # Sieger hervorheben
    print("\n" + "=" * 70)
    if result["winner"] == "White":
        print(f"🏆 GEWINNER: Weiß mit {WHITE_ENGINE}")
    elif result["winner"] == "Black":
        print(f"🏆 GEWINNER: Schwarz mit {BLACK_ENGINE}")
    else:
        print("🤝 REMIS!")
    print("=" * 70)