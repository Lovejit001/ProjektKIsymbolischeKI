# all_testboards.py
# 100 verschiedene Tablut-Boards (50 aus testboards3.py + 50 aus testboards4.py)
# B = Schwarz, W = Weiß, K = König, 0 = leeres Feld

B = 'B'
W = 'W'
K = 'K'

def create_empty_board():
    """Erstellt ein leeres 9x9 Board"""
    return [[0 for _ in range(9)] for _ in range(9)]

def is_valid_position(row, col):
    """Prüft ob eine Position gültig ist (kein Eckfeld)"""
    if (row == 0 and col == 0) or (row == 0 and col == 8) or \
       (row == 8 and col == 0) or (row == 8 and col == 8):
        return False
    return True

def place_piece(board, row, col, piece):
    """Platziert eine Figur nur wenn Position gültig ist"""
    if is_valid_position(row, col):
        board[row][col] = piece
        return True
    return False

all_boards = []

# ============================================================
# TESTBOARDS3.PY - BOARDS 1-50
# ============================================================

# ============================================================
# KATEGORIE 1: STARTNAHE STELLUNGEN (Boards 1-10) - VIELE FIGUREN
# ============================================================

# BOARD 1: Offizielle Startstellung (16 Schwarz, 8 Weiß + König)
board1 = create_empty_board()
board1[4][4] = K
for f in [2, 3, 5, 6]:
    board1[4][f] = W
    board1[f][4] = W
for f in [3, 4, 5]:
    board1[0][f] = B
    board1[8][f] = B
    board1[f][0] = B
    board1[f][8] = B
board1[1][4] = B
board1[7][4] = B
board1[4][1] = B
board1[4][7] = B
all_boards.append(board1)

# BOARD 2: Erste Züge - Schwarz dringt ein, Weiß formiert sich
board2 = create_empty_board()
board2[4][4] = K
for f in [2, 3, 5, 6]:
    board2[4][f] = W
    board2[f][4] = W
board2[0][3] = B
board2[0][4] = B
board2[0][5] = B
board2[2][0] = B
board2[3][0] = B
board2[4][0] = B
board2[5][0] = B
board2[8][3] = B
board2[8][4] = B
board2[8][5] = B
board2[0][8] = 0
board2[8][8] = 0
board2[1][3] = B
board2[7][5] = B
all_boards.append(board2)

# BOARD 3: Weiß hat Thron verlassen, breite Verteilung
board3 = create_empty_board()
board3[4][3] = K
board3[4][4] = 0
board3[3][3] = W
board3[5][3] = W
board3[4][5] = W
board3[2][4] = W
board3[6][4] = W
board3[3][5] = W
board3[5][5] = W
board3[0][3] = B
board3[0][4] = B
board3[0][5] = B
board3[1][4] = B
board3[2][2] = B
board3[2][6] = B
board3[3][7] = B
board3[4][2] = B
board3[4][6] = B
board3[5][7] = B
board3[6][2] = B
board3[7][4] = B
board3[8][3] = B
board3[8][4] = B
board3[8][5] = B
all_boards.append(board3)

# BOARD 4: Offene Stellung - viele Figuren über Brett verteilt
board4 = create_empty_board()
board4[5][4] = K
board4[3][3] = W
board4[3][5] = W
board4[4][5] = W
board4[5][3] = W
board4[6][4] = W
board4[2][4] = W
board4[4][2] = W
board4[0][2] = B
board4[0][6] = B
board4[1][4] = B
board4[2][6] = B
board4[3][7] = B
board4[4][6] = B
board4[5][7] = B
board4[6][2] = B
board4[6][6] = B
board4[7][3] = B
board4[7][5] = B
board4[8][2] = B
board4[8][6] = B
all_boards.append(board4)

# BOARD 5: Ausgebreitete Stellung - viele Optionen
board5 = create_empty_board()
board5[4][4] = K
board5[2][3] = W
board5[2][5] = W
board5[3][2] = W
board5[3][4] = W
board5[4][3] = W
board5[4][5] = W
board5[5][4] = W
board5[6][3] = W
board5[6][5] = W
board5[0][2] = B
board5[0][4] = B
board5[0][6] = B
board5[1][5] = B
board5[2][7] = B
board5[3][6] = B
board5[5][2] = B
board5[5][6] = B
board5[6][7] = B
board5[7][2] = B
board5[7][4] = B
board5[7][6] = B
board5[8][3] = B
board5[8][5] = B
all_boards.append(board5)

# BOARD 6: Kompaktes Zentrum mit vielen Figuren
board6 = create_empty_board()
board6[4][4] = K
board6[3][3] = W
board6[3][4] = W
board6[3][5] = W
board6[4][3] = W
board6[4][5] = W
board6[5][3] = W
board6[5][4] = W
board6[5][5] = W
board6[2][4] = B
board6[4][2] = B
board6[4][6] = B
board6[6][4] = B
board6[1][3] = B
board6[3][1] = B
board6[5][7] = B
board6[7][5] = B
board6[0][4] = B
board6[4][0] = B
board6[4][8] = B
board6[8][4] = B
all_boards.append(board6)

