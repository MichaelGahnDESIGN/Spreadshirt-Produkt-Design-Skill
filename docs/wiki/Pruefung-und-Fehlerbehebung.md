# Prüfung und Fehlerbehebung

Befehle aus dem geklonten Repository mit eingerichteter Python-Umgebung ausführen.

## Druck-PNG

```bash
.venv/bin/python skills/spreadshirt-product-design/scripts/check_print_png.py \
  /pfad/druck.png --width-cm 28
```

Nur Breite angegeben: Höhe wird proportional aus den Motivgrenzen errechnet. Beide Maße angegeben: Verzerrung wird geprüft. Ohne Zielgröße nur maximale rechnerische Größe anzeigen und fehlende Zielprüfung warnen.

Der Bericht enthält Pixelmaße, Motivgrenzen, Transparenz, Dateigröße, effektive dpi, benötigte Zielpixel und den Anteil halbtransparenter sichtbarer Pixel. Keine Bildänderung oder Übertragung.

## Werbeexports

```bash
.venv/bin/python skills/spreadshirt-product-design/scripts/check_social_assets.py \
  /pfad/Artikel/werbung
```

Alle fünf Presetdateien nötig; Maße, PNG, RGB/RGBA und vollständig gedeckter Werbehintergrund werden geprüft. Für andere vereinbarte Maße eine Projektpresetdatei mit `--presets` übergeben, nicht nur Grenzen ändern, damit ein fehlerhafter Export besteht.

## Exit-Codes

`0`: automatische Checks bestanden, manuelle Prüfungen bleiben nötig. `1`: Kriterium verletzt. `2`: Aufruf/Datei nicht verarbeitbar. „Bestanden“ bedeutet weder Spreadshirt-Annahme noch Plattformfreigabe.

## Typische Fehler

- Zu wenig Motivpixel: kleinere belegte Größe nennen oder geeigneten Master erstellen. Nur DPI hochsetzen reicht nicht.
- Weißer Hintergrund: echte Freistellung herstellen, Motivweiß erhalten.
- Viele halbtransparente Pixel: Bild auf Zieltextil beurteilen, flächige Ausläufe von geglätteten Kanten unterscheiden.
- Falsche Werbemaße: Layout korrekt neu exportieren; kein verzerrendes Strecken.
- Fehlendes Bildwerkzeug: klar benennen. Prompts sind keine fertig exportierten Grafiken.
- Falscher Text im Mockup: korrigieren, nicht wegen guter Bildwirkung ignorieren.
- Unklarer Produktartikel: Konzept kennzeichnen, tatsächliche Variante und Druckfläche vor Verkauf prüfen.
- Fehlender KI-Hinweis: direkt im Bild plus geeignete Begleit-/Plattformangaben vorbereiten.

Der Prüfer erkennt nicht alle Freistellungsfehler, Rechteprobleme, Typografiemängel oder KI-bedingten Produktabweichungen. Sichtprüfung, Editor und realer Probedruck bleiben separate Schritte.
