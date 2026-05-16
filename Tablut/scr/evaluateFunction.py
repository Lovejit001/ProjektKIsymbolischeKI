"""
Tablut Bewertungsfunktion
=========================
Positiv  = gut für Weiß (Verteidiger)
Negativ  = gut für Schwarz (Angreifer)

Brett-Koordinaten: board[row][col], 0-indiziert, 9x9
Figuren: 'K' = König, 'W' = weißer Stein, 'B' = schwarzer Stein, 0 = leer
Thron:   (4, 4)
Ecken:   (0,0), (0,8), (8,0), (8,8)
"""

import math

# ──────────────────────────────────────────────────
# Konstanten
# ──────────────────────────────────────────────────

THRONE         = (4, 4)
CORNERS        = [(0, 0), (0, 8), (8, 0), (8, 8)]
THRONE_NEIGHBORS = [(3, 4), (5, 4), (4, 3), (4, 5)]

# ──────────────────────────────────────────────────
# Gewichte  (positiv = gut für Weiß)
# ──────────────────────────────────────────────────

W_WIN               =  100_000
B_WIN               = -100_000

W_PIECE_VALUE       =    150
B_PIECE_VALUE       =   -120

W_KING_CORNER_DIST  =    -80   # pro Manhattan-Distanz zur nächsten Ecke
W_KING_OPEN_PATHS   =    300   # freie orthogonale Wege zur Ecke
B_SURROUND_KING     =   -500   # schwarze Steine direkt neben König
W_PROTECT_KING      =    100   # weiße Steine direkt neben König

# Rand-Gefahr: König am Rand mit schwarzem Nachbar ist leicht einzuschließen
B_KING_ON_EDGE_THREAT = -350   # extra Strafe pro schwarzem Nachbar wenn König am Rand

# Ecken-Blockade durch Schwarz
B_CORNER_BLOCK      =    -70   # pro schwarzem Stein nahe Eckzugang

W_KING_ON_THRONE    =     40
W_CENTER_CONTROL    =     25
B_CENTER_CONTROL    =    -35


# ──────────────────────────────────────────────────
# Hilfsfunktionen
# ──────────────────────────────────────────────────

def find_king(board):
    for r in range(9):
        for c in range(9):
            if board[r][c] == 'K':
                return (r, c)
    return None


def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def nearest_corner_dist(pos):
    return min(manhattan(pos, corner) for corner in CORNERS)


def neighbors_of(pos):
    r, c = pos
    result = []
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 9 and 0 <= nc < 9:
            result.append((nr, nc))
    return result


def king_open_paths_to_corners(board, king_pos):
    """
    Zählt auf wie vielen der 4 orthogonalen Richtungen der König
    eine ungehinderte Linie zu einer Ecke hat.
    """
    kr, kc = king_pos
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    open_paths = 0

    for dr, dc in directions:
        r, c = kr + dr, kc + dc
        blocked = False
        while 0 <= r < 9 and 0 <= c < 9:
            cell = board[r][c]
            if cell != 0 and (r, c) != king_pos:
                blocked = True
                break
            if (r, c) in CORNERS:
                open_paths += 1
                break
            r += dr
            c += dc

    return open_paths


def black_adjacent_to_king(board, king_pos):
    count = 0
    for nb in neighbors_of(king_pos):
        if board[nb[0]][nb[1]] == 'B':
            count += 1
    return count


def white_adjacent_to_king(board, king_pos):
    count = 0
    for nb in neighbors_of(king_pos):
        if board[nb[0]][nb[1]] == 'W':
            count += 1
    return count


def king_is_captured(board, king_pos):
    """
    Prüft ob der König geschlagen gilt:
    - Auf dem Thron: alle 4 Nachbarn schwarz
    - Auf Thron-Nachbarfeld: 3 schwarze + Thron als 4. Seite
    - Sonst: eingeschlossen von 2 Feinden (auch Ecke / leerer Thron zählt)
    """
    if king_pos is None:
        return True

    kr, kc = king_pos

    def is_hostile(pos):
        r, c = pos
        if not (0 <= r < 9 and 0 <= c < 9):
            return False
        if (r, c) in CORNERS:
            return True
        if (r, c) == THRONE and board[r][c] == 0:
            return True
        return board[r][c] == 'B'

    if king_pos == THRONE:
        return all(
            board[kr + dr][kc + dc] == 'B'
            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]
        )

    if king_pos in THRONE_NEIGHBORS:
        hostile_count = sum(
            is_hostile((kr + dr, kc + dc))
            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]
        )
        return hostile_count >= 3

    # Normales Feld: horizontale oder vertikale Einschließung
    for dr, dc in [(-1, 0), (0, -1)]:
        a = (kr + dr, kc + dc)
        b = (kr - dr, kc - dc)
        if is_hostile(a) and is_hostile(b):
            return True

    return False


def king_on_corner(king_pos):
    return king_pos in CORNERS


def king_on_edge(king_pos):
    """König am Rand (aber nicht Ecke) — leichter einzuschließen."""
    r, c = king_pos
    return (r == 0 or r == 8 or c == 0 or c == 8) and king_pos not in CORNERS


def count_center_control(board):
    """Zählt Steine im 5×5-Zentrum (Zeilen/Spalten 2–6)."""
    w = b = 0
    for r in range(2, 7):
        for c in range(2, 7):
            cell = board[r][c]
            if cell == 'W':
                w += 1
            elif cell == 'B':
                b += 1
    return w, b


def count_corner_blocks(board):
    """
    Zählt schwarze Steine die direkt neben einer Ecke stehen
    und damit den Weg des Königs blockieren.
    """
    blocks = 0
    for cr, cc in CORNERS:
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < 9 and 0 <= nc < 9:
                if board[nr][nc] == 'B':
                    blocks += 1
    return blocks


# ──────────────────────────────────────────────────
# Haupt-Bewertungsfunktion
# ──────────────────────────────────────────────────

def eval(board):
    """
    Gibt einen skalaren Score zurück.
    Positiv = Vorteil für Weiß, Negativ = Vorteil für Schwarz.
    """
    score = 0
    king_pos = find_king(board)

    # ── Terminalbedingungen ──────────────────────────
    if king_on_corner(king_pos):
        return W_WIN

    if king_is_captured(board, king_pos):
        return B_WIN

    if king_pos is None:
        return B_WIN

    # ── Figurenanzahl ────────────────────────────────
    w_pieces = sum(board[r][c] in ('W', 'K') for r in range(9) for c in range(9))
    b_pieces = sum(board[r][c] == 'B'        for r in range(9) for c in range(9))

    score += (w_pieces - 1) * W_PIECE_VALUE  # -1 weil König separat bewertet
    score += b_pieces * B_PIECE_VALUE

    # ── Königsposition ───────────────────────────────
    kr, kc = king_pos

    # Distanz zur nächsten Ecke
    dist = nearest_corner_dist(king_pos)
    score += dist * W_KING_CORNER_DIST

    # Freie Wege zu Ecken (wichtigster Faktor für Weiß)
    open_paths = king_open_paths_to_corners(board, king_pos)
    score += open_paths * W_KING_OPEN_PATHS

    # Schwarze Steine direkt neben König
    black_adj = black_adjacent_to_king(board, king_pos)
    score += black_adj * B_SURROUND_KING

    # Weiße Steine neben König (Schutz)
    white_adj = white_adjacent_to_king(board, king_pos)
    score += white_adj * W_PROTECT_KING

    # ── Rand-Gefahr ──────────────────────────────────
    # König am Rand + schwarzer Nachbar = akute Einschließungsgefahr
    # weil Rand als Einschluss zählt (nur 1 weiterer Feind nötig)
    if king_on_edge(king_pos):
        score += black_adj * B_KING_ON_EDGE_THREAT

    # ── König auf Thron ──────────────────────────────
    if king_pos == THRONE:
        score += W_KING_ON_THRONE

    # ── Ecken-Blockade ───────────────────────────────
    corner_blocks = count_corner_blocks(board)
    score += corner_blocks * B_CORNER_BLOCK

    # ── Zentrumskontrolle ────────────────────────────
    w_center, b_center = count_center_control(board)
    score += w_center * W_CENTER_CONTROL
    score += b_center * B_CENTER_CONTROL

    return score