# BOARD 7: Dynamische Eröffnung - Figuren im Vormarsch
board7 = create_empty_board()
board7[4][3] = K
board7[3][3] = W
board7[3][4] = W
board7[4][5] = W
board7[5][3] = W
board7[2][3] = W
board7[4][2] = W
board7[0][3] = B
board7[0][5] = B
board7[1][4] = B
board7[2][5] = B
board7[3][6] = B
board7[4][6] = B
board7[5][5] = B
board7[6][4] = B
board7[7][3] = B
board7[8][4] = B
board7[8][6] = B
all_boards.append(board7)

# BOARD 8: Ausgeglichene Startphase mit vielen Figuren
board8 = create_empty_board()
board8[4][4] = K
board8[3][3] = W
board8[3][5] = W
board8[4][3] = W
board8[4][5] = W
board8[5][3] = W
board8[5][5] = W
board8[2][4] = W
board8[6][4] = W
board8[0][2] = B
board8[0][4] = B
board8[0][6] = B
board8[1][3] = B
board8[1][5] = B
board8[2][6] = B
board8[3][7] = B
board8[5][7] = B
board8[6][2] = B
board8[7][3] = B
board8[7][5] = B
board8[8][2] = B
board8[8][4] = B
board8[8][6] = B
all_boards.append(board8)

# BOARD 9: Weite Verteilung - viel Bewegung möglich
board9 = create_empty_board()
board9[3][4] = K
board9[2][3] = W
board9[2][5] = W
board9[3][2] = W
board9[3][6] = W
board9[4][3] = W
board9[4][5] = W
board9[5][4] = W
board9[6][3] = W
board9[6][5] = W
board9[0][3] = B
board9[0][5] = B
board9[1][2] = B
board9[1][6] = B
board9[2][7] = B
board9[4][7] = B
board9[5][2] = B
board9[5][6] = B
board9[7][2] = B
board9[7][6] = B
board9[8][3] = B
board9[8][5] = B
all_boards.append(board9)

# BOARD 10: Volles Brett - viele Interaktionen
board10 = create_empty_board()
board10[4][4] = K
board10[2][2] = W
board10[2][4] = W
board10[2][6] = W
board10[3][3] = W
board10[3][5] = W
board10[4][2] = W
board10[4][6] = W
board10[5][3] = W
board10[5][5] = W
board10[6][2] = W
board10[6][4] = W
board10[6][6] = W
board10[0][2] = B
board10[0][4] = B
board10[0][6] = B
board10[1][3] = B
board10[1][5] = B
board10[2][3] = B
board10[2][5] = B
board10[3][2] = B
board10[3][6] = B
board10[5][2] = B
board10[5][6] = B
board10[6][3] = B
board10[6][5] = B
board10[7][4] = B
board10[8][3] = B
board10[8][5] = B
all_boards.append(board10)

# ============================================================
# KATEGORIE 2: AUSGEGLICHENE MITTELSPIEL (Boards 11-20)
# ============================================================

# BOARD 11: Ausgeglichenes Mittelspiel - viele Figuren
board11 = create_empty_board()
board11[4][3] = K
board11[3][3] = W
board11[3][4] = W
board11[3][5] = W
board11[4][5] = W
board11[5][3] = W
board11[5][4] = W
board11[5][5] = W
board11[2][4] = B
board11[4][2] = B
board11[4][6] = B
board11[6][4] = B
board11[1][3] = B
board11[1][5] = B
board11[3][7] = B
board11[5][7] = B
board11[7][3] = B
board11[7][5] = B
all_boards.append(board11)

# BOARD 12: Offene Mitte - viele Figuren verteilt
board12 = create_empty_board()
board12[5][5] = K
board12[3][3] = W
board12[3][5] = W
board12[4][4] = W
board12[4][6] = W
board12[5][3] = W
board12[5][7] = W
board12[6][4] = W
board12[6][6] = W
board12[1][4] = B
board12[2][3] = B
board12[2][5] = B
board12[3][6] = B
board12[4][2] = B
board12[4][7] = B
board12[6][3] = B
board12[6][7] = B
board12[7][4] = B
board12[8][4] = B
all_boards.append(board12)

# BOARD 13: Dynamisches Mittelspiel
board13 = create_empty_board()
board13[3][4] = K
board13[2][3] = W
board13[2][4] = W
board13[2][5] = W
board13[3][3] = W
board13[4][4] = W
board13[4][5] = W
board13[5][4] = W
board13[1][3] = B
board13[1][5] = B
board13[2][6] = B
board13[3][6] = B
board13[4][2] = B
board13[5][3] = B
board13[5][5] = B
board13[6][4] = B
board13[7][4] = B
board13[8][3] = B
board13[8][5] = B
all_boards.append(board13)

# BOARD 14: Komplexe Stellung mit vielen Optionen
board14 = create_empty_board()
board14[4][5] = K
board14[3][3] = W
board14[3][5] = W
board14[4][3] = W
board14[4][4] = W
board14[5][3] = W
board14[5][5] = W
board14[5][6] = W
board14[6][5] = W
board14[2][4] = B
board14[2][6] = B
board14[3][7] = B
board14[4][2] = B
board14[4][7] = B
board14[5][7] = B
board14[6][3] = B
board14[6][6] = B
board14[7][4] = B
board14[8][4] = B
all_boards.append(board14)

