import matplotlib.pyplot as plt
from .compare2 import run

"""
aktuelle file um grafik zu erstellen !"""

# Boards 1–10
boards = list(range(1, 11))

# Zeiten für die drei Verfahren
times_pvs = None
times_tt  = None
times_ab  = None

result = run()

times_ab = result[0]
times_tt = result[1]
times_pvs = result[2]
times_mcts = result[3] #HIER


print("RESULLLLLLTTTT")
print(times_mcts)

times_pvs = [13.777, 11.405, 14.840, 6.416, 5.522, 4.393, 15.548, 16.827, 16.499, 19.948]
times_tt  = [13.876, 13.480, 16.488, 8.145, 7.271, 4.456, 23.391, 27.489, 24.846, 28.474]
#times_ab  = [11.432, 9.699, 17.329, 3.973, 3.498, 1.887, 10.435, 11.726, 10.757, 12.293]

# Plot erstellen
plt.figure(figsize=(12, 6))

# Linie 1: PVS
plt.plot(boards, times_pvs, marker='o', linestyle='-', color='blue',
         linewidth=2, markersize=8, label='AlphaBeta + MO + TT + PVS')

# Linie 2: TT ohne PVS
plt.plot(boards, times_tt, marker='s', linestyle='-', color='red',
         linewidth=2, markersize=8, label='AlphaBeta + MO + TT')

# Linie 3: Basis-Alphabeta
plt.plot(boards, times_ab, marker='^', linestyle='-', color='green',
         linewidth=2, markersize=8, label='AlphaBeta (Basis)')

# Linie 4: MCTS (neu)
plt.plot(boards, times_mcts, marker='D', linestyle='-', color='orange',
         linewidth=2, markersize=8, label='MCTS + UCT + PB')

# Achsenbeschriftungen und Titel
plt.xlabel('Board‑Komplexität (1 = einfach → 10 = komplex)', fontsize=12)
plt.ylabel('Suchzeit (Sekunden)', fontsize=12)
plt.title('Vergleich der Suchzeiten – drei Verfahren', fontsize=14)


# Gitter
plt.grid(True, linestyle='--', alpha=0.7)

# Optional: Werte über den Punkten anzeigen (auskommentiert, um Übersichtlichkeit zu wahren)
# for i, t in enumerate(times_pvs):
#     plt.text(boards[i], t + 0.5, f'{t:.1f}', ha='center', fontsize=7, color='blue')
# for i, t in enumerate(times_tt):
#     plt.text(boards[i], t + 0.5, f'{t:.1f}', ha='center', fontsize=7, color='red')
# for i, t in enumerate(times_ab):
#     plt.text(boards[i], t + 0.5, f'{t:.1f}', ha='center', fontsize=7, color='green')


# Achsenbereich (MCTS mit einbeziehen)
all_times = [t for t in [times_pvs, times_tt, times_ab, times_mcts] if t is not None]
if all_times:
    max_time = max(max(t) for t in all_times)
    plt.ylim(0, max_time + 3)

plt.xticks(boards)
plt.legend(loc='upper left')
plt.tight_layout()
plt.show()