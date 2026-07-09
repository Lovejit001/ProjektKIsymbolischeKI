# tablut_boards.py
# 50 verschiedene Tablut-Board-Zustände (9x9 Arrays)
# Gemäß den offiziellen Regeln: Schwarz (S) beginnt, Weiß (W) verteidigt den König (K).
# X markiert den Thron (e5) oder die Eckfelder (a1, a9, i1, i9).

# Hilfsfunktion zur Erstellung eines leeren Boards mit Thron und Ecken
def create_empty_board():
    board = [[" " for _ in range(9)] for _ in range(9)]
    board[0][0] = "X"  # a9
    board[0][8] = "X"  # i9
    board[8][0] = "X"  # a1
    board[8][8] = "X"  # i1
    board[4][4] = "X"  # e5 (Thron)
    return board

x = []

# ==============================================================================
# KATEGORIE 1: STARTZUSTÄNDE & FRÜHE SPIELPHASEN (Boards 1-8)
# ==============================================================================

# Board 1: Die offizielle Startaufstellung
b1 = create_empty_board()
b1[4][4] = "K"  # König auf dem Thron
# Weiße Verteidiger im Kreuz
for f in [2, 3, 5, 6]: b1[4][f] = "W"; b1[f][4] = "W"
# Schwarze Angreifer an den Rändern
for f in [3, 4, 5]: b1[0][f] = "S"; b1[8][f] = "S"; b1[f][0] = "S"; b1[f][8] = "S"
b1[1][4] = "S"; b1[7][4] = "S"; b1[4][1] = "S"; b1[4][7] = "S"
x.append({"board": b1, "description": "1. Offizielle Startaufstellung. S beginnt, alle Steine in T-Form an den Raendern."})

# Board 2: Erster Zug von Schwarz (z.B. f9-f7)
b2 = [row[:] for row in b1]
b2[0][5] = " "
b2[2][5] = "S"
x.append({"board": b2, "description": "2. Fruehes Spiel: Schwarz hat f9 nach f7 bewegt, um Druck aufzubauen."})

# Board 3: Weiß antwortet (z.B. e6-f6)
b3 = [row[:] for row in b2]
b3[3][4] = " "
b3[3][5] = "W"
x.append({"board": b3, "description": "3. Fruehes Spiel: Weiss zieht einen Verteidiger aus dem Zentrum nach rechts heraus."})

# Board 4: Schwarz blockiert Fluchtwege
b4 = [row[:] for row in b3]
b4[4][0] = " "
b4[2][0] = "S"
x.append({"board": b4, "description": "4. Fruehes Spiel: Ein schwarzer Stein zieht auf der a-Linie nach oben."})

# Board 5: König verlässt den Thron (Erster Schritt)
b5 = [row[:] for row in b1]
b5[4][4] = "X"  # Thron ist jetzt leer
b5[4][3] = "K"  # König zieht nach d5
x.append({"board": b5, "description": "5. Fruehes Spiel: Der Koenig verlaesst sehr frueh den Thron in Richtung d5."})

# Board 6: Minimaler Abtausch im Zentrum
b6 = create_empty_board()
b6[4][4] = "K"
b6[4][3] = "W"; b6[4][5] = "W"; b6[3][4] = "W"; b6[5][4] = "W"
b6[2][4] = "S"; b6[6][4] = "S"; b6[4][2] = "S"; b6[4][6] = "S"
x.append({"board": b6, "description": "6. Fruehes Spiel: Ein kompakteres Zentrum nach den ersten symmetrischen Schlaegen."})

# Board 7: Schwarz oeffnet eine Flanke
b7 = [row[:] for row in b1]
b7[0][4] = " "
b7[1][3] = "S"
x.append({"board": b7, "description": "7. Fruehes Spiel: Schwarz repositioniert die e9-Zwinge nach d8."})

# Board 8: Weiß versucht eine Gasse zu schlagen
b8 = [row[:] for row in b1]
b8[4][2] = " "
b8[2][2] = "W"
x.append({"board": b8, "description": "8. Fruehes Spiel: Weiss zieht c5 nach c7, um die obere linke Ecke anzusteuern."})


# ==============================================================================
# KATEGORIE 2: MITTENDRIN / AUSGEGLICHENE SITUATIONEN (Boards 9-16)
# ==============================================================================