# BOARD 15: Ausgeglichenes Kräftemessen
board15 = create_empty_board()
board15[5][4] = K
board15[3][3] = W
board15[3][4] = W
board15[3][5] = W
board15[4][3] = W
board15[4][5] = W
board15[5][3] = W
board15[5][5] = W
board15[6][4] = W
board15[2][3] = B
board15[2][5] = B
board15[3][6] = B
board15[4][2] = B
board15[4][6] = B
board15[5][7] = B
board15[6][3] = B
board15[6][5] = B
board15[7][4] = B
all_boards.append(board15)

# BOARD 16: Offene Flanken - viel Bewegung
board16 = create_empty_board()
board16[3][3] = K
board16[2][2] = W
board16[2][4] = W
board16[3][5] = W
board16[4][3] = W
board16[4][4] = W
board16[5][3] = W
board16[5][5] = W
board16[6][4] = W
board16[1][3] = B
board16[1][5] = B
board16[2][6] = B
board16[3][6] = B
board16[4][2] = B
board16[4][6] = B
board16[5][7] = B
board16[6][3] = B
board16[6][5] = B
board16[7][4] = B
board16[8][3] = B
all_boards.append(board16)

# BOARD 17: Vielseitige Stellung
board17 = create_empty_board()
board17[4][3] = K
board17[3][2] = W
board17[3][4] = W
board17[4][5] = W
board17[5][2] = W
board17[5][4] = W
board17[6][3] = W
board17[6][5] = W
board17[2][3] = B
board17[2][5] = B
board17[3][6] = B
board17[4][2] = B
board17[4][7] = B
board17[5][6] = B
board17[6][4] = B
board17[7][3] = B
board17[7][5] = B
board17[8][4] = B
all_boards.append(board17)

# BOARD 18: Ausgewogene Verteilung
board18 = create_empty_board()
board18[4][4] = K
board18[2][3] = W
board18[2][5] = W
board18[3][2] = W
board18[3][4] = W
board18[3][6] = W
board18[4][3] = W
board18[4][5] = W
board18[5][4] = W
board18[6][3] = W
board18[6][5] = W
board18[1][4] = B
board18[2][6] = B
board18[3][7] = B
board18[4][2] = B
board18[4][7] = B
board18[5][6] = B
board18[6][2] = B
board18[7][4] = B
board18[8][4] = B
all_boards.append(board18)

# BOARD 19: Kompaktes Mittelspiel
board19 = create_empty_board()
board19[3][4] = K
board19[2][3] = W
board19[2][5] = W
board19[3][3] = W
board19[3][5] = W
board19[4][3] = W
board19[4][5] = W
board19[5][4] = W
board19[1][3] = B
board19[1][5] = B
board19[2][6] = B
board19[3][6] = B
board19[4][2] = B
board19[4][7] = B
board19[5][5] = B
board19[6][3] = B
board19[6][5] = B
board19[7][4] = B
all_boards.append(board19)

# BOARD 20: Breit gefächerte Stellung
board20 = create_empty_board()
board20[5][3] = K
board20[3][3] = W
board20[3][5] = W
board20[4][4] = W
board20[4][6] = W
board20[5][4] = W
board20[5][6] = W
board20[6][3] = W
board20[6][5] = W
board20[2][4] = B
board20[2][6] = B
board20[3][7] = B
board20[4][2] = B
board20[4][7] = B
board20[5][7] = B
board20[6][2] = B
board20[7][4] = B
board20[7][6] = B
board20[8][4] = B
all_boards.append(board20)

# ============================================================
# KATEGORIE 3: SCHWARZ IM VORTEIL (Boards 21-30)
# ============================================================

# BOARD 21: Schwarz kontrolliert die Mitte
board21 = create_empty_board()
board21[4][4] = K
board21[3][4] = W
board21[4][3] = W
board21[4][5] = W
board21[5][4] = W
board21[2][4] = B
board21[4][2] = B
board21[4][6] = B
board21[6][4] = B
board21[1][3] = B
board21[1][5] = B
board21[3][6] = B
board21[5][6] = B
board21[7][4] = B
board21[8][3] = B
board21[8][5] = B
all_boards.append(board21)

# BOARD 22: Schwarze Übermacht im Zentrum
board22 = create_empty_board()
board22[3][3] = K
board22[2][3] = W
board22[3][4] = W
board22[3][2] = W
board22[4][3] = W
board22[1][3] = B
board22[2][2] = B
board22[2][4] = B
board22[3][5] = B
board22[4][2] = B
board22[4][4] = B
board22[5][3] = B
board22[5][5] = B
board22[6][4] = B
board22[7][3] = B
board22[8][3] = B
all_boards.append(board22)

# BOARD 23: König bedrängt, wenig Verteidiger
board23 = create_empty_board()
board23[4][4] = K
board23[3][4] = B
board23[5][4] = B
board23[4][3] = B
board23[4][5] = B
board23[2][4] = B
board23[4][2] = B
board23[4][6] = B
board23[6][4] = B
board23[3][3] = W
board23[3][5] = W
board23[5][3] = W
all_boards.append(board23)

