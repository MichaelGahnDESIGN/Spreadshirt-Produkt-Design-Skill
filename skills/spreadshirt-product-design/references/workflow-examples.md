# Beispiele für Briefing, Prompt und Prüfstand

## Produktbriefing

> Entwickle für meine Marke NIGHTFORGE eine eigene Gothic-Zombie-Krähe aus dieser Inspiration. Schwarzes Shirt und schwarzer Pullover-Hoodie, Brustmotiv etwa 25 cm breit. Ordner: Produkte/001-zombie-kraehe. Markenname exakt NIGHTFORGE. Zeige Druckmotiv und Produktvorschau getrennt.

Die Marke und das Motiv sind frei austauschbar. Bei mehreren Referenzen deren Rolle benennen: anatomische Referenz, Stimmung, gewünschte Farbwelt oder tatsächliches Bearbeitungsziel.

## Prompt-Grundlage

```text
Zweck: eigenständiges Textildruckmotiv, kein Mockup.
Motiv und Atmosphäre: [gewünschte Figur, Haltung, Stimmung].
Marke/Text exakt: [Text oder ausdrücklich ohne Text].
Referenzen: [Rollen; eigenständige Komposition oder beauftragte Bearbeitung].
Textilfarbe: [Farbe]; Kontraste darauf auslegen.
Bildaufbau: [Hoch-/Querformat, Figur, Rahmen falls gewünscht].
Druckgestaltung: [Detailgrad], klare Motivkanten, relevante Details ausreichend kräftig.
Hintergrund: echte Transparenz; keine gefälschte Schachbrettfläche.
Auflösung: [benötigte Pixel für geplante Größe]; tatsächlichen Export anschließend prüfen.
Vermeiden: [nur auftragsbezogene Ausschlüsse].
```

Eine angeforderte Pixelzahl garantiert nicht, dass das Werkzeug sie liefert. Ein kleines Bild nicht als großen druckfertigen Master ausgeben.

## Beispiel: zu geringe Auflösung

Eine Datei mit 1122 × 1402 Motivpixeln erreicht bei 200 dpi ungefähr 14,25 × 17,81 cm. Für 28 cm Motivbreite sind es nur ungefähr 102 dpi. Konsequenz: Entwurf erhalten, kleinere belegte Druckgröße nennen oder höher aufgelösten Master erstellen und erneut prüfen. Ein hübsches großformatiges Mockup beseitigt diesen Mangel nicht.

## Beispiel für PRUEFUNG.md

```markdown
# Prüfstand

Status: Entwurf; Zielauflösung noch nicht erreicht.
Datei: druck/motiv-entwurf.png
Produkte: schwarzes Shirt und Pullover-Hoodie
Ziel: Brustmotiv 28 cm breit
Dateiwerte: 1122 × 1402 Pixel, RGBA, echte Transparenz vorhanden
Maximal belegte Motivgröße bei 200 dpi: 14,25 × 17,81 cm
Sichtprüfung: Text korrekt; feine Federlinien bei kleiner Ansicht kritisch
Vorschau: KI-generiert, Größe und Motivtreue nicht garantiert
Offen: höher aufgelöster Master, Produkteditor, reale Druckprobe
Vorgaben: Quelle und Prüfdatum angeben
```