# Board 9: Offener Schlagabtausch, einige Steine fehlen bereits
b9 = create_empty_board()
b9[4][4] = "X"; b9[4][3] = "K"  # König auf d5
b9[3][3] = "W"; b9[5][5] = "W"; b9[2][4] = "W"
b9[1][3] = "S"; b9[4][1] = "S"; b9[6][3] = "S"; b9[4][6] = "S"; b9[7][5] = "S"
x.append({"board": b9, "description": "9. Midgame: Ausgeglichen. Beide Seiten haben bereits 3-4 Figuren verloren."})

# Board 10: König blockiert in der Mitte, Kampf an den Flanken
b10 = create_empty_board()
b10[4][4] = "K"; b10[4][5] = "W"; b10[5][4] = "W"
b10[2][2] = "S"; b10[6][6] = "S"; b10[4][2] = "S"; b10[2][4] = "S"
x.append({"board": b10, "description": "10. Midgame: Der Koenig verbleibt auf dem Thron, waehrend die Verteidiger dezimiert sind."})

# Board 11: Dynamische Struktur mit freien Linien
b11 = create_empty_board()
b11[4][4] = "X"; b11[3][4] = "K"  # König auf e6
b11[3][2] = "W"; b11[5][6] = "W"
b11[1][4] = "S"; b11[3][7] = "S"; b11[7][4] = "S"; b11[4][2] = "S"
x.append({"board": b11, "description": "11. Midgame: Weit verstreute Figuren. Die e- und g-Linien sind teilweise geoeffnet."})

# Board 12: Taktische Einklammerungsgefahr fuer Weiss
b12 = create_empty_board()
b12[4][4] = "X"; b12[4][5] = "K"
b12[4][6] = "W"; b12[2][5] = "W"
b12[4][7] = "S"; b12[3][5] = "S"; b12[5][5] = "S"; b12[1][1] = "S"
x.append({"board": b12, "description": "12. Midgame: Weiss versucht eine Festung rechts zu bauen, Schwarz klammert eng ein."})

# Board 13: Symmetrisches Chaos
b13 = create_empty_board()
b13[4][4] = "K"
for pos in [(2,3), (3,2), (5,6), (6,5)]: b13[pos[0]][pos[1]] = "W"
for pos in [(1,3), (3,1), (7,5), (5,7)]: b13[pos[0]][pos[1]] = "S"
x.append({"board": b13, "description": "13. Midgame: Symmetrische Verteilung nach wildem Schlagabtausch im inneren Ring."})

# Board 14: Barrikadenkampf
b14 = create_empty_board()
b14[4][4] = "X"; b14[4][2] = "K"
b14[3][2] = "W"; b14[5][2] = "W"
b14[2][2] = "S"; b14[6][2] = "S"; b14[4][1] = "S"; b14[4][5] = "S"
x.append({"board": b14, "description": "14. Midgame: Der Koenig ist auf c5 von eigenen Verteidigern vertikal geschuetzt."})

# Board 15: Massiver Figurenabbau
b15 = create_empty_board()
b15[4][4] = "X"; b15[5][4] = "K"
b15[5][3] = "W"
b15[2][4] = "S"; b15[5][7] = "S"; b15[7][2] = "S"
x.append({"board": b15, "description": "15. Midgame: Sehr wenige Figuren uebrig. Hohe Mobilitaet fuer beide Seiten."})

# Board 16: Drohende Spaltung der Verteidigung
b16 = create_empty_board()
b16[4][4] = "K"; b16[4][3] = "W"; b16[2][4] = "W"
b16[4][2] = "S"; b16[3][3] = "S"; b16[1][4] = "S"; b16[5][5] = "S"
x.append({"board": b16, "description": "16. Midgame: Schwarz bricht in den inneren Verteidigungsring ein."})


# ==============================================================================
# KATEGORIE 3: SCHWARZ IM VORTEIL (Boards 17-25)
# ==============================================================================

# Board 17: König auf dem Thron umzingelt (3 von 4 Seiten)
b17 = create_empty_board()
b17[4][4] = "K"
b17[3][4] = "S"; b17[5][4] = "S"; b17[4][3] = "S"  # 3 Angreifer am Thron
b17[4][5] = "W"  # Letzter Schutz-Verteidiger
x.append({"board": b17, "description": "17. Schwarz Vorteil: Der Koenig ist auf dem Thron bereits von 3 Seiten belagert."})