# BOARD 24: König auf der Flucht - schwarze Verfolgung
board24 = create_empty_board()
board24[2][2] = K
board24[2][3] = W
board24[3][2] = W
board24[3][3] = W
board24[1][2] = B
board24[2][1] = B
board24[2][4] = B
board24[4][2] = B
board24[3][4] = B
board24[1][4] = B
board24[4][3] = B
board24[5][2] = B
board24[2][5] = B
all_boards.append(board24)

# BOARD 25: Eingekesselter König
board25 = create_empty_board()
board25[4][3] = K
board25[3][3] = B
board25[5][3] = B
board25[4][2] = B
board25[4][4] = B
board25[2][3] = B
board25[6][3] = B
board25[3][4] = W
board25[5][4] = W
board25[4][5] = W
board25[3][5] = W
all_boards.append(board25)

# BOARD 26: Schwarze Dominanz
board26 = create_empty_board()
board26[5][4] = K
board26[4][4] = W
board26[5][3] = W
board26[5][5] = W
board26[6][4] = W
board26[3][4] = B
board26[5][2] = B
board26[5][6] = B
board26[4][3] = B
board26[4][5] = B
board26[6][3] = B
board26[6][5] = B
board26[7][4] = B
board26[8][4] = B
all_boards.append(board26)

# BOARD 27: König isoliert - viele Angreifer
board27 = create_empty_board()
board27[4][2] = K
board27[3][2] = B
board27[5][2] = B
board27[4][1] = B
board27[4][3] = B
board27[2][2] = B
board27[6][2] = B
board27[3][3] = W
board27[5][3] = W
board27[4][4] = W
board27[3][4] = W
board27[5][4] = W
all_boards.append(board27)

# BOARD 28: Materialüberlegenheit Schwarz
board28 = create_empty_board()
board28[3][4] = K
board28[2][3] = W
board28[3][3] = W
board28[3][5] = W
board28[4][4] = W
board28[1][4] = B
board28[2][5] = B
board28[3][6] = B
board28[4][3] = B
board28[4][5] = B
board28[5][4] = B
board28[5][5] = B
board28[6][3] = B
board28[6][4] = B
board28[7][4] = B
board28[8][4] = B
all_boards.append(board28)

# BOARD 29: Thron umzingelt - wenig Verteidiger
board29 = create_empty_board()
board29[4][4] = K
board29[3][4] = B
board29[5][4] = B
board29[4][3] = B
board29[4][5] = B
board29[2][4] = B
board29[6][4] = B
board29[4][2] = B
board29[4][6] = B
board29[3][3] = W
board29[5][5] = W
all_boards.append(board29)

# BOARD 30: Schwere Bedrängnis
board30 = create_empty_board()
board30[4][5] = K
board30[3][5] = B
board30[5][5] = B
board30[4][4] = B
board30[4][6] = B
board30[2][5] = B
board30[6][5] = B
board30[3][4] = W
board30[5][4] = W
board30[4][3] = W
board30[4][7] = W
board30[5][6] = W
all_boards.append(board30)

# ============================================================
# KATEGORIE 4: WEISS IM VORTEIL (Boards 31-40)
# ============================================================

# BOARD 31: Weiße Verteidigungsfestung
board31 = create_empty_board()
board31[4][4] = K
board31[3][3] = W
board31[3][4] = W
board31[3][5] = W
board31[4][3] = W
board31[4][5] = W
board31[5][3] = W
board31[5][4] = W
board31[5][5] = W
board31[2][4] = W
board31[6][4] = W
board31[1][4] = B
board31[4][2] = B
board31[4][6] = B
board31[7][4] = B
all_boards.append(board31)

# BOARD 32: König auf dem Weg zur Ecke
board32 = create_empty_board()
board32[2][2] = K
board32[2][3] = W
board32[3][2] = W
board32[2][1] = W
board32[1][2] = W
board32[3][3] = W
board32[4][2] = W
board32[2][4] = W
board32[1][3] = B
board32[2][5] = B
board32[3][4] = B
board32[4][3] = B
board32[5][2] = B
board32[2][6] = B
all_boards.append(board32)

# BOARD 33: Weiße Übermacht im Zentrum
board33 = create_empty_board()
board33[3][4] = K
board33[2][3] = W
board33[2][4] = W
board33[2][5] = W
board33[3][3] = W
board33[3][5] = W
board33[4][3] = W
board33[4][4] = W
board33[4][5] = W
board33[5][4] = W
board33[1][4] = W
board33[3][6] = W
board33[4][6] = B
board33[5][5] = B
board33[6][4] = B
board33[7][4] = B
all_boards.append(board33)

# BOARD 34: König mit starker Eskorte
board34 = create_empty_board()
board34[6][2] = K
board34[6][3] = W
board34[5][2] = W
board34[7][2] = W
board34[6][1] = W
board34[5][3] = W
board34[6][4] = W
board34[7][3] = W
board34[4][2] = W
board34[4][3] = B
board34[6][5] = B
board34[5][4] = B
board34[7][4] = B
board34[8][3] = B
board34[6][6] = B
all_boards.append(board34)

# BOARD 35: Weiß kontrolliert die Flanken
board35 = create_empty_board()
board35[2][4] = K
board35[1][3] = W
board35[1][4] = W
board35[1][5] = W
board35[2][3] = W
board35[2][5] = W
board35[3][3] = W
board35[3][4] = W
board35[3][5] = W
board35[0][4] = W
board35[2][2] = W
board35[2][6] = W
board35[4][4] = B
board35[2][7] = B
board35[3][6] = B
board35[4][3] = B
board35[5][4] = B
all_boards.append(board35)

