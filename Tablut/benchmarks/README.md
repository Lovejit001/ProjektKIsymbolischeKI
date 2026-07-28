# Tablut - KI Benchmark Suite

## Übersicht

Diese Suite enthält verschiedene Benchmark-Tools zur Evaluation und Visualisierung von KI-Algorithmen für das Spiel Tablut. Die implementierten KI-Verfahren umfassen:

- **Alpha-Beta ** (Basisimplementierung)
- **Alpha-Beta mit Move Ordering**
- **Alpha-Beta mit Move Ordering und Transposition Table**
- **Alpha-Beta mit Move Ordering, Transposition Table und Principal Variation Search (PVS)**
- **Monte Carlo Tree Search (MCTS)**

## Projektstruktur

```
Tablut/
├── benchmarks/
│   ├── bewertungsfunktion.py    # Benchmark der Bewertungsfunktion
│   ├── gewinnrate.py            # KI vs KI - Win-Rate Tests
│   ├── iterative_Search_Exp1.py # Iterative Deepening Experiment 1
│   ├── Mst2_3.py                # Iterative Deepening Experiment 2
│   ├── Mst4.py                  # MCTS Benchmark
│   ├── speedtest.py             # Geschwindigkeitstests aller KIs
│   ├── testboard_for2Graph.py   # Testboards für Visualisierungen
│   ├── testboards_winRate.py    # Testboards für Win-Rate Tests
│   ├── visual_node.py           # Visualisierung evaluierter Zustände
│   ├── visual_time.py           # Visualisierung der Suchzeiten
│   └── visual_WinRate.py        # Visualisierung der Win-Rate Matrix
└── src/                         # Quellcode der KI-Algorithmen
```

## Voraussetzungen

- Python 3.8+
- matplotlib
- numpy

Installation der Abhängigkeiten:
```bash
pip install matplotlib numpy
```

## Testboards

Die Tests verwenden verschiedene vordefinierte Boards mit steigender Komplexität:

- **testboard_speedtest.py**: 10 Boards für Geschwindigkeits- und Zustandsvizualisierungen
- **testboards_winRate.py**: 100 Boards für Win-Rate Analysen

## Ausführung

**Wichtig:** um die Benchmarks ausführen zu können muss sichergestellt werden, dass man im Path .\Tablut ist

```bash
cd Tablut/
```

### 1. Bewertungsfunktion Benchmark
```bash
python -m benchmarks.bewertungsfunktion
```
Führt 10.000 Evaluationen der Bewertungsfunktion durch und misst die Zeit.

### 2. Iterative Deepening Experimente
```bash
python -m benchmarks.iterative_Search_Exp1
python -m benchmarks.Mst2_3
python -m benchmarks.Mst4
```
Analysiert das iterative Deepening-Verhalten der verschiedenen KI-Algorithmen.

### 3. Geschwindigkeitstests
```bash
python -m benchmarks.speedtest
```
Vergleicht die Suchgeschwindigkeit aller KI-Implementierungen auf verschiedenen Boards.

### 4. Win-Rate Tests
```bash
python -m benchmarks.gewinnrate
```
Lässt KI-Agenten gegeneinander spielen und ermittelt die Gewinnraten.

## Visualisierungen

Die folgenden Skripte erstellen Grafiken zur Analyse der Ergebnisse:

### Suchzeiten (visual_time.py)
```bash
python -m benchmarks.visual_time
```
Zeigt die Suchzeiten der Algorithmen über verschiedene Board-Komplexitäten.

### Evaluierte Zustände (visual_node.py)
```bash
python -m benchmarks.visual_node
```
Vergleicht die Anzahl evaluierter Zustände pro Algorithmus.

### Win-Rate Matrix (visual_WinRate.py)
```bash
python -m benchmarks.visual_WinRate
```
Erstellt eine Heatmap der Gewinnraten zwischen den KI-Agenten.

## Wichtige Hinweise

- Einige Skripte importieren aus `src.*` Modulen - diese müssen im Projekt vorhanden sein
- Die Win-Rate Tests können je nach Komplexität mehrere Minuten dauern
- Für MCTS werden Simulationszahlen (z.B. 1000-2000) verwendet

## Ergebnisse

Die Ergebnisse der Benchmarks werden in den Visualisierungen dargestellt:

1. **Zeitvergleich**: Suchzeit in Sekunden pro Board
2. **Zustandsvergleich**: Anzahl evaluierter Zustände
3. **Win-Rate**: Prozentuale Siegquoten zwischen Algorithmen (je Zeile gegen je Spalte)

## Konfiguration

Anpassbare Parameter in den Benchmark-Skripten:

- `time_limit`: Maximale Suchzeit pro Zug
- `max_depth`: Maximale Suchtiefe
- `number_simulations`: Anzahl MCTS-Simulationen
- `iterations`: Anzahl Wiederholungen für Geschwindigkeitstests

## Benchmark Ergebnisse

![Gewinnwahrscheinlichkeit der KI (Zeileneintrag) gegen der anderen KI (Spalteneintrag)](winRate.jpg)

![Laufzeitvergleich der KI-Algorithmen](speedtest.jpg)