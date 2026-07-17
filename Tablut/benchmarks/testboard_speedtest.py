def create_empty_board():
    return [[0 for _ in range(9)] for _ in range(9)]

def place(board, row, col, piece):
    if 0 <= row < 9 and 0 <= col < 9:
        board[row][col] = piece

# ---------- 10 Boards (Komplexität von 1 bis 10) ----------
all_boards = []

# Board 1: König (4,4), eine weiße Figur bei (4,3) – König kann nach (4,5) ziehen und gewinnen (sofern Regel)
board1 = create_empty_board()
place(board1, 4, 0, 'K')
place(board1, 4, 3, 'W')
place(board1, 2, 1, 'W')
place(board1, 5, 3, 'B')
place(board1, 6, 0, 'B')
place(board1, 5, 3, 'B')

# Keine schwarzen Figuren
all_boards.append(board1)

# Board 2: Zwei weiße, eine schwarze Figur – König muss einen Zug planen
board2 = create_empty_board()
place(board2, 4, 4, 'K')
place(board2, 4, 3, 'W')
place(board2, 3, 4, 'W')
place(board2, 4, 5, 'B')   # blockiert eine Flucht
all_boards.append(board2)

# Board 3: Drei weiße, zwei schwarze – erste richtige Verteidigung
board3 = create_empty_board()
place(board3, 4, 4, 'K')
place(board3, 3, 4, 'W')
place(board3, 5, 4, 'W')
place(board3, 4, 3, 'W')
place(board3, 4, 5, 'B')
place(board3, 2, 4, 'B')
all_boards.append(board3)

# Board 4: Vier weiße, vier schwarze – verteilt
board4 = create_empty_board()
place(board4, 4, 4, 'K')
place(board4, 3, 3, 'W')
place(board4, 3, 5, 'W')
place(board4, 5, 3, 'W')
place(board4, 5, 5, 'W')
place(board4, 2, 4, 'B')
place(board4, 4, 2, 'B')
place(board4, 6, 4, 'B')
place(board4, 4, 6, 'B')
all_boards.append(board4)

# Board 5: Acht weiße, acht schwarze – dichter Kampf
board5 = create_empty_board()
place(board5, 4, 4, 'K')
for row in [2, 3, 5, 6]:
    place(board5, row, 4, 'W')
    place(board5, 4, row, 'W')   # symmetrisch
place(board5, 1, 4, 'B')
place(board5, 7, 4, 'B')
place(board5, 4, 1, 'B')
place(board5, 4, 7, 'B')
place(board5, 0, 3, 'B')
place(board5, 0, 5, 'B')
place(board5, 8, 3, 'B')
place(board5, 8, 5, 'B')
all_boards.append(board5)

# Board 6: Sechs weiße, sechs schwarze – unregelmäßige Verteilung
board6 = create_empty_board()
place(board6, 4, 4, 'K')
place(board6, 6, 4, 'W')
place(board6, 3, 2, 'W')
place(board6, 2, 3, 'W')
place(board6, 2, 5, 'W')
place(board6, 3, 6, 'W')
place(board6, 5, 2, 'W')
place(board6, 6, 3, 'W')
place(board6, 1, 4, 'B')
place(board6, 4, 1, 'B')
place(board6, 7, 4, 'B')
place(board6, 4, 7, 'B')
place(board6, 0, 4, 'B')
place(board6, 4, 0, 'B')
all_boards.append(board6)


# Board 7: Acht weiße, zehn schwarze – asymmetrisch, viele am Rand
board7 = create_empty_board()
place(board7, 4, 4, 'K')
# weiße
place(board7, 2, 4, 'W')
place(board7, 3, 3, 'W')
place(board7, 3, 5, 'W')
place(board7, 5, 3, 'W')
place(board7, 5, 5, 'W')
place(board7, 6, 4, 'W')
place(board7, 4, 2, 'W')
place(board7, 4, 6, 'W')
# schwarze – unregelmäßig
place(board7, 1, 2, 'B')
place(board7, 1, 6, 'B')
place(board7, 2, 1, 'B')
place(board7, 2, 7, 'B')
place(board7, 6, 1, 'B')
place(board7, 6, 7, 'B')
place(board7, 7, 2, 'B')
place(board7, 7, 6, 'B')
place(board7, 0, 4, 'B')
place(board7, 8, 4, 'B')
all_boards.append(board7)

# Board 8: Acht weiße, zwölf schwarze – fast volles Layout, aber andere Verteilung
board8 = create_empty_board()
place(board8, 4, 4, 'K')
# weiße – in zwei diagonalen Linien
place(board8, 3, 3, 'W')
place(board8, 3, 5, 'W')
place(board8, 5, 3, 'W')
place(board8, 5, 5, 'W')
place(board8, 2, 4, 'W')
place(board8, 6, 4, 'W')
place(board8, 4, 2, 'W')
place(board8, 4, 6, 'W')
# schwarze – viele auf den äußeren Ringen
for col in [2, 3, 5, 6]:
    place(board8, 0, col, 'B')
    place(board8, 8, col, 'B')
    place(board8, col, 0, 'B')
    place(board8, col, 8, 'B')
# zusätzliche schwarze auf (1,4) und (7,4)
place(board8, 1, 4, 'B')
place(board8, 7, 4, 'B')
all_boards.append(board8)

# Board 9: Acht weiße, vierzehn schwarze – dicht, aber mit Lücken
board9 = create_empty_board()
place(board9, 4, 4, 'K')
# weiße – unregelmäßig um den König
place(board9, 3, 2, 'W')
place(board9, 2, 4, 'W')
place(board9, 3, 6, 'W')
place(board9, 5, 2, 'W')
place(board9, 6, 4, 'W')
place(board9, 5, 6, 'W')
place(board9, 4, 3, 'W')
place(board9, 4, 5, 'W')
# schwarze – fast alle Rand- und Diagonalpositionen
for col in [2, 3, 5, 6]:
    place(board9, 0, col, 'B')
    place(board9, 8, col, 'B')
    place(board9, col, 0, 'B')
    place(board9, col, 8, 'B')
place(board9, 1, 4, 'B')
place(board9, 7, 4, 'B')
place(board9, 4, 1, 'B')
place(board9, 4, 7, 'B')
all_boards.append(board9)

# Board 10: Acht weiße, sechzehn schwarze – maximal, aber anders verteilt
board10 = create_empty_board()
place(board10, 4, 4, 'K')
# weiße – alle vier Diagonalen und Seiten‚
place(board10, 3, 3, 'W')
place(board10, 3, 5, 'W')

place(board10, 5, 5, 'W') 
place(board10, 8, 4, 'W') 
place(board10, 2, 4, 'W')

place(board10, 4, 2, 'W')
place(board10, 4, 6, 'W')
# schwarze – komplette Besetzung der äußeren zwei Ringe (außer Ecken)
for r in [0,  7]:
    for c in [2, 3]:
        place(board10, r, c, 'B')
for r in [ 3, 6]:
    for c in [ 7, 8]:
        place(board10, r, c, 'B')
# zusätzlich die verbleibenden Felder, um auf 16 zu kommen:
place(board10, 1, 4, 'B')

place(board10, 4, 1, 'B')

# Nun sind es genau 16 (man zählt nach)
all_boards.append(board10)

# Jetzt enthält all_boards 10 Boards mit steigender Komplexität.