# BOARD 36: König kurz vor der Ecke - stark geschützt
board36 = create_empty_board()
board36[0][2] = K
board36[0][1] = W
board36[0][3] = W
board36[1][1] = W
board36[1][2] = W
board36[1][3] = W
board36[2][1] = W
board36[2][2] = W
board36[2][3] = W
board36[0][0] = 0
board36[0][4] = B
board36[1][4] = B
board36[3][2] = B
board36[2][4] = B
all_boards.append(board36)

# BOARD 37: Weiße Materialüberlegenheit
board37 = create_empty_board()
board37[4][3] = K
board37[3][3] = W
board37[3][4] = W
board37[3][5] = W
board37[4][2] = W
board37[4][4] = W
board37[4][5] = W
board37[5][3] = W
board37[5][4] = W
board37[5][5] = W
board37[2][3] = B
board37[4][6] = B
board37[6][4] = B
board37[7][3] = B
board37[8][4] = B
all_boards.append(board37)

# BOARD 38: Weiße Dominanz in der Mitte
board38 = create_empty_board()
board38[4][4] = K
board38[3][3] = W
board38[3][4] = W
board38[3][5] = W
board38[4][3] = W
board38[4][5] = W
board38[5][3] = W
board38[5][4] = W
board38[5][5] = W
board38[2][4] = W
board38[6][4] = W
board38[1][4] = B
board38[4][2] = B
board38[4][6] = B
board38[7][4] = B
board38[8][4] = B
all_boards.append(board38)

# ============================================================
# KATEGORIE 5: ENDSPIEL-STELLUNGEN (Boards 39-50)
# ============================================================

# BOARD 39: Wenige Figuren, offene Stellung
board39 = create_empty_board()
board39[4][3] = K
board39[3][3] = W
board39[5][3] = W
board39[2][4] = B
board39[6][4] = B
board39[4][2] = B
all_boards.append(board39)

# BOARD 40: König mit zwei Verteidigern
board40 = create_empty_board()
board40[2][2] = K
board40[2][3] = W
board40[3][2] = W
board40[1][2] = B
board40[2][1] = B
board40[4][2] = B
all_boards.append(board40)

# BOARD 41: Letzte Verteidigung
board41 = create_empty_board()
board41[5][4] = K
board41[5][3] = W
board41[4][4] = W
board41[5][5] = W
board41[6][4] = B
board41[4][3] = B
board41[5][6] = B
all_boards.append(board41)

# BOARD 42: 1-gegen-1 Kampf um die Ecke
board42 = create_empty_board()
board42[0][2] = K
board42[0][1] = W
board42[0][3] = B
board42[1][2] = B
all_boards.append(board42)

# BOARD 43: König am Rand, wenige Figuren
board43 = create_empty_board()
board43[0][3] = K
board43[0][2] = W
board43[0][4] = W
board43[1][3] = B
board43[1][2] = B
all_boards.append(board43)

# BOARD 44: Zwei gegen zwei
board44 = create_empty_board()
board44[4][2] = K
board44[4][3] = W
board44[4][1] = B
board44[3][2] = B
board44[5][2] = W
all_boards.append(board44)

# BOARD 45: König in der Mitte, allein
board45 = create_empty_board()
board45[4][4] = K
board45[3][4] = B
board45[5][4] = B
board45[4][3] = B
board45[4][5] = W
all_boards.append(board45)

# BOARD 46: Kritische Endspiel-Stellung
board46 = create_empty_board()
board46[3][3] = K
board46[3][2] = W
board46[3][4] = B
board46[2][3] = B
board46[4][3] = B
board46[5][3] = W
all_boards.append(board46)

# BOARD 47: König auf der Flucht
board47 = create_empty_board()
board47[2][3] = K
board47[2][4] = W
board47[2][2] = B
board47[3][3] = B
board47[1][3] = B
board47[4][3] = W
all_boards.append(board47)

# BOARD 48: Minimalistische Endspiel-Stellung
board48 = create_empty_board()
board48[5][3] = K
board48[5][4] = W
board48[4][3] = B
board48[6][3] = B
board48[5][2] = W
all_boards.append(board48)

# BOARD 49: Kampf um die letzte Ecke
board49 = create_empty_board()
board49[0][2] = K
board49[0][1] = W
board49[0][3] = B
board49[1][2] = B
board49[1][1] = W
all_boards.append(board49)

# BOARD 50: Entscheidende Endspiel-Situation
board50 = create_empty_board()
board50[0][1] = K
board50[0][2] = W
board50[1][1] = B
board50[0][0] = 0
board50[1][2] = B
all_boards.append(board50)


# ============================================================
# TESTBOARDS4.PY - BOARDS 51-100
# ============================================================

# ==============================================================================
# KATEGORIE 1: ANFANGSZUSTÄNDE / FRÜHES SPIEL
# ==============================================================================

b1 = create_empty_board()
b1[4][4] = "K"
for f in [2, 3, 5, 6]:
    b1[4][f] = "W"
    b1[f][4] = "W"
