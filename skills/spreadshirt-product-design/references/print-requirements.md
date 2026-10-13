# Druckanforderungen und Größenrechnung

Stand der zuletzt gelesenen offiziellen Quellen: 13. Oktober 2026. Vor endgültiger Übergabe aktuell prüfen; Produkteditor und produktspezifische Druckflächen zusätzlich beachten.

## PNG / Digitaldruck

[Offizielle Pixelgrafik-Anforderungen](https://service.spreadshirt.com/hc/de/articles/360012941280-Pixelgrafiken-f%C3%BCr-den-Druck-optimieren): PNG/JPG/BMP/GIF, maximal 10 MB, höchstens 4000 × 4000 Pixel, mindestens 200 dpi bezogen auf die Druckgröße. Freigestellte Motive als transparente PNG im RGB-Modus hochladen. Die Limits gelten je Bildachse; quadratische Bilder sind keine Pflicht.

Formeln:

- benötigte Motivpixel = Druckgröße in cm / 2,54 × 200; aufrunden.
- effektive dpi = vorhandene Motivpixel / (Druckgröße in cm / 2,54).
- maximal belegte Größe in cm = vorhandene Motivpixel / 200 × 2,54.

Bei 30 cm Motivbreite mindestens 2363 Motivpixel. DPI-Metadaten ändern die Anzahl der vorhandenen Pixel nicht. Ein 4000-Pixel-Bild mit 2000 Pixel breitem Motiv liefert für dieses Motiv nur 2000 Pixel.

Breite und Höhe proportional planen. Rechenwerte gelten für die Motivgrenzen; die Anwendung im Produkteditor anhand der tatsächlichen Platzierung prüfen. Maximale Pixelzahl ist keine erlaubte physische Druckfläche für jedes Produkt.

Halbtransparente Farbverläufe können auf dunklen Textilien die weiße Unterlegung sichtbar machen. Das bedeutet nicht, dass jede geglättete Kante falsch ist. Sichtprüfung auf Zieltextil und Druckprobe sind entscheidend. RGB-Dateien und ausreichenden Kontrast nutzen; Bildschirmfarben sind keine garantierten Druckfarben.

## Vektor / Plottdruck

[Offizielle Vektorgrafik-Anforderungen](https://service.spreadshirt.com/hc/de/articles/360012941260-Vektorgrafiken-f%C3%BCr-den-Druck-optimieren): SVG, AI oder CDR; maximal 38 × 38 cm, empfohlene Größe 28 × 28 cm. Höchstens drei Farben, je Farbe eine Ebene. Texte und Objekte als geschlossene Pfade, keine überflüssigen Überlappungen. Linien/Motivteile mindestens 1,5 mm und Zwischenräume mindestens 1 mm. Ankerpunkte reduzieren; Quelle nennt maximal 2000 je Farbe.

Diese Werte gehören zum Plottdruck. Nicht jedes komplexe Digitaldruckmotiv braucht eine solche Vektorfassung. Ein automatisch nachgezeichnetes Motiv kann zu viele Knoten und zu dünne Teile enthalten. Der PNG-Prüfer validiert keine Vektordateien.
