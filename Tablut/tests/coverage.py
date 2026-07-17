#!/usr/bin/env python3
"""
Generiert die Coverage-Tabelle als PNG
Zeigt NUR Game-Logic Dateien (src/gamelogic) aber die Coverage basiert auf den Tests
Speichert als tests/coverage_table.png
"""

import os
import sys
import subprocess
import matplotlib.pyplot as plt
import numpy as np

# Fuege Projekt-Root zum Pfad hinzu
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Mapping: Game-Logic Datei -> zugehörige Test-Datei
TEST_MAPPING = {
    "debug": "test_debug",
    "attack": "test_attack",
    "checkBoard": "test_checkboard",
    "makeMove": "test_makeMove",
    "config": "test_config",
    "positions": "test_positions",
}

# Module die ignoriert werden sollen (0% Coverage oder nicht getestet)
IGNORE_MODULES = [
    "transpositionTable",
    "transpositionTable_array",
    "zugsortierung",
    "evaluateFunction",
    "saveBoardState",
    "__init__"
]

def run_coverage():
    """Führt Coverage neu aus und generiert XML"""
    print("Fuehre Coverage-Analyse neu durch...")
    
    # Alte Coverage-Daten löschen
    for f in [".coverage", "coverage.xml", "coverage_data.json"]:
        if os.path.exists(f):
            os.remove(f)
            print(f"  Geloescht: {f}")
    
    # Alle Test-Dateien die existieren (test_config hinzugefügt)
    test_files = [
        "tests.test_attack",
        "tests.test_checkboard",
        "tests.test_config",      # NEU: test_config hinzugefügt
        "tests.test_debug",
        "tests.test_makeMove",
        "tests.test_moves",
        "tests.test_positions",
        "tests.test_totalMoves",
    ]
    
    # Coverage mit allen Tests ausführen
    cmd = [
        sys.executable, "-m", "coverage", "run",
        "--source=src/gamelogic,tests",
        "-m", "unittest",
        *test_files
    ]
    
    print(f"  Fuehre aus: {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode != 0:
        print("  Tests fehlgeschlagen:")
        print(result.stdout)
        if result.stderr:
            print(result.stderr)
    
    print("  Tests ausgefuehrt")
    
    # XML generieren
    subprocess.run([
        sys.executable, "-m", "coverage", "xml",
        "-o", "coverage.xml"
    ], capture_output=True, check=True)
    
    print("  XML generiert")
    return True

def get_coverage_data():
    """Holt Coverage-Daten aus .coverage"""
    
    try:
        # XML parsen
        import xml.etree.ElementTree as ET
        tree = ET.parse("coverage.xml")
        root = tree.getroot()
        
        results = {}
        
        for package in root.findall(".//package"):
            for cls in package.findall(".//class"):
                filename = cls.get("filename")
                
                # NUR src/gamelogic Dateien (keine tests)
                if "src/gamelogic" in filename and "tests" not in filename:
                    name = filename.split("/")[-1].replace(".py", "")
                    
                    # Ignoriere bestimmte Module
                    if name in IGNORE_MODULES:
                        continue
                    
                    lines = cls.findall(".//line")
                    total = len(lines)
                    covered = sum(1 for line in lines if line.get("hits") != "0")
                    
                    if total > 0:
                        results[name] = {
                            "covered": covered,
                            "total": total,
                            "percent": (covered / total) * 100,
                            "test_file": TEST_MAPPING.get(name, "kein Test")
                        }
        
        return results
        
    except Exception as e:
        print(f"Fehler beim Parsen: {e}")
        return None

def create_coverage_table_png(results):
    """Erstellt die Tabelle als PNG (NUR Game-Logic)"""
    
    if not results:
        print("Keine Coverage-Daten gefunden!")
        return
    
    # Sortiere nach Coverage
    sorted_results = sorted(results.items(), key=lambda x: x[1]["percent"], reverse=True)
    
    # Figure Groesse anpassen
    fig_height = max(6, len(sorted_results) * 0.5 + 2)
    fig, ax = plt.subplots(figsize=(14, fig_height))
    ax.axis('off')
    
    # Tabelle erstellen (mit Test-Datei Spalte)
    table_data = [["#", "Modul", "Covered", "Total", "Coverage", "Getestet von"]]
    
    for i, (m, d) in enumerate(sorted_results, 1):
        p = d["percent"]
        test_file = d["test_file"]
        table_data.append([
            str(i),
            m,
            str(d["covered"]),
            str(d["total"]),
            f"{p:.1f}%",
            test_file
        ])
    
    # Gesamtzeile
    total_covered = sum(d["covered"] for _, d in sorted_results)
    total_total = sum(d["total"] for _, d in sorted_results)
    total_percent = (total_covered / total_total * 100) if total_total > 0 else 0
    table_data.append([
        "",
        "GESAMT",
        str(total_covered),
        str(total_total),
        f"{total_percent:.1f}%",
        ""
    ])
    
    # Tabelle zeichnen
    table = ax.table(
        cellText=table_data,
        loc='center',
        cellLoc='center',
        colWidths=[0.05, 0.25, 0.10, 0.10, 0.12, 0.28]
    )
    
    table.auto_set_font_size(False)
    table.set_fontsize(12)
    table.scale(1, 1.8)
    
    # Header
    for i in range(6):
        table[(0, i)].set_facecolor('#2c3e50')
        table[(0, i)].set_text_props(color='white', fontweight='bold', fontsize=13)
    
    # Zeilen einfarben
    for i in range(1, len(table_data)):
        row_color = '#ecf0f1' if i % 2 == 0 else 'white'
        for j in range(6):
            if j == 4:  # Coverage Spalte
                if i < len(table_data)-1:
                    p = float(table_data[i][4].replace('%', ''))
                else:
                    p = total_percent
                # GRÜN für >=80%, GELB für >=60%, ORANGE für >=30%, ROT für <30%
                if p >= 80:
                    color = '#27ae60'  # Grün
                elif p >= 60:
                    color = '#f39c12'  # Gelb
                elif p >= 30:
                    color = '#e67e22'  # Orange
                else:
                    color = '#e74c3c'  # Rot
                table[(i, j)].set_facecolor(color)
                table[(i, j)].set_text_props(color='white' if p < 60 else 'black', fontweight='bold')
            elif j == 5:  # Test-Datei Spalte
                table[(i, j)].set_facecolor(row_color)
                if i < len(table_data)-1:
                    table[(i, j)].set_text_props(style='italic', color='#7f8c8d')
            else:
                table[(i, j)].set_facecolor(row_color)
                if i == len(table_data)-1:
                    table[(i, j)].set_text_props(fontweight='bold')
    
    ax.set_title(
        "Coverage Report - Game Logic",
        fontsize=18, 
        fontweight='bold', 
        pad=20
    )
    
    plt.tight_layout()
    
    # Speichern im tests/ Ordner
    os.makedirs("tests", exist_ok=True)
    filename = "tests/coverage_table.png"
    plt.savefig(filename, dpi=150, bbox_inches='tight')
    print(f"Gespeichert: {filename}")
    plt.close()
    
    # Konsolenausgabe (NUR Game-Logic)
    print("\n" + "=" * 70)
    print("COVERAGE REPORT - GAME LOGIC")
    print("=" * 70)
    print(f"{'Modul':<20} {'Coverage':>10} {'Getestet von':>25}")
    print("-" * 60)
    for m, d in sorted_results:
        p = d["percent"]
        test_file = d["test_file"]
        print(f"{m:<20} {p:>9.1f}% {test_file:>25}")
    print("-" * 60)
    print(f"{'GESAMT':<20} {total_percent:>9.1f}%")
    print("=" * 70)
    print(f"PNG: {os.path.abspath(filename)}")
    print("=" * 70)

def main():
    print("Generiere Coverage-Tabelle (NUR Game-Logic)...")
    print("=" * 60)
    
    # Coverage neu generieren
    if not run_coverage():
        print("Coverage-Analyse fehlgeschlagen!")
        return
    
    # Daten holen
    results = get_coverage_data()
    
    if results:
        create_coverage_table_png(results)
    else:
        print("Keine Coverage-Daten gefunden!")

if __name__ == "__main__":
    main()