for f in [3, 4, 5]:
    b1[0][f] = "B"
    b1[8][f] = "B"
    b1[f][0] = "B"
    b1[f][8] = "B"
b1[1][4] = "B"; b1[7][4] = "B"; b1[4][1] = "B"; b1[4][7] = "B"
all_boards.append(b1)

b2 = create_empty_board()
b2[4][4] = "K"
for f in [2, 3, 5, 6]:
    b2[4][f] = "W"
    b2[f][4] = "W"
for f in [3, 4, 5]:
    b2[0][f] = "B"
    b2[8][f] = "B"
    b2[f][8] = "B"
b2[1][4] = "B"; b2[7][4] = "B"; b2[4][7] = "B"
b2[3][2] = "B"; b2[4][2] = "B"; b2[5][2] = "B"
all_boards.append(b2)

b3 = create_empty_board()
b3[4][4] = "K"
b3[4][2] = "W"; b3[4][3] = "W"; b3[5][4] = "W"; b3[6][4] = "W"
b3[2][6] = "W"; b3[1][6] = "W"
for f in [3, 4, 5]:
    b3[8][f] = "B"
    b3[f][0] = "B"
b3[0][3] = "B"; b3[0][5] = "B"; b3[1][4] = "B"; b3[4][1] = "B"; b3[7][4] = "B"
b3[3][7] = "B"; b3[4][7] = "B"; b3[5][7] = "B"
all_boards.append(b3)

b4 = create_empty_board()
b4[4][4] = "K"
for f in [2, 3, 5, 6]:
    b4[4][f] = "W"
b4[3][4] = "W"
for f in [3, 4, 5]:
    b4[0][f] = "B"
    b4[f][0] = "B"
    b4[f][8] = "B"
b4[1][4] = "B"; b4[4][1] = "B"; b4[4][7] = "B"
b4[7][2] = "B"; b4[7][3] = "B"; b4[7][4] = "B"; b4[7][5] = "B"; b4[7][6] = "B"
all_boards.append(b4)

b5 = create_empty_board()
b5[4][4] = "K"
b5[2][4] = "W"; b5[6][4] = "W"; b5[4][2] = "W"; b5[4][6] = "W"
b5[1][2] = "B"; b5[1][6] = "B"; b5[7][2] = "B"; b5[7][6] = "B"
b5[2][1] = "B"; b5[2][7] = "B"; b5[6][1] = "B"; b5[6][7] = "B"
all_boards.append(b5)

b6 = create_empty_board()
b6[6][2] = "K"
b6[6][3] = "W"; b6[5][2] = "W"; b6[4][3] = "W"
b6[0][3] = "B"; b6[0][4] = "B"; b6[0][5] = "B"; b6[4][8] = "B"; b6[5][8] = "B"
b6[7][1] = "B"; b6[7][3] = "B"; b6[8][4] = "B"
all_boards.append(b6)

b7 = create_empty_board()
b7[4][4] = "K"
b7[3][4] = "W"; b7[5][4] = "W"
b7[4][2] = "B"; b7[4][3] = "B"; b7[4][5] = "B"; b7[4][6] = "B"
b7[2][4] = "B"; b7[6][4] = "B"
b7[0][1] = "B"; b7[0][7] = "B"; b7[8][1] = "B"; b7[8][7] = "B"
all_boards.append(b7)

b8 = create_empty_board()
b8[4][5] = "K"
b8[3][5] = "W"; b8[5][5] = "W"; b8[4][6] = "W"; b8[2][6] = "W"
b8[2][1] = "B"; b8[3][1] = "B"; b8[4][1] = "B"; b8[5][1] = "B"; b8[6][1] = "B"
b8[4][3] = "B"; b8[3][2] = "B"; b8[5][2] = "B"
all_boards.append(b8)

# ==============================================================================
# KATEGORIE 2: MITTELSPIEL
# ==============================================================================

b9 = create_empty_board()
b9[4][4] = 0; b9[3][3] = "K"
b9[2][3] = "W"; b9[3][5] = "W"; b9[5][3] = "W"
b9[1][3] = "B"; b9[3][1] = "B"; b9[3][7] = "B"; b9[6][3] = "B"; b9[4][2] = "B"; b9[4][6] = "B"
all_boards.append(b9)

b10 = create_empty_board()
b10[4][4] = 0; b10[2][6] = "K"
b10[1][6] = "W"; b10[2][5] = "W"; b10[3][7] = "W"
b10[0][6] = "B"; b10[2][8] = "B"; b10[1][5] = "B"; b10[3][6] = "B"; b10[2][3] = "B"
b10[7][2] = "B"; b10[6][1] = "B"
all_boards.append(b10)

b11 = create_empty_board()
b11[5][4] = "K"
b11[1][2] = "W"; b11[7][6] = "W"; b11[3][7] = "W"
b11[0][4] = "B"; b11[2][1] = "B"; b11[4][8] = "B"; b11[8][3] = "B"; b11[6][2] = "B"; b11[3][3] = "B"
all_boards.append(b11)

b12 = create_empty_board()
b12[4][4] = 0; b12[4][6] = "K"
b12[3][6] = "W"; b12[5][6] = "W"; b12[4][5] = "W"
b12[2][6] = "B"; b12[6][6] = "B"; b12[4][7] = "B"; b12[3][8] = "B"; b12[5][8] = "B"
b12[4][1] = "B"
all_boards.append(b12)

