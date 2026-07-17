import matplotlib.pyplot as plt
from .speedtest import run

"""
TODO: Werte ermitteln für Bericht
"""

# Boards 1–10
boards = list(range(1, 11))

# Zustände für die vier Verfahren
states_pvs = None
states_tt  = None
states_ab  = None

#result = run()

#states_ab = result[0]
#states_tt = result[1]
#states_pvs = result[2]
#states_mcts = result[3] #HIER

#print("RESULLLLLLTTTT")
#print(states_mcts)

# Zustände für die vier Verfahren (aus dem Log extrahiert)
states_ab = [50238, 19714, 47320, 128576, 445376, 564776, 599324, 529448, 594912, 592750]
states_tt = [1213, 2202, 2320, 4993, 5837, 15092, 21239, 9430, 7670, 38950]
states_pvs = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
states_mcts = [65430, 423404, 323610, 281736, 252658, 340929, 252238, 163376, 160406, 334007]

# Plot erstellen
plt.figure(figsize=(12, 6))

# Linie 1: PVS
plt.plot(boards, states_pvs, marker='o', linestyle='-', color='blue',
         linewidth=2, markersize=8, label='AlphaBeta + MO + TT + PVS')

# Linie 2: TT ohne PVS
plt.plot(boards, states_tt, marker='s', linestyle='-', color='red',
         linewidth=2, markersize=8, label='AlphaBeta + MO + TT')

# Linie 3: Basis-Alphabeta
plt.plot(boards, states_ab, marker='^', linestyle='-', color='green',
         linewidth=2, markersize=8, label='AlphaBeta (Basis)')

# Linie 4: MCTS
plt.plot(boards, states_mcts, marker='D', linestyle='-', color='orange',
         linewidth=2, markersize=8, label='MCTS + UCT + PB')

# Achsenbeschriftungen und Titel
plt.xlabel('Board‑Komplexität (1 = einfach → 10 = komplex)', fontsize=12)
plt.ylabel('Evaluierte Zustände', fontsize=12)
plt.title('Vergleich der evaluierten Zustände von vier KI-Modellen', fontsize=14)

# Gitter
plt.grid(True, linestyle='--', alpha=0.7)

# Achsenbereich
all_states = [s for s in [states_pvs, states_tt, states_ab, states_mcts] if s is not None]
if all_states:
    max_state = max(max(s) for s in all_states)
    plt.ylim(0, max_state + 50000)

plt.xticks(boards)
plt.legend(loc='upper left')
plt.tight_layout()
plt.show()