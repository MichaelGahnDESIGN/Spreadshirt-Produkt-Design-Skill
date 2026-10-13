# Installation und Umgebung

## Unterstützte Nutzung

Claude Code und Codex mit Dateizugriff können lokale Skills verwenden. In einem normalen ChatGPT-Browserchat ist kein globaler lokaler Skill installiert, auch wenn die Anleitung in den Chat kopiert wird. Fähigkeit und verfügbares Bildwerkzeug zuerst prüfen.

Der kopierbare Installationsprompt steht am Anfang der Repository-README.

## Globale Installation

Repository klonen:

```bash
git clone https://github.com/MichaelGahnDESIGN/Spreadshirt-Produkt-Design-Skill.git
```

Codex, wenn `CODEX_HOME` nicht gesetzt ist:

```bash
mkdir -p ~/.codex/skills
cp -R Spreadshirt-Produkt-Design-Skill/skills/spreadshirt-product-design ~/.codex/skills/
```

Ist `CODEX_HOME` gesetzt, verwende dessen `skills/`-Unterordner. Claude Code:

```bash
mkdir -p ~/.claude/skills
cp -R Spreadshirt-Produkt-Design-Skill/skills/spreadshirt-product-design ~/.claude/skills/
```

Die Beispiele setzen voraus, dass noch keine gleichnamige Installation existiert. Bestehende Inhalte vor einem Update prüfen und sichern. Nicht nur SKILL.md kopieren: Referenzen, Skripte, UI-Metadaten und requirements.txt werden benötigt. Neue Sitzung öffnen, wenn die Agentenoberfläche den Skill nicht sofort entdeckt.

## Voraussetzungen

Für Gestaltung: geeignete Bild-/Vektor-/Layoutwerkzeuge in deiner Umgebung. Der Skill setzt keinen Anbieter voraus und liefert keine API-Schlüssel. Für lokale Prüfungen: Python ab 3.10 und Pillow.

Im geklonten Repository:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r skills/spreadshirt-product-design/requirements.txt
```

Unter Windows `.venv\Scripts\python.exe` verwenden. Installation der Abhängigkeiten braucht Netzwerk; die Prüfskripte arbeiten danach lokal und rein lesend.

## Updates

Aktuellen Repository-Stand holen, eigene Anpassungen der installierten Fassung prüfen und den vollständigen neuen Skillordner übernehmen. Keine zusätzliche kostenpflichtige Infrastruktur erforderlich. Lokale Produktordner gehören nicht in die Skillinstallation.