b13 = create_empty_board()
b13[4][4] = "K"
b13[1][4] = "W"; b13[7][4] = "W"; b13[4][1] = "W"; b13[4][7] = "W"
b13[1][3] = "B"; b13[1][5] = "B"; b13[7][3] = "B"; b13[7][5] = "B"
b13[3][1] = "B"; b13[5][1] = "B"; b13[3][7] = "B"; b13[5][7] = "B"
all_boards.append(b13)

b14 = create_empty_board()
b14[4][4] = 0; b14[6][2] = "K"
b14[6][1] = "W"; b14[7][2] = "W"; b14[5][3] = "W"
b14[5][1] = "B"; b14[7][1] = "B"; b14[8][2] = "B"; b14[6][4] = "B"; b14[6][0] = "B"
b14[1][7] = "B"; b14[2][7] = "B"
all_boards.append(b14)

b15 = create_empty_board()
b15[4][4] = 0; b15[2][2] = "K"
b15[2][4] = "W"; b15[4][2] = "W"
b15[1][2] = "B"; b15[3][2] = "B"; b15[2][1] = "B"; b15[2][3] = "B"
b15[0][5] = "B"; b15[5][0] = "B"; b15[8][6] = "B"
all_boards.append(b15)

b16 = create_empty_board()
b16[4][4] = "K"
b16[1][1] = "B"; b16[1][2] = "W"
b16[7][7] = "B"; b16[6][7] = "W"
b16[2][7] = "B"; b16[2][6] = "B"; b16[1][6] = "W"
all_boards.append(b16)

# ==============================================================================
# KATEGORIE 3: SCHWARZ IM VORTEIL
# ==============================================================================

b17 = create_empty_board()
b17[4][4] = "K"
b17[3][4] = "B"; b17[5][4] = "B"; b17[4][3] = "B"
b17[1][1] = "W"; b17[7][7] = "W"
b17[4][7] = "B"; b17[7][4] = "B"
all_boards.append(b17)

b18 = create_empty_board()
b18[4][4] = 0; b18[2][4] = "K"
b18[2][3] = "W"
b18[1][4] = "B"; b18[2][5] = "B"; b18[3][4] = "B"; b18[0][2] = "B"; b18[0][6] = "B"; b18[1][7] = "B"
all_boards.append(b18)

b19 = create_empty_board()
b19[4][4] = 0; b19[4][2] = "K"
b19[4][3] = "W"
b19[0][2] = "B"; b19[8][2] = "B"; b19[4][0] = "B"; b19[4][6] = "B"; b19[3][1] = "B"; b19[5][1] = "B"
all_boards.append(b19)

b20 = create_empty_board()
b20[4][4] = 0; b20[4][5] = "K"
b20[3][5] = "W"
b20[1][7] = "B"; b20[2][7] = "B"; b20[3][7] = "B"; b20[4][7] = "B"; b20[5][7] = "B"; b20[6][7] = "B"
all_boards.append(b20)

b21 = create_empty_board()
b21[4][4] = 0; b21[8][4] = "K"
b21[7][4] = "B"; b21[8][2] = "B"; b21[8][6] = "B"
b21[5][1] = "W"
all_boards.append(b21)

b22 = create_empty_board()
b22[4][4] = 0; b22[5][3] = "K"
b22[5][2] = "B"; b22[5][4] = "B"; b22[4][3] = "B"
b22[2][2] = "W"
all_boards.append(b22)

b23 = create_empty_board()
b23[4][4] = 0; b23[3][6] = "K"
b23[2][6] = "B"; b23[4][6] = "B"
b23[3][2] = "B"; b23[7][6] = "B"
b23[0][3] = "W"
all_boards.append(b23)

b24 = create_empty_board()
b24[4][4] = 0; b24[1][1] = "K"
b24[1][5] = "B"; b24[5][1] = "B"; b24[2][2] = "B"
all_boards.append(b24)

b25 = create_empty_board()
b25[4][4] = 0; b25[7][7] = "K"
b25[7][6] = "B"; b25[6][7] = "B"
b25[3][3] = "W"
all_boards.append(b25)

# ==============================================================================
# KATEGORIE 4: WEISS IM VORTEIL
# ==============================================================================

b26 = create_empty_board()
b26[4][4] = 0; b26[2][2] = "K"
b26[2][1] = "W"; b26[1][2] = "W"
b26[5][7] = "B"; b26[6][7] = "B"; b26[7][7] = "B"
all_boards.append(b26)

b27 = create_empty_board()
b27[4][4] = 0; b27[7][4] = "K"
b27[7][1] = "W"; b27[7][7] = "W"
b27[1][1] = "B"; b27[1][2] = "B"
all_boards.append(b27)

b28 = create_empty_board()
b28[4][4] = 0; b28[4][7] = "K"
b28[4][6] = "W"
b28[0][1] = "B"; b28[8][1] = "B"
all_boards.append(b28)

b29 = create_empty_board()
b29[4][4] = 0; b29[3][3] = "K"
b29[2][2] = "W"; b29[3][2] = "W"; b29[4][2] = "W"; b29[2][3] = "W"
b29[6][6] = "B"; b29[7][7] = "B"
all_boards.append(b29)

