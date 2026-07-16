# Communication - Tablut Game Client

## Übersicht

Dieser Ordner enthält den Client für die Kommunikation mit dem gspy Gameserver. Der Client ermöglicht es, eine KI für das Spiel Tablut gegen andere Spieler oder KIs antreten zu lassen.

## Datei

| Datei | Beschreibung |
|-------|--------------|
| `client.py` | Hauptclient für die Server-Kommunikation und Spielsteuerung |

## Funktionen

### Server-Kommunikation
- **Handshake**: Verbindungsaufbau mit dem gspy-Server
- **Lobby-Management**: Erstellen und Beitreten von Spiel-Lobbys
- **Spielstart**: Starten von Spielen (nur für Lobby-Creator)
- **Spielzug-Übertragung**: Senden und Empfangen von Zügen
- **Zeitmanagement**: Verarbeitung der Zeitkonten

### Spiel-Logik
- **Board-Konvertierung**: Umwandlung zwischen String- und 2D-Board-Format
- **Zug-Kodierung**: Konvertierung von Zügen in Server-Format (`move x1,y1,x2,y2`)
- **Zug-Dekodierung**: Parsen eingehender Züge vom Server
- **Spielerwechsel**: Automatisches Umschalten zwischen Schwarz und Weiß

## Konfiguration

Die folgenden Parameter können in der `client.py` angepasst werden:

| Parameter | Standard | Beschreibung |
|-----------|----------|--------------|
| `GAMETYPE` | `"tablut"` | Spieltyp (tablut, tictactoe, archimedes) |
| `SCHEDULER` | `"random"` | Turnier-Modus (random, classic_tournament, double_tournament, round_robin) |
| `MIN_PLYERS` | `2` | Minimale Spieleranzahl |
| `MAX_PLYERS` | `2` | Maximale Spieleranzahl |
| `HOST` | `"bore.pub"` | Server-Hostname |
| `PORT` | `44843` | Server-Port |

## Ausführung

### Grundlegende Nutzung

```bash
python -m communication.client <lobbyname>
```

### Beispiele

```bash
# Lobby "mein_spiel" erstellen oder beitreten
python -m communication.client mein_spiel

# Lobby "turnier_2026" erstellen oder beitreten
python -m communication.client turnier_2026
```

## Ablauf

1. **Verbindung**: Client verbindet sich mit dem Server
2. **Handshake**: Austausch der Server-Identifikation
3. **Registrierung**: Automatische Registrierung und Login
4. **Lobby**: Erstellen oder Beitreten einer Lobby
5. **Spielstart**: 
   - Creator startet das Spiel (`start`-Befehl)
   - Teilnehmer warten auf Spielbeginn
6. **Spiel**: 
   - Zugwechsel zwischen Spielern
   - Automatische KI-Züge über `alphaBetaWithPVS`
   - Zeitkontrolle über Server
7. **Spielende**: Ausgabe des Ergebnisses

## Spielzug-Verarbeitung

### Eigenen Zug senden
```python
# KI berechnet besten Zug
alphaBetaWithPVS.iterative_deepening(board, config.onTurn, time)

# Zug in Server-Format konvertieren
convert_move = encode_move(config.bestMove)

# Zug senden
client.send(f"{convert_move}\n")
```

### Gegnerzug empfangen
```python
# Move vom Server empfangen (z.B. "move 4,4,4,5")
response = client.recv()

# Zug dekodieren und Board aktualisieren
getMove = decode_move(response)
makeMove.updateBoard(board, getMove)
```

## Server-Protokoll

### Wichtige Server-Befehle

| Befehl | Beschreibung |
|--------|--------------|
| `gspy` | Handshake-Initialisierung |
| `register` | Client-Registrierung |
| `login <token>` | Client-Login |
| `create <lobbyname>` | Lobby erstellen |
| `join <lobbyname>` | Lobby beitreten |
| `ls` | Lobbys auflisten |
| `set game.type <typ>` | Spieltyp setzen |
| `set scheduler <modus>` | Turnier-Modus setzen |
| `start` | Spiel starten |
| `move x1,y1,x2,y2` | Zug ausführen |

### Server-Antworten

| Antwort | Bedeutung |
|---------|-----------|
| `ok` | Erfolgreiche Operation |
| `queued` | Spiel wurde in Warteschlange gestellt |
| `start` | Spiel beginnt |
| `wait` | Warten auf Gegnerzug |
| `over` | Spiel beendet |
| `err 'invalid move or not your turn'` | Ungültiger Zug |
| `err 'time account exceeded'` | Zeit überschritten |

## Fehlerbehandlung

- **Verbindungsfehler**: Automatische Fehlermeldung bei Server-Erreichbarkeit
- **Ungültige Züge**: Server sendet Fehlermeldung zurück
- **Zeitüberschreitung**: Automatische Niederlage bei Zeitablauf
- **Falscher Spieltyp**: Programm beendet sich bei abweichendem Spieltyp

## Abhängigkeiten

Der Client benötigt folgende Module aus dem `src`-Verzeichnis:
- `config`: Spielkonfiguration
- `makeMove`: Zug-Ausführung
- `debug`: Debug-Funktionen
- `alphaBetaWithPVS`: KI-Algorithmus (Principal Variation Search)
- `checkBoard`: Spielstandsprüfung

## Hinweise

- Der Client verwendet aktuell `alphaBetaWithPVS` als Standard-KI
- Die Lobby muss existieren oder wird automatisch erstellt
- Der Creator muss das Spiel starten (`start`-Befehl)
- Nach Spielende wird das Ergebnis auf der Konsole ausgegeben