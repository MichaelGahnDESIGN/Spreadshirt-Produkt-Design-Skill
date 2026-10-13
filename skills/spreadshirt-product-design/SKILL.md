---
name: spreadshirt-product-design
description: Entwickle eigene Spreadshirt-Motive aus Briefings oder Bildreferenzen und liefere getrennte Druckdateien, Produktvorschauen und nachvollziehbare Dateiprüfungen für Shirts und Hoodies. Für Gestaltung und Druckvorbereitung, nicht für automatische Shopveröffentlichung.
---

# Spreadshirt Produktdesign

Entwickle eigenständige, zur gewünschten Marke passende Motive. Liefere pro Motiv einen eigenen Ordner mit Druckdatei, Vorschau und ehrlichem Prüfstand. Marke, Stil, Sprache und Speicherort kommen aus dem Auftrag; keine feste Marke oder Ästhetik vorgeben.

## Briefing und Referenzen

Übernimm bekannte Wünsche aus dem Gespräch: Motiv, Markenname und exakte Schreibweise, Produkte, Textilfarbe, Vorder-/Rückseite, gewünschte Motivgröße und Zielordner. Fehlende unkritische Angaben als Annahme dokumentieren. Ohne Größenangabe zunächst einen Entwurf erstellen und die maximal belegte Druckgröße nennen; keine große Druckfreigabe erfinden.

Referenzen zunächst ansehen. Atmosphäre, Bildaufbau, Detailgrad und konkrete bevorzugte Merkmale herausarbeiten. Referenzen sind Inspiration, sofern nicht ausdrücklich eine Bearbeitung beauftragt wird. Eigenständige Figur und Komposition entwickeln; Wasserzeichen und fremde Logos nicht als nutzbare Assets behandeln. Keine exklusiven Rechte oder rechtliche Freigabe allein aus KI-Erzeugung ableiten.

## Gestaltung

- Werkzeuge entsprechend der Umgebung nutzen. Für neue rasterbasierte Motive das verfügbare Bildgenerierungswerkzeug und dessen Skill verwenden, wenn vorhanden. Bestehende echte Vektoren mit einem geeigneten Vektorwerkzeug bearbeiten. Keine feste Anbieter-, API-Key- oder Aboabhängigkeit voraussetzen.
- Ziel: separates Druckmotiv mit echtem transparentem Hintergrund, nicht ein Shirtfoto. Produktvorschauen erst danach erzeugen.
- Auf dunklen Textilien helle Konturen und ausreichend starke Details gestalten. Schwarze Motivflächen können optisch verschwinden. Weißes Motiv und weißer Hintergrund sind verschiedene Dinge.
- Gewünschten Detailgrad erhalten, aber feine Linien, Mikrotexturen und transparente Farbverläufe gezielt prüfen. Plottdruckregeln nicht pauschal auf Digitaldruck anwenden.
- Markenname und Texte visuell auf exakte Schreibweise prüfen. Fehler gezielt korrigieren; keine unveränderten Serien erzeugen. Nach zwei erfolglosen Korrekturen desselben Problems den konkreten Werkzeugblocker nennen und einen geeigneten anderen Weg oder eine klar begrenzte Fassung vorschlagen.

## Druckvorbereitung und Prüfung

Vor der finalen Ausgabe die aktuellen offiziellen Spreadshirt-Anforderungen prüfen. Startwerte und Quellen stehen in [references/print-requirements.md](references/print-requirements.md); Offline-Nutzung als unbestätigten Stand kennzeichnen.

PNG-Digitaldruck ist für detailreiche Illustrationen oft sinnvoll. Vektor-/Plottdruck eignet sich für reduzierte geschlossene Flächen. PNG in SVG einzubetten ist keine Vektorisierung. Bei Plottdruck Pfade, Farben, Linienstärken und Abstände am tatsächlichen Ausgabeformat prüfen.

Die tatsächliche Datei prüfen, nicht nur Prompt und DPI-Metadaten. Für PNG kann der mitgelieferte **rein lesende** Prüfer verwendet werden:

```bash
python3 scripts/check_print_png.py /pfad/druck.png --width-cm 28 --height-cm 35
```

Die Pfade im Beispiel beziehen sich auf diesen Skillordner. Pillow ist nötig; bei fehlender Bibliothek eine vorhandene geeignete Umgebung verwenden oder die Einrichtung mit dem Nutzer abstimmen. Der Prüfer verändert keine Bilder und ruft keine Dienste auf.

Nenne Pixelmaße, Dateigröße, Transparenz, tatsächliche Motivgrenzen, effektive Auflösung bei gewünschter Größe und maximale Größe bei 200 dpi. Gewünschte Breite/Höhe dürfen das Seitenverhältnis nicht unbemerkt verändern. Leerer transparenter Rand zählt nicht als Motivauflösung. Hochskalierung und generierte zusätzliche Details offen ausweisen; sie beweisen keine native Detailqualität. Wenn das Werkzeug zu wenige Pixel liefert, Ergebnis als Entwurf oder nur für die belegte kleinere Größe ausgeben und fehlende Masterauflösung deutlich benennen.

Technikcheck durch Sichtprüfung auf dunklem/hellem Untergrund und in realistischer Größe ergänzen. Transparenzkanal allein beweist keine saubere Freistellung. Antialiasing an Kanten ist zulässig; breite halbtransparente Nebel können Probleme verursachen. Druckbarkeit und Annahme durch Spreadshirt bleiben separate Prüfungen.

## Ablage und Übergabe

Je Motiv einen eindeutig benannten Ordner im vereinbarten Ziel anlegen, etwa `Produkte/001-motivname/`. Bestehende Dateien nicht still überschreiben. Verwende nach Bedarf:

- `druck/`: tatsächlich geprüfte PNGs bzw. echte Vektorfassungen; Entwürfe entsprechend benennen.
- `vorschau/`: Shirt-/Hoodieansichten, klar als Vorschau bezeichnet.
- `QUELLE.md`: Briefing, Generierungs-/Bearbeitungsweg, Referenzrolle und relevante Nutzungsrechte ohne vertrauliche Daten.
- `PRUEFUNG.md` und optional JSON-Prüfbericht: tatsächliche Werte, Zielgröße, angenommene Vorgaben mit Datum/Quelle, Sichtprüfung, offene Punkte und Status.

Für detaillierte Prompts und einen Beispielbericht lies [references/workflow-examples.md](references/workflow-examples.md) nur bei Bedarf.

Vorschauen können Motivdetails, Position und Größe verändern. Mit der Druckdatei vergleichen; nie als maßhaltige Druckprobe ausgeben. Beim Hoodie Kapuze, Kordeln, Tasche und Reißverschluss berücksichtigen. Nicht automatisch von einem Shirt auf alle Produkte schließen.

Am Ende Dateien verlinken, gestalterisches Ergebnis kurz erklären und **Entwurf**, **technisch geprüft für benannte Größe**, **im Produkteditor geprüft** und **physisch probegedruckt** unterscheiden. Keine Veröffentlichung, Bestellung oder Änderung von Shopangeboten ohne entsprechende Beauftragung. Auch bei bestandenen Dateichecks keine Druckabnahme behaupten.
