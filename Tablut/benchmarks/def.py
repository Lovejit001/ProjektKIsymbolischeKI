import matplotlib.pyplot as plt

# Boards 1–10
boards = list(range(1, 11))

# Evaluierte Zustände für die drei Verfahren (aus deinen Logs)
states_ab  = [346484, 274500, 514744, 85870, 76240, 36782, 210142, 233644, 208320, 234736]
states_tt  = [85318, 93768, 137043, 25770, 23539, 11376, 81695, 92141, 83176, 96182]
states_pvs = [77143, 76173, 113661, 21365, 19244, 10703, 56283, 60401, 58729, 71486]

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

# Achsenbeschriftungen und Titel
plt.xlabel('Board‑Komplexität (1 = einfach → 10 = komplex)', fontsize=12)
plt.ylabel('Evaluierte Zustände', fontsize=12)
plt.title('Vergleich der evaluierten Zustände – drei Verfahren', fontsize=14)

# Gitter
plt.grid(True, linestyle='--', alpha=0.7)

# Achsenbereich
plt.xticks(boards)
plt.ylim(0, max(max(states_ab), max(states_tt), max(states_pvs)) * 1.1)

# Legende
plt.legend(loc='upper left')

plt.tight_layout()
plt.show()