# Projekt-KI---symbolische-K-nstliche-Intelligenz
Projekt KI - symbolische Künstliche Intelligenz -> Tablut Projekt | Gruppenmitglieder: Bilal, Emanuel und Lovejit



Zum testen der Unittests die in tests\test_positions.py erstellt wurden: python -m unittest tests.test_positions


Testcoverage prüfen :

# 1. Zuerst neue Tests AUSFÜHREN (neue Daten sammeln)
python -m coverage run -m unittest tests/test_attack.py

# 2. DANN HTML Report aktualisieren
python -m coverage html

# 3. Optional: Terminal Report mit neuen Daten
python -m coverage report --show-missing