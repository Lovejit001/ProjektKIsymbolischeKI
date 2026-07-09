# testboards_simple.py
# 50 verschiedene Tablut-Boards mit echter Varianz
# B = Schwarz, W = Weiß, K = König, 0 = leeres Feld

B = 'B'
W = 'W'
K = 'K'

def create_empty_board():
    """Erstellt ein leeres 9x9 Board"""
    return [[0 for _ in range(9)] for _ in range(9)]

def is_valid_position(row, col):
    """Prüft ob eine Position gültig ist (kein Eckfeld)"""
    # Eckfelder sind (0,0), (0,8), (8,0), (8,8)
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

boards = []

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
boards.append(board1)

# BOARD 2: Erste Züge - Schwarz dringt ein, Weiß formiert sich
board2 = create_empty_board()
board2[4][4] = K
# Weiße Verteidiger
for f in [2, 3, 5, 6]:
    board2[4][f] = W
    board2[f][4] = W
# Schwarze Angreifer - leicht verschoben
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
boards.append(board2)

# BOARD 3: Weiß hat Thron verlassen, breite Verteilung
board3 = create_empty_board()
board3[4][3] = K  # König auf d5
board3[4][4] = 0
# Weiße Verteidiger - breit verteilt
board3[3][3] = W
board3[5][3] = W
board3[4][5] = W
board3[2][4] = W
board3[6][4] = W
board3[3][5] = W
board3[5][5] = W
# Schwarze Angreifer - viele
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
boards.append(board3)

# BOARD 4: Offene Stellung - viele Figuren über Brett verteilt
board4 = create_empty_board()
board4[5][4] = K  # König auf e4
# Weiße Figuren über Brett verteilt
board4[3][3] = W
board4[3][5] = W
board4[4][5] = W
board4[5][3] = W
board4[6][4] = W
board4[2][4] = W
board4[4][2] = W
# Schwarze Figuren über Brett verteilt
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
boards.append(board4)

# BOARD 5: Ausgebreitete Stellung - viele Optionen
board5 = create_empty_board()
board5[4][4] = K
# Weiß - breit verteilt
board5[2][3] = W
board5[2][5] = W
board5[3][2] = W
board5[3][4] = W
board5[4][3] = W
board5[4][5] = W
board5[5][4] = W
board5[6][3] = W
board5[6][5] = W
# Schwarz - breit verteilt
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
boards.append(board5)

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
boards.append(board6)

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
boards.append(board7)

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
boards.append(board8)

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
boards.append(board9)

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
boards.append(board10)

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
boards.append(board11)

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
boards.append(board12)

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
boards.append(board13)

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
boards.append(board14)

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
boards.append(board15)

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
boards.append(board16)

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
boards.append(board17)

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
boards.append(board18)

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
boards.append(board19)

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
boards.append(board20)

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
boards.append(board21)

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
boards.append(board22)

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
boards.append(board23)

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
boards.append(board24)

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
boards.append(board25)

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
boards.append(board26)

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
boards.append(board27)

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
boards.append(board28)

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
boards.append(board29)

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
boards.append(board30)

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
boards.append(board31)

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
boards.append(board32)

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
boards.append(board33)

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
boards.append(board34)

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
boards.append(board35)

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
boards.append(board36)

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
boards.append(board37)

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
boards.append(board38)

# ============================================================
# KATEGORIE 5: ENDSPIEL-STELLUNGEN (Boards 39-50)
# ============================================================

# BOARD 39: Wenige Figuren, offene Stellung
board39 = create_empty_board()
board39[4][3] = K  # König auf d5
board39[3][3] = W
board39[5][3] = W
board39[2][4] = B
board39[6][4] = B
board39[4][2] = B
boards.append(board39)

# BOARD 40: König mit zwei Verteidigern
board40 = create_empty_board()
board40[2][2] = K  # König auf c7
board40[2][3] = W
board40[3][2] = W
board40[1][2] = B
board40[2][1] = B
board40[4][2] = B
boards.append(board40)

# BOARD 41: Letzte Verteidigung
board41 = create_empty_board()
board41[5][4] = K  # König auf e4
board41[5][3] = W
board41[4][4] = W
board41[5][5] = W
board41[6][4] = B
board41[4][3] = B
board41[5][6] = B
boards.append(board41)

# BOARD 42: 1-gegen-1 Kampf um die Ecke
board42 = create_empty_board()
board42[0][2] = K  # König auf c9
board42[0][1] = W
board42[0][3] = B
board42[1][2] = B
boards.append(board42)

# BOARD 43: König am Rand, wenige Figuren
board43 = create_empty_board()
board43[0][3] = K  # König auf d9
board43[0][2] = W
board43[0][4] = W
board43[1][3] = B
board43[1][2] = B
boards.append(board43)

# BOARD 44: Zwei gegen zwei
board44 = create_empty_board()
board44[4][2] = K  # König auf c5
board44[4][3] = W
board44[4][1] = B
board44[3][2] = B
board44[5][2] = W
boards.append(board44)

# BOARD 45: König in der Mitte, allein
board45 = create_empty_board()
board45[4][4] = K  # König auf Thron
board45[3][4] = B
board45[5][4] = B
board45[4][3] = B
board45[4][5] = W
boards.append(board45)

# BOARD 46: Kritische Endspiel-Stellung
board46 = create_empty_board()
board46[3][3] = K  # König auf d6
board46[3][2] = W
board46[3][4] = B
board46[2][3] = B
board46[4][3] = B
board46[5][3] = W
boards.append(board46)

# BOARD 47: König auf der Flucht
board47 = create_empty_board()
board47[2][3] = K  # König auf d7
board47[2][4] = W
board47[2][2] = B
board47[3][3] = B
board47[1][3] = B
board47[4][3] = W
boards.append(board47)

# BOARD 48: Minimalistische Endspiel-Stellung
board48 = create_empty_board()
board48[5][3] = K  # König auf d4
board48[5][4] = W
board48[4][3] = B
board48[6][3] = B
board48[5][2] = W
boards.append(board48)

# BOARD 49: Kampf um die letzte Ecke
board49 = create_empty_board()
board49[0][2] = K  # König auf c9
board49[0][1] = W
board49[0][3] = B
board49[1][2] = B
board49[1][1] = W
boards.append(board49)

# BOARD 50: Entscheidende Endspiel-Situation
board50 = create_empty_board()
board50[0][1] = K  # König auf b9 (fast am Ziel)
board50[0][2] = W
board50[1][1] = B
board50[0][0] = 0  # Eckfeld bleibt frei
board50[1][2] = B
boards.append(board50)

# ============================================================
# AUSGABE
# ============================================================

if __name__ == "__main__":
    print(f"Erfolgreich {len(boards)} Boards generiert.")
    
    # Statistik anzeigen
    for i, board in enumerate(boards):
        white = sum(row.count(W) for row in board)
        black = sum(row.count(B) for row in board)
        king = sum(row.count(K) for row in board)
        total = white + black + king
        print(f"Board {i+1}: {total} Figuren (W:{white}, B:{black}, K:{king})")
    
    # Board 1 anzeigen
    print("\nBoard 1 (Startstellung):")
    for row in boards[0]:
        print(row)