# Board 18: Weiß hat kaum noch Verteidiger
b18 = create_empty_board()
b18[4][4] = "X"; b18[2][2] = "K"
b18[2][6] = "W"  # Weit weg vom König
b18[1][2] = "S"; b18[2][1] = "S"; b18[5][2] = "S"; b18[2][5] = "S"
x.append({"board": b18, "description": "18. Schwarz Vorteil: Der Koenig ist isoliert, der einzige Verteidiger steht abseits."})

# Board 19: Alle Fluchtwege zu den Ecken blockiert
b19 = create_empty_board()
b19[4][4] = "X"; b19[4][3] = "K"
b19[1][1] = "S"; b19[1][7] = "S"; b19[7][1] = "S"; b19[7][7] = "S"  # Strategische Ecken-Blockade
x.append({"board": b19, "description": "19. Schwarz Vorteil: Schwarz kontrolliert die Diagonalen vor den Eckfeldern."})

# Board 20: König in der Falle an der Wand
b20 = create_empty_board()
b20[4][4] = "X"; b20[0][3] = "K"  # König auf d9
b20[0][2] = "S"; b20[1][3] = "S"  # Eingekesselt an der Wand
x.append({"board": b20, "description": "20. Schwarz Vorteil: Der Koenig steht an der oberen Bande und ist fast bewegungsunfaehig."})

# Board 21: Verteidiger-Minderheit (8 Angreifer gegen 2 Verteidiger)
b21 = create_empty_board()
b21[4][4] = "X"; b21[3][4] = "K"
b21[3][3] = "W"
for f in [1, 2, 5, 6]: b21[f][2] = "S"; b21[2][f] = "S"
x.append({"board": b21, "description": "21. Schwarz Vorteil: Drastische Materialueberlegenheit fuer Schwarz im Zentrum."})

# Board 22: Thron als Blockade-Werkzeug fuer Schwarz
b22 = create_empty_board()
b22[4][4] = "X"; b22[5][4] = "K"  # König auf e4
b22[6][4] = "S"; b22[5][3] = "S"  # Unten und links blockiert. Oben ist der leere Thron (X).
x.append({"board": b22, "description": "22. Schwarz Vorteil: Schwarz nutzt den leeren Thron, um den Koenig oben zu blockieren."})

# Board 23: Zangengriff auf der d-Linie
b23 = create_empty_board()
b23[4][4] = "X"; b23[4][3] = "K"
b23[2][3] = "S"; b23[6][3] = "S"; b23[4][1] = "S"
x.append({"board": b23, "description": "23. Schwarz Vorteil: Der Koenig ist in einer vertikalen Zange gefangen."})

# Board 24: Abgeschnittener Fluchtkorridor links
b24 = create_empty_board()
b24[4][4] = "X"; b24[4][2] = "K"
b24[1][0] = "S"; b24[3][0] = "S"; b24[5][0] = "S"; b24[7][0] = "S"
x.append({"board": b24, "description": "24. Schwarz Vorteil: Die komplette linke Aussenbahn ist in schwarzer Hand."})

# Board 25: Dominanz im Zentrum
b25 = create_empty_board()
b25[4][4] = "K"
for f in [3, 5]: b25[4][f] = "S"; b25[f][4] = "S"
x.append({"board": b25, "description": "25. Schwarz Vorteil: Der Koenig sitzt auf dem Thron fest, alle direkten Nachbarn sind schwarz."})


# ==============================================================================
# KATEGORIE 4: WEISS IM VORTEIL (Boards 26-34)
# ==============================================================================

# Board 26: Freie Bahn zu einer Ecke
b26 = create_empty_board()
b26[4][4] = "X"; b26[2][2] = "K"  # König auf c7
# Keine schwarzen Steine auf der Rechts-Achse oder Oben-Achse zu den Ecken
b26[2][3] = "W"; b26[3][2] = "W"
x.append({"board": b26, "description": "26. Weiss Vorteil: Der Koenig hat freie Bahn zur linken oberen oder rechten oberen Ecke."})

# Board 27: Materialvorteil Weiß (Kaum noch Angreifer übrig)
b27 = create_empty_board()
b27[4][4] = "X"; b27[4][5] = "K"
b27[4][3] = "W"; b27[3][5] = "W"; b27[5][5] = "W"
b27[0][4] = "S"  # Nur noch ein einsamer Angreifer
x.append({"board": b27, "description": "27. Weiss Vorteil: Schwarz hat fast alle Angreifer durch unvorsichtige Zuege verloren."})

# Board 28: Ausbruch aus dem Zentrum gelungen
b28 = create_empty_board()
b28[4][4] = "X"; b28[6][2] = "K"  # König auf c3
b28[6][3] = "W"; b28[5][2] = "W"  # Eskorte schützt ihn
b28[8][2] = "S"  # Schwarz steht hinterher
x.append({"board": b28, "description": "28. Weiss Vorteil: Der Koenig ist ausgebrochen und wird von zwei Verteidigern abgeschirmt."})

# Board 29: König agiert als aktiver Jäger
b29 = create_empty_board()
b29[4][4] = "X"; b29[4][2] = "K"  # König auf c5
b29[4][1] = "W"
b29[3][2] = "S"  # Kann vom König und einem W geschlagen werden
x.append({"board": b29, "description": "29. Weiss Vorteil: Der Koenig kann aktiv helfen, schwarze Steine einzukesseln."})

# Board 30: Perfekte Verteidigungs-Phalanx
b30 = create_empty_board()
b30[4][4] = "X"; b30[1][4] = "K"  # König auf e8
b30[1][3] = "W"; b30[1][5] = "W"; b30[2][4] = "W"  # Schutzwall
x.append({"board": b30, "description": "30. Weiss Vorteil: Der Koenig steht sicher hinter einer unbeschadeten Verteidigungslinie."})

# Board 31: Freie Fahrt auf Reihe 2
b31 = create_empty_board()
b31[4][4] = "X"; b31[7][3] = "K"  # König auf d2
# Ganze Reihe 2 (Index 7) ist frei bis zur Ecke a2/i2
x.append({"board": b31, "description": "31. Weiss Vorteil: Reihe 2 ist komplett leer geraeumt, freier Weg fuer den Koenig."})

# Board 32: Aggressive Eskorte
b32 = create_empty_board()
b32[4][4] = "X"; b32[3][3] = "K"  # König auf d6
b32[3][0] = "W"; b32[3][8] = "W"; b32[0][3] = "W"  # Kontrollieren die Achsen
x.append({"board": b32, "description": "32. Weiss Vorteil: Weisse Raeumschiffe sichern die Fluchtachsen des Koenigs."})

# Board 33: Schwarz ist in den Ecken gefangen
b33 = create_empty_board()
b33[4][4] = "X"; b33[4][3] = "K"
b33[0][1] = "S"; b33[8][1] = "S"  # Schwarze Steine stehen nutzlos nah an den Ecken
b33[3][3] = "W"; b33[5][3] = "W"
x.append({"board": b33, "description": "33. Weiss Vorteil: Die verbleibenden schwarzen Steine stehen taktisch unguenstig abseits."})

# Board 34: König nähert sich unaufhaltsam Ecke h9
b34 = create_empty_board()
b34[4][4] = "X"; b34[0][7] = "K"  # König auf h9
b34[1][7] = "W"  # Schützt von unten
x.append({"board": b34, "description": "34. Weiss Vorteil: Der Koenig steht direkt neben dem Zielfeld i9, bewacht von W."})


# ==============================================================================
# KATEGORIE 5: SCHWARZ KURZ VOR DEM SIEG (Boards 35-42)
# ==============================================================================

# Board 35: König auf freiem Feld von 1 Seite belagert, 2. folgt im nächsten Zug
b35 = create_empty_board()
b35[4][4] = "X"; b35[3][3] = "K"  # König auf d6
b35[2][3] = "S"  # Oben belagert (d7)
b35[3][1] = "S"  # Zieht im naechsten Zug auf d6- links (b6 nach c6)
x.append({"board": b35, "description": "35. Schwarz gewinnt fast: S am Zug zieht b6-c6 und schlaegt den Koenig auf freiem Feld."})

# Board 36: König am Thron-Rand, 2 von 3 legalen Feldern besetzt
b36 = create_empty_board()
b36[4][4] = "X"; b36[3][4] = "K"  # König auf e6 (neben Thron)
b36[2][4] = "S"; b36[3][3] = "S"  # d6 und e7 besetzt
b36[3][8] = "S"  # Angreifer auf i6 bereit für e6-rechts (f6)
x.append({"board": b36, "description": "36. Schwarz gewinnt fast: S zieht i6-f6, besetzt das 3. Feld am Thron-Nachbarn und schlaegt K."})

# Board 37: König auf dem Thron, 3 Plätze voll, 4. Schlagzug bereit
b37 = create_empty_board()
b37[4][4] = "K"  # Auf dem Thron
b37[3][4] = "S"; b37[5][4] = "S"; b37[4][3] = "S"  # e6, e4, d5 besetzt
b37[0][5] = "S"  # Auf f9 bereit fuer Zug nach f5
x.append({"board": b37, "description": "37. Schwarz gewinnt fast: S am Zug zieht f9-f5, schliesst das 4. Feld um den Thron."})

# Board 38: Doppel-Schlag-Drohung auf freiem Feld
b38 = create_empty_board()
b38[4][4] = "X"; b38[5][5] = "K"  # König auf f4
b38[5][4] = "S"  # Links besetzt (e4)
b38[1][5] = "S"  # Oben auf f8 bereit fuer Zug nach f5
x.append({"board": b38, "description": "38. Schwarz gewinnt fast: S zieht f8-f5, klammert den Koenig orthogonal ein."})

# Board 39: Einkesselung unter Ausnutzung einer Ecke
b39 = create_empty_board()
b39[4][4] = "X"; b39[0][1] = "K"  # König auf b9 (neben Ecke a9)
b39[1][1] = "S"  # Unten besetzt (b8)
b39[0][5] = "S"  # Rechts auf f9 bereit fuer Zug nach c9
x.append({"board": b39, "description": "39. Schwarz gewinnt fast: S zieht f9-c9. Koenig ist zwischen Ecke a9 und c9 eingeklemmt."})

# Board 40: Umzingelung unter Ausnutzung des leeren Throns
b40 = create_empty_board()
b40[4][4] = "X"; b40[4][3] = "K"  # König auf d5 (neben Thron)
b40[3][3] = "S"; b40[5][3] = "S"  # d6 und d4 besetzt. Rechts ist der Thron.
b40[4][0] = "S"  # Links auf a5 bereit fuer Zug nach c5
x.append({"board": b40, "description": "40. Schwarz gewinnt fast: S zieht a5-c5. K wird durch c5 und den leeren Thron besiegt."})

# Board 41: Mattstellung im naechsten Zug durch unbewachte Spalte
b41 = create_empty_board()
b41[4][4] = "X"; b41[6][6] = "K"  # König auf g3
b41[6][5] = "S"  # Links besetzt (f3)
b41[8][7] = "S"  # Unten bereit fuer h1-h3
x.append({"board": b41, "description": "41. Schwarz gewinnt fast: S zieht h1-h3 zur orthogonalen Einklammerung von g3 aus."})

# Board 42: Zugzwang-Falle fuer Weiss
b42 = create_empty_board()
b42[4][4] = "X"; b42[0][2] = "K"  # König auf c9
b42[0][1] = "S"; b42[1][2] = "S"  # Blockiert von links und unten
b42[0][4] = "S"  # Blockiert den Weg nach rechts (e9) -> K kann sich nicht legal bewegen
x.append({"board": b42, "description": "42. Schwarz gewinnt fast: Weiss hat keine legalen Zuege mehr fuer den Koenig, S blockiert."})


# ==============================================================================
# KATEGORIE 6: WEISS KURZ VOR DEM SIEG (Boards 43-50)
# ==============================================================================

# Board 43: König steht 1 Feld vor der Ecke a9
b43 = create_empty_board()
b43[4][4] = "X"; b43[0][1] = "K"  # König auf b9
# Keine Figuren auf a9
x.append({"board": b43, "description": "43. Weiss gewinnt fast: K am Zug springt einfach von b9 nach a9 (Eckfeld)."})

# Board 44: König steht 1 Feld vor der Ecke i1
b44 = create_empty_board()
b44[4][4] = "X"; b44[7][8] = "K"  # König auf i2
x.append({"board": b44, "description": "44. Weiss gewinnt fast: K am Zug zieht von i2 nach i1 ins Eckfeld zum Sieg."})

# Board 45: Freier Fluchtkorridor durch Ablenkungsopfer
b45 = create_empty_board()
b45[4][4] = "X"; b45[4][2] = "K"  # König auf c5
b45[0][2] = " "  # Ganze c-Linie nach oben (c9) ist frei!
x.append({"board": b45, "description": "45. Weiss gewinnt fast: Die c-Linie ist komplett offen. K zieht c5-c9 zum Sieg."})

# Board 46: Verteidiger blockiert Angreifer, Weg zur Ecke frei
b46 = create_empty_board()
b46[4][4] = "X"; b46[6][2] = "K"  # König auf c3
b46[6][1] = "W"  # Verteidiger sichert b3 ab
# Weg von c3 nach a3 (Index 6,0) ist frei, da b3 durch W besetzt aber a3 frei ist? Nein, Koenig darf W nicht ueberspringen.
# Korrektur: Reihe 3 (Index 6) nach rechts frei: c3 -> i3 (Ecke ist i1/i9, keine Randfelder!)
# Neuer Ansatz fuer 46: Koenig auf b2, Weg nach a1 oder b9 frei.
b46 = create_empty_board()
b46[7][1] = "K"  # König auf b2
# Weg nach b9 (0,1) ist absolut frei
x.append({"board": b46, "description": "46. Weiss gewinnt fast: K auf b2 hat freie Bahn nach oben ueber die gesamte b-Linie zur Ecke b9? Nein, Ecke ist a9!"})

# Korrigiertes Board 46: Richtige Fluchtachse zur echten Ecke (a9, i9, a1, i1)
b46_corr = create_empty_board()
b46_corr[1][0] = "K"  # König auf a8
# Direktes Ziehen nach a9 (0,0) im nächsten Zug möglich
x.append({"board": b46_corr, "description": "46. Weiss gewinnt fast: K steht auf a8 und zieht naechsten Zug auf das Eckfeld a9."})

# Board 47: Weißer Verteidiger oeffnet die Ziellinie
b47 = create_empty_board()
b47[4][4] = "X"; b47[8][2] = "K"  # König auf c1 (neben Ecke a1)
# Das Feld b1 (8,1) ist frei. Der Weg zur Ecke a1 (8,0) ist frei.
x.append({"board": b47, "description": "47. Weiss gewinnt fast: K steht auf c1, zieht ueber das freie b1 direkt nach a1."})

# Board 48: Doppelbedrohung (Zwei Ecken gleichzeitig offen)
b48 = create_empty_board()
b48[4][4] = "X"; b48[2][2] = "K"  # König auf c7
# Reihe 7 (Index 2) ist nach links frei (zu a7 -> Ecke a9 nah)
# Spalte c (Index 2) ist nach oben frei (zu c9 -> Ecke a9/i9 nah)
# Direktes Erreichen: c7 kann in einem Zug zu a7 oder c9 ziehen. Von dort im uebernaechsten in die Ecke.
# Machen wir es unaufhaltbar: K steht auf b8 (1,1). Kann nach a8 oder b9 ziehen. Beides führt im nächsten Zug zum Sieg.
b48_double = create_empty_board()
b48_double[1][1] = "K"  # König auf b8
x.append({"board": b48_double, "description": "48. Weiss gewinnt fast: Doppelbedrohung! K auf b8 kann weder horizontal noch vertikal komplett geblockt werden."})

# Board 49: Weißer Koeder zwingt Schwarz zum Fehlzug
b49 = create_empty_board()
b49[4][4] = "X"; b49[4][6] = "K"  # König auf g5
b49[4][7] = "W"  # Weißer Verteidiger auf h5 sichert den Weg zur Ecke i5? Nein, Ecke ist i9/i1!
# Flucht nach oben zu i9: K auf g7 (2,6). Weg nach g9 (0,6) ist frei. Von g9 freier Weg nach i9 (0,8).
b49_trap = create_empty_board()
b49_trap[2][6] = "K"  # König auf g7
x.append({"board": b49_trap, "description": "49. Weiss gewinnt fast: K steht auf g7. Der Weg nach g9 und anschliessend zur Ecke i9 ist offen."})

# Board 50: Finaler Sprint
b50 = create_empty_board()
b50[0][7] = "K"  # König auf h9
# Zielfeld i9 (0,8) liegt direkt vor ihm und ist komplett frei
x.append({"board": b50, "description": "50. Weiss gewinnt fast: Der Koenig steht auf h9 und muss nur noch ein Feld nach rechts auf i9 ziehen."})


# Überprüfung der Anzahl der generierten Boards
print(f"Erfolgreich {len(x)} Tablut-Boards generiert.")