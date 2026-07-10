import numpy as np
import matplotlib.pyplot as plt

# Namen der Algorithmen
algorithms = [
    r'$\alpha\beta$',
    r'$\alpha\beta$ + TT',
    r'$\alpha\beta$ + TT + PVS',
    'MCTS'
]

# Gewinnrate der Zeilen-KI gegen die Spalten-KI
# (Beispielwerte)
data = np.array([
    [50, 34, 28, 18],
    [66, 50, 48, 36],
    [72, 52, 50, 42],
    [82, 64, 58, 50]
])

fig, ax = plt.subplots(figsize=(7,6))

# Heatmap
im = ax.imshow(data, cmap='RdYlGn', vmin=0, vmax=100)

# Achsen
ax.set_xticks(np.arange(len(algorithms)))
ax.set_yticks(np.arange(len(algorithms)))

ax.set_xticklabels(algorithms, fontsize=12)
ax.set_yticklabels(algorithms, fontsize=12)

plt.setp(ax.get_xticklabels(), rotation=25, ha="right")

# Zahlen in jede Zelle
for i in range(data.shape[0]):
    for j in range(data.shape[1]):
        ax.text(j, i,
                f"{data[i,j]}%",
                ha="center",
                va="center",
                color="black",
                fontsize=11,
                fontweight="bold")

# Titel
ax.set_title("Win Rate Matrix", fontsize=16, pad=20)

# Farbskala
cbar = plt.colorbar(im)
cbar.set_label("Winning Percentage [%]", fontsize=12)

plt.tight_layout()
plt.show()