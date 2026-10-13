---
name: spreadshirt-product-design
description: Erstelle eigene Spreadshirt-Produktmotive mit geprüften Druckdateien, Produktvorschauen, Instagram-/Facebook-/Pinterest-Werbung und SEO-gerechten Titeln, Beschreibungen und Tags als Markdown im Artikelordner. Keine automatische Veröffentlichung.
---

# Spreadshirt Produktdesign

Entwickle eigenständige, zur gewünschten Marke passende Motive. Liefere pro Motiv einen eigenen Ordner mit Druckdatei, Vorschau, Werbepaket und ehrlichem Prüfstand, sofern der Nutzer den Auftrag nicht ausdrücklich enger fasst. Marke, Stil, Sprache und Speicherort kommen aus dem Auftrag; keine feste Marke oder Ästhetik vorgeben.

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
- `werbung/`: standardmäßig die fünf Plattformgrafiken, Texte und Werbeprüfbericht gemäß dem folgenden Abschnitt.
- `METADATEN.md`, `PRODUKTBESCHREIBUNG.md`, `TAGS.md`: standardmäßig Texte gemäß dem Abschnitt zu Produkttexten; nicht ausschließlich in Social-Captions ablegen.
- `QUELLE.md`: Briefing, Generierungs-/Bearbeitungsweg, Referenzrolle und relevante Nutzungsrechte ohne vertrauliche Daten.
- `PRUEFUNG.md` und optional JSON-Prüfbericht: tatsächliche Werte, Zielgröße, angenommene Vorgaben mit Datum/Quelle, Sichtprüfung, offene Punkte und Status.

Für detaillierte Prompts und einen Beispielbericht lies [references/workflow-examples.md](references/workflow-examples.md) nur bei Bedarf.

Vorschauen können Motivdetails, Position und Größe verändern. Mit der Druckdatei vergleichen; nie als maßhaltige Druckprobe ausgeben. Beim Hoodie Kapuze, Kordeln, Tasche und Reißverschluss berücksichtigen. Nicht automatisch von einem Shirt auf alle Produkte schließen.

Am Ende Dateien verlinken, gestalterisches Ergebnis kurz erklären und **Entwurf**, **technisch geprüft für benannte Größe**, **im Produkteditor geprüft** und **physisch probegedruckt** unterscheiden. Keine Veröffentlichung, Bestellung oder Änderung von Shopangeboten ohne entsprechende Beauftragung. Auch bei bestandenen Dateichecks keine Druckabnahme behaupten.

## Werbepaket gehört standardmäßig dazu

Zu jedem neuen Produktmotiv **immer** Werbegrafiken für Instagram, Facebook und Pinterest erstellen, auch wenn der Nutzer nur das Produktdesign nennt. Nur bei ausdrücklich engerem Auftrag, etwa „nur Druckdatei“ oder „keine Werbung“, entfällt es. Bei einer kleinen Motivkorrektur betroffene bestehende Werbedateien aktualisieren statt unnötig eine neue Kampagne anzulegen. Keine Serienproduktion für alte Motive ohne Auftrag.

Lies dafür [references/social-creative.md](references/social-creative.md) einschließlich der Marketingqualitätsprüfung und [references/ai-transparency.md](references/ai-transparency.md). Lege einen kurzen Kampagnenplan an; Produktinszenierung, Hook und CTA müssen plattformspezifisch sinnvoll sein. Keine bloßen Motivplakate mit winzigen Produktminiaturen als Standard. Das Standardpaket enthält fünf Plattformformate mit jeweils zwei tatsächlich exportierten Fassungen: Instagram-Feed und -Story, Facebook-Feed und -Story sowie Pinterest-Pin. Die konfigurierbaren Produktionsmaße liegen in [references/social-presets.json](references/social-presets.json). Feed- und Story-Layouts bewusst komponieren, nicht blind strecken oder wichtige Teile wegschneiden. Gemeinsame Gestaltung für kompatible Placements wiederverwenden; alle Plattformdateien separat benennen.

Zusätzlich erstellen: je Plattform einen passenden Veröffentlichungstext mit CTA und Alttext, für Pinterest einen Titel, sowie kurze Produktbeschreibung und Produktname als Entwurf. Nur belegte Produkteigenschaften, Preise und Verfügbarkeit nennen. Fehlende URLs/Preise als Platzhalter in Textdateien halten und als offene Veröffentlichungsvoraussetzung markieren; keine Platzhalter in fertigen Bildgrafiken und keine erfundenen Angebote. Ist das Motiv noch ein Druckentwurf, auch das Werbepaket als Konzept kennzeichnen und keinen Verkaufsstart suggerieren.

Exaktes Motiv und Markenidentität erhalten. Wenn Werkzeug und Lizenzlage es erlauben, die geprüfte Grafik als unveränderte Ebene in die Werbekomposition einsetzen und Texte sauber setzen. Bei generierten Mockups Motivtreue und Schreibweise vergleichen. Tool-Ausgaben an den tatsächlichen Pixelmaßen prüfen, nicht am gewünschten Prompt. Kein automatischer externer Upload oder kostenpflichtiger Anbieterwechsel zur Fehlerbehebung.

```bash
python3 scripts/check_social_assets.py /pfad/Produkte/001-motiv/werbung
```

Der rein lesende Prüfer kontrolliert die fünf Bilddateien, Maße und RGB-Farbmodus gegen die mitgelieferten Presets. Er prüft keine Werberichtlinien, Textlesbarkeit, Nutzungsrechte, Motivtreue oder Plattformannahme. Diese Punkte separat im Prüfbericht festhalten. Fehlende Dateien oder Werkzeuge offen melden; Prompts allein sind kein fertiges Werbepaket. Offline ausführbare Prüfung ersetzt keine aktuellen Plattformvorgaben.

## Zwei Bildfassungen als fester Standard

Jede Produktvorschau und jede der fünf Social-Grafiken standardmäßig zweimal tatsächlich exportieren: **mit unteren Textboxen** und **ohne unteren Textbereich**. Nur eine ausdrücklich gewünschte einzelne Fassung reduziert diesen Umfang. Dieselbe Bildquelle, Motivposition, Farbgestaltung und Bildqualität verwenden; keine zwei unabhängig generierten Motive. Bei Social-Grafiken obere Headlines, Branding und seitliche Markenzeilen erhalten: „ohne Textboxen“ bedeutet nicht „komplett ohne Text“.

Beide Fassungen getrennt unter `Varianten/Mit-Textboxen/{produktbilder,werbung}/` und `Varianten/Ohne-Textboxen/{produktbilder,werbung}/` im Artikelordner speichern. Bestehende Originale erhalten. Produktbilder ohne Footer können die unveränderte Bildquelle verwenden; Social-Exports behalten die Plattformmaße. Native Layouts mit getrennten Bild- und Textebenen bevorzugen, damit der Footer ohne Veränderung des Motivs entfernt werden kann. Eine Übersicht `Varianten/README.md` mit Links zu beiden Fassungen anlegen.

Die fünf Social-Formate in **beiden** Variantenordnern separat mit dem Exportprüfer prüfen und beide Fassungen sichtbar gegenprüfen. Bei Shirt und Hoodie entstehen standardmäßig 14 PNGs je Motiv: zwei Produktansichten und fünf Social-Grafiken, jeweils zweimal. Druckdateien bleiben separat; sie brauchen keine Werbe-Textboxen.

Kennzeichnungspflichten bleiben unabhängig vom Layout bestehen. Eine Fassung ohne Footer ist keine automatische Veröffentlichungsfreigabe. Herkunft und Prüfstatus in `KI-TRANSPARENZ.md`, Postingtexten und Prüfbericht erhalten. Wenn für einen konkreten Einsatz ein sichtbarer Bildhinweis erforderlich ist oder die konservative Kennzeichnungspraxis dieses Skills greift, vor Veröffentlichung einen separaten lesbaren Hinweis außerhalb der entfernten Textbox vorsehen. Eine Caption ersetzt keine erforderliche direkte Bildkennzeichnung. Details: [references/social-creative.md](references/social-creative.md).

## Produkttexte, Metadaten und Tags gehören zum Artikel

Lies [references/spreadshirt-seo.md](references/spreadshirt-seo.md) und prüfe relevante aktuelle offizielle Hinweise. Unterscheide kurze Design-Metadaten im Partnerbereich von längeren redaktionellen Produkttexten: ein 200-Zeichen-Designfeld bekommt keinen langen Shoptext. Accountsprache übernehmen; Oberfläche und belegte Feldgrenzen gehen vor.

Erstelle in jedem Artikelordner standardmäßig:

- `METADATEN.md`: kopierbarer Designname, kurze Designbeschreibung, Zeichenzahlen und dokumentierter Feld-/Quellenstand.
- `PRODUKTBESCHREIBUNG.md`: eigenständige ansprechende Texte je bestelltem Produkttyp, z. B. Shirt und Hoodie, Produktnamenvorschläge, kurze Einstiegstexte und offene Produktfakten. Hauptsuchbegriff natürlich früh einbauen; sichtbares Motiv und passende Nutzung beschreiben.
- `TAGS.md`: priorisierte relevante Design-Tags zum Kopieren und getrennte interne Long-Tail-Ideen für Produkttitel/Social-Texte. Keine erfundenen Suchvolumina, fremden Marken, Keyword-Dopplungen oder garantierten Rankings. Keine Produktgattungen in Design-Tags, wenn das jeweilige Metadatenfeld diese nicht verlangt.

Emotionale Ansprache mit tatsächlichem Motiv verbinden. Keine geschlechtlichen Klischees erzwingen und keine unbekannte Passform, Größen, Material-, Komfort-, Nachhaltigkeits- oder Produktionsversprechen erfinden. Material, Pflege, Preis und Verfügbarkeit erst mit konkreter Produktquelle ergänzen. „Originalmotiv“ darf eine eigene Markenkomposition beschreiben, beweist aber keine Exklusivität oder Markenprüfung. Markdown-Dateien lokal erstellen ist keine Freigabe zur Änderung veröffentlichter Shoptexte.


## KI-Kennzeichnung und Veröffentlichungsvoraussetzungen

Lies bei KI-generierten/bearbeiteten Assets [references/ai-transparency.md](references/ai-transparency.md). Fotorealistische KI-Menschen und KI-Produktmockups als Standardpraxis direkt lesbar am Bild kennzeichnen; passende Caption und verfügbare Plattform-Labeloptionen zusätzlich vorsehen. Rechtslage, Plattformpflicht und freiwillige Transparenz getrennt dokumentieren. Keine pauschale „rechtssicher“-Behauptung.

Bei KI-generiertem oder wesentlich KI-bearbeitetem Motiv einen zutreffenden kurzen Gestaltungshinweis am Ende jedes kopierbaren Produkttexts ergänzen. Je Artikel `KI-TRANSPARENZ.md` anlegen. Der Beschreibungszusatz ersetzt weder unmittelbare Bildkennzeichnung noch Plattformangaben oder eine Rechtsprüfung im Zielmarkt. Keine falsche Handarbeitsbehauptung, Testimonials oder nachgeahmte echte Identität. KI-Hinweise machen unrealistische Produktdetails nicht wahr.