b30 = create_empty_board()
b30[4][4] = 0; b30[1][7] = "K"
b30[6][2] = "W"; b30[6][3] = "W"
b30[7][1] = "B"; b30[7][2] = "B"; b30[6][1] = "B"
all_boards.append(b30)

b31 = create_empty_board()
b31[4][4] = 0; b31[5][5] = "K"
b31[1][5] = "W"
b31[4][1] = "B"; b31[7][1] = "B"
all_boards.append(b31)

b32 = create_empty_board()
b32[4][4] = 0; b32[3][2] = "K"
b32[3][1] = "W"; b32[3][3] = "W"
b32[3][4] = "B"
all_boards.append(b32)

b33 = create_empty_board()
b33[4][4] = 0; b33[1][1] = "K"
b33[1][2] = "W"; b33[2][1] = "W"
b33[5][5] = "B"; b33[6][6] = "B"
all_boards.append(b33)

b34 = create_empty_board()
b34[4][4] = 0; b34[3][0] = "K"
b34[5][3] = "W"
b34[6][6] = "B"
all_boards.append(b34)

# ==============================================================================
# KATEGORIE 5: SCHWARZ KURZ VOR DEM SIEG
# ==============================================================================

b35 = create_empty_board()
b35[4][4] = 0; b35[3][5] = "K"
b35[3][4] = "B"
b35[0][6] = "B"
all_boards.append(b35)

b36 = create_empty_board()
b36[4][4] = 0; b36[4][3] = "K"
b36[3][3] = "B"; b36[5][3] = "B"
b36[4][7] = "B"
all_boards.append(b36)

b37 = create_empty_board()
b37[4][4] = "K"
b37[3][4] = "B"; b37[5][4] = "B"; b37[4][3] = "B"
b37[4][8] = "B"
all_boards.append(b37)

b38 = create_empty_board()
b38[4][4] = 0; b38[0][6] = "K"
b38[0][5] = "B"
b38[5][6] = "B"
all_boards.append(b38)

b39 = create_empty_board()
b39[4][4] = 0; b39[8][1] = "K"
b39[7][1] = "B"
b39[8][5] = "B"
all_boards.append(b39)

b40 = create_empty_board()
b40[4][4] = 0; b40[5][2] = "K"
b40[6][2] = "B"
b40[1][2] = "B"
all_boards.append(b40)

b41 = create_empty_board()
b41[4][4] = 0; b41[4][5] = "K"
b41[3][5] = "B"; b41[5][5] = "B"
b41[0][6] = "B"
all_boards.append(b41)

b42 = create_empty_board()
b42[4][4] = 0; b42[0][3] = "K"
b42[0][2] = "B"; b42[0][4] = "B"
b42[6][3] = "B"
all_boards.append(b42)

# ==============================================================================
# KATEGORIE 6: WEISS KURZ VOR DEM SIEG
# ==============================================================================

b43 = create_empty_board()
b43[4][4] = 0; b43[0][1] = "K"
b43[1][2] = "B"; b43[2][6] = "B"
b43[1][1] = "W"; b43[4][7] = "B"
all_boards.append(b43)

b44 = create_empty_board()
b44[4][4] = 0; b44[4][3] = "K"
b44[4][6] = "W"; b44[2][8] = "B"
all_boards.append(b44)

b45 = create_empty_board()
b45[4][4] = 0; b45[8][3] = "K"
b45[4][1] = "B"; b45[1][7] = "W"
all_boards.append(b45)

b46 = create_empty_board()
b46[4][4] = 0; b46[1][1] = "K"
b46[3][2] = "B"; b46[1][8] = "B"
b46[6][8] = "B"
all_boards.append(b46)

b47 = create_empty_board()
b47[4][4] = 0; b47[3][8] = "K"
b47[6][1] = "B"
all_boards.append(b47)

# ==============================================================================
# KATEGORIE 7: CHAOS / VERSTREUT
# ==============================================================================

b48 = create_empty_board()
b48[2][1] = "K"
b48[0][5] = "B"; b48[1][7] = "B"; b48[3][0] = "B"; b48[5][8] = "B"; b48[7][2] = "B"; b48[8][5] = "B"
b48[1][3] = "W"; b48[3][6] = "W"; b48[6][4] = "W"; b48[7][7] = "W"
all_boards.append(b48)

b49 = create_empty_board()
b49[5][2] = "K"
b49[1][6] = "B"; b49[7][1] = "B"; b49[3][7] = "B"
b49[6][5] = "W"
all_boards.append(b49)

b50 = create_empty_board()
b50[4][2] = "K"
b50[0][4] = "B"; b50[8][4] = "B"; b50[4][8] = "B"
b50[2][6] = "W"; b50[6][6] = "W"
all_boards.append(b50)

# ============================================================
# AUSGABE
# ============================================================

if __name__ == "__main__":
    print(f"Erfolgreich {len(all_boards)} Boards generiert.")
    
    # Statistik anzeigen
    for i, board in enumerate(all_boards):
        white = sum(row.count(W) for row in board)
        black = sum(row.count(B) for row in board)
        king = sum(row.count(K) for row in board)
        total = white + black + king
        print(f"Board {i+1}: {total} Figuren (W:{white}, B:{black}, K:{king})")