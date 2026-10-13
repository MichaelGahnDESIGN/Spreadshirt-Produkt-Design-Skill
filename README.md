<!-- MGD-HEADER -->
<p align="center"><a href="https://Michael-Gahn.de"><img src="assets/mgd-logo.png" alt="Michael Gahn DESIGN" width="48"></a></p>
<p align="center"><img src="assets/banner.svg" alt="Spreadshirt Produktdesign Skill" width="100%"></p>
<p align="center">
  <img alt="Lizenz MIT" src="https://img.shields.io/badge/Lizenz-MIT-green">
  <img alt="Version" src="https://img.shields.io/badge/Version-0.4.0-blue">
  <img alt="Sprache" src="https://img.shields.io/badge/Sprache-Deutsch-2f6fed">
  <a href="https://Michael-Gahn.de"><img alt="by Michael Gahn DESIGN" src="https://img.shields.io/badge/by-Michael%20Gahn%20DESIGN-cd1616"></a>
</p>
<!-- /MGD-HEADER -->

# Spreadshirt Produkt Design Skill

**Aus einer Idee oder Bildinspiration wird ein eigenes Produktmotiv – mit separater Druckdatei, Shirt-/Hoodie-Vorschau, Social-Media-Werbegrafiken und nachvollziehbarer Dateiprüfung.**

Ein deutschsprachiger Skill für Codex und andere KI-Agenten mit Skill-Unterstützung. Er verbindet kreative Gestaltung mit der Vorbereitung von Spreadshirt-Druckdateien. Die allgemeine Version enthält keine feste Marke, Stilrichtung, Kundendaten oder lokalen Benutzerpfade.

> [!NOTE]
> Version **0.4.0** ergänzt verbindliche Marketingqualitätsprüfung und nachvollziehbare KI-Kennzeichnung für Produkttexte und Social-Grafiken. Eine attraktive Vorschau ist keine Druckfreigabe: Auflösung, Transparenz, Motivgröße und Produktplatzierung werden getrennt bewertet. Die Veröffentlichung des Repositorys bleibt eine Entscheidung des Eigentümers.

## Was der Skill leistet

- Bildreferenzen ansehen und deren gewünschte Merkmale in eine eigene Komposition übersetzen.
- Marke, exakte Texte, Produktarten, Shirtfarbe und Speicherort aus deinem Auftrag übernehmen.
- Detailreiche Digitaldruckmotive oder reduzierte Vektormotive passend zum Auftrag vorbereiten.
- Jedes Produktmotiv in einem eigenen Ordner mit Quelle, Druckdatei und Prüfstand ablegen.
- Tatsächliche Pixelgröße, Dateigröße, Transparenz und effektive Auflösung bezogen auf die Motivfläche prüfen.
- Shirt- und Hoodie-Vorschauen getrennt von den Druckdateien erstellen.
- Zu jedem neuen Motiv automatisch fünf Werbegrafiken für Instagram, Facebook und Pinterest sowie plattformgerechte Texte, Alttexte und Produkttext-Entwürfe liefern.
- Fehlende Masterauflösung, Druckproben und unbestätigte Produktplatzierung sichtbar benennen.

Der Skill ist für Gothic, Gaming, Metal, Humor, minimalistische Motive und andere Richtungen nutzbar. Er erzwingt keine bestimmte Ästhetik.

## Was du benötigst

Ein KI-Agent mit Datei- und Bildwerkzeugen. Für KI-generierte Motive braucht die Umgebung ein geeignetes Bildgenerierungswerkzeug. Der Skill selbst liefert weder Bildmodell noch API-Schlüssel und installiert kein kostenpflichtiges Abo. Auch vorhandene eigene Illustrationen und Vektordateien können als Ausgangspunkt dienen.

Für den mitgelieferten PNG-Prüfer: **Python 3.10 oder neuer und Pillow**. Die Prüfung läuft lokal, liest die Datei und überträgt nichts. Browserzugriff ist hilfreich, um aktuelle Spreadshirt-Vorgaben zu bestätigen. Offline stehen datierte Quellen zur Verfügung; dann bleibt der Vorgabenstand unbestätigt.

## Installation

### Codex

Repository klonen und den vollständigen Skillordner kopieren:

```bash
git clone https://github.com/MichaelGahnDESIGN/Spreadshirt-Produkt-Design-Skill.git
mkdir -p ~/.codex/skills
cp -R Spreadshirt-Produkt-Design-Skill/skills/spreadshirt-product-design ~/.codex/skills/
```

Solange das Repository privat ist, benötigt das Klonen einen berechtigten GitHub-Zugang. Einen bereits installierten gleichnamigen Skill vor dem Kopieren prüfen und gegebenenfalls sichern. Je nach Agent/App eine neue Sitzung öffnen, damit der Skill entdeckt wird.

### Claude Code und andere Agenten

Für Claude Code den Ordner beispielsweise nach `~/.claude/skills/spreadshirt-product-design` kopieren. Für eine projektlokale Installation den Skillordner in den vom jeweiligen Agenten unterstützten Skillpfad legen. Kopiere nicht nur `SKILL.md`: Referenzen und Prüfer gehören dazu. Werkzeugnamen können je nach Umgebung abweichen; der Skill setzt kein bestimmtes Bildmodell voraus.

### Python-Prüfer vorbereiten

Im geklonten Repository, optional mit isolierter Python-Umgebung:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r skills/spreadshirt-product-design/requirements.txt
```

Unter Windows heißt der Interpreter `.venv\Scripts\python.exe`. Die Paketinstallation benötigt Netzwerkzugriff; der anschließende Prüfer nicht.

## So benutzt du den Skill

```text
Nutze $spreadshirt-product-design.
Entwickle aus diesem Bild eine eigene Gothic-Zombie-Krähe für meine Marke NIGHTFORGE.
Schwarze Shirts und Pullover-Hoodies, Frontmotiv etwa 25 cm breit.
Markenname exakt NIGHTFORGE. Speichere jedes Motiv unter Produkte/ in einem eigenen Ordner.
Erstelle transparente Druckdatei, Vorschau und Prüfbericht.
```

Du kannst auch ein vollständig neues Motiv ohne Bildreferenz beauftragen:

```text
Nutze $spreadshirt-product-design für ein minimalistisches Gaming-Motiv.
Ein eigener Würfel mit dem Text „Noch ein Versuch“. Helles Shirt, Brustmotiv 20 cm breit.
Bitte eine reduzierte Vektorfassung prüfen, falls die Werkzeuge das unterstützen.
```

Bei einer Referenz ist hilfreich: Was gefällt dir konkret – Stimmung, Farben, Figur, Detailgrad oder Bildaufbau? Gib möglichst Textilfarbe und gewünschte Druckgröße an. Falls diese fehlen, arbeitet der Agent mit benannten Annahmen statt eine Druckgröße zu erfinden.

## Ablauf vom Briefing bis zur Ausgabe

1. **Briefing:** Marke, Text, Motiv, Referenzen, Produkte und Ausgabeziel aus dem Gespräch erfassen.
2. **Eigenständiger Entwurf:** eine passende Komposition entwickeln und Referenzen entsprechend ihrer Rolle verwenden.
3. **Druckdatei:** transparentes Motiv für den Digitaldruck oder echte Pfade für geeignete Vektormotive vorbereiten.
4. **Technik und Sichtprüfung:** Dateiwerte messen, Motiv auf der Zieltextilfarbe ansehen, Text und Details prüfen.
5. **Produktvorschau:** Front-/Rückenansichten getrennt erzeugen; beim Hoodie Taschen, Kordeln und Reißverschlüsse beachten.
6. **Werbepaket:** Feed-/Story-Grafiken für Instagram und Facebook sowie einen Pinterest-Pin mit Texten und Alttexten exportieren.
7. **Übergabe:** Dateien, passende Druckgröße, Werbeexports, offene Prüfungen und Status nennen.

Der Skill veröffentlicht keine Shopangebote und bestellt keine Produkte ohne entsprechenden Auftrag. Das Erstellen eines Designs erteilt keine automatische Verkaufs- oder Veröffentlichungsfreigabe.

## Ein Ordner je Motiv

```text
Produkte/
└── 001-zombie-kraehe/
    ├── druck/
    │   └── motiv-schwarzes-textil.png
    ├── vorschau/
    │   └── shirt-und-hoodie.png
    ├── werbung/
    │   ├── instagram-feed.png
    │   ├── instagram-story.png
    │   ├── facebook-feed.png
    │   ├── facebook-story.png
    │   ├── pinterest-pin.png
    │   ├── texte.md
    │   └── PRUEFUNG.md
    ├── METADATEN.md
    ├── PRODUKTBESCHREIBUNG.md
    ├── TAGS.md
    ├── QUELLE.md
    ├── PRUEFUNG.md
    └── pruefung.json
```

Die Struktur ist ein Vorschlag. Bestehende Projektkonventionen und der gewünschte Zielordner gehen vor. Druckdatei und Vorschau bleiben unterscheidbar. Entwürfe dürfen im Ordner liegen, werden aber nicht als fertige Druckmaster bezeichnet.

## Marketingqualität und KI-Transparenz

Die Werbung startet mit einem kurzen Kampagnenplan: Zielgruppe, Kommunikationsziel, Hook, Bildidee und CTA je Plattform. Große nachvollziehbare Produktinszenierung ersetzt den Standard aus Motivplakat und winzigen Produktminiaturen. Lifestyle, Still Life und Outfitinspiration werden bewusst gewählt; Lesbarkeit, Motivtreue und visueller Fokus zusätzlich zu den Pixelmaßen geprüft. Eine Kampagne verspricht keine unbelegten Verkaufs- oder Conversionerfolge.

Fotorealistische KI-Models und KI-Produktmockups bekommen als konservative Standardpraxis einen sichtbaren Bildhinweis, etwa **„KI-generiertes Model · Produktvisualisierung“**. Passende Angaben werden in Captions und für vorhandene Plattformoptionen vorbereitet. Am Ende der kopierbaren Produkttexte steht bei einem KI-Motiv ein zutreffender Gestaltungshinweis. `KI-TRANSPARENZ.md` dokumentiert den Herstellungsweg und offene Veröffentlichungsschritte.

Diese Praxis ist keine pauschale Rechtsgarantie: gesetzlicher Tatbestand, Zielmarkt, Plattformregeln und freiwillige Kennzeichnung bleiben getrennt. Eine Beschreibung allein ersetzt keine erforderliche direkte Bildoffenlegung. Ein Label macht eine irreführende Darstellung des Produkts nicht zulässig. Vollständig menschlich erstellte Motive erhalten keinen falschen KI-Hinweis. [Quellen, Beispiele und Grenzen](skills/spreadshirt-product-design/references/ai-transparency.md).

## Produkttexte, SEO und Tags als Markdown

Jeder Artikelordner erhält automatisch **METADATEN.md**, **PRODUKTBESCHREIBUNG.md** und **TAGS.md**. Darin liegen kopierbare Designfelder, eigenständige Texte für Shirt und Hoodie sowie priorisierte Motiv-Tags. Tatsächliche Zeichenzahlen und offene Produktfakten stehen außerhalb der kopierbaren Felder.

Wichtig ist die Trennung: Spreadshirt beschreibt ein kurzes Designfeld mit bis zu 200 Zeichen; ein längerer redaktioneller Shoptext gehört dort nicht hinein. Die offiziellen Hinweise empfehlen kurze eindeutige Designnamen, präzise Tags ohne Dopplungen und natürliche Sprache statt Keyword-Spam. Längere Produkttitel und variantenspezifische Texte werden separat vorbereitet. [Quellen und Arbeitsregeln](skills/spreadshirt-product-design/references/spreadshirt-seo.md).

Der Skill formuliert motivbezogene Marketingtexte und passende Suchphrasen. Er erfindet keine Materialien, Passformen, Kindergrößen, Suchvolumina oder Verkaufsversprechen. Felder und Funktionen im konkreten Partnerbereich werden vor Veröffentlichung geprüft; der Skill verspricht weder vollständiges Anbieterwissen noch garantierte Rankings.

## Automatisches Werbepaket

**Werbegrafiken gehören jetzt zu jedem neuen Produktmotiv dazu**, ohne zusätzlichen Auftrag. Nur wenn du ausdrücklich „nur Druckdatei“ oder „keine Werbung“ möchtest, entfallen sie. Bei einer kleinen Korrektur wird das vorhandene Set entsprechend angepasst; alte Motive werden nicht automatisch nachbearbeitet.

| Plattform und Einsatz | Produktionsformat | Datei |
| --- | --- | --- |
| Instagram Feed | 1080 × 1350 px, 4:5 | instagram-feed.png |
| Instagram Story | 1080 × 1920 px, 9:16 | instagram-story.png |
| Facebook Feed | 1080 × 1080 px, 1:1 | facebook-feed.png |
| Facebook Story | 1080 × 1920 px, 9:16 | facebook-story.png |
| Pinterest Standard-Pin | 1000 × 1500 px, 2:3 | pinterest-pin.png |

Das sind konfigurierbare Produktionspresets, keine garantierten Anforderungen für jedes Anzeigenplacement. Die Meta-Vorgaben waren beim Abruf am 13. Oktober 2026 durch eine Login-/Zugriffssperre nicht live bestätigbar. Pinterest empfiehlt öffentlich 2:3 beziehungsweise 1000 × 1500 Pixel. Quellen und Unterschiede zwischen organischen Posts und bezahlten Anzeigen stehen in [der Werbereferenz](skills/spreadshirt-product-design/references/social-creative.md).

Jede Grafik wird für ihr Format gestaltet: ein klarer Blickfang im Feed, großzügige UI-Ränder in Storys und ein suchorientierter Produktkontext für Pinterest. Passende Storylayouts dürfen wiederverwendet werden, werden aber separat exportiert. Das Produktmotiv bleibt erkennbar und wird nicht für jede Plattform neu erfunden.

`werbung/texte.md` enthält Instagram-Caption, Facebook-Post, Pinterest-Titel und -Beschreibung, Alttexte, CTA und bestätigte Links beziehungsweise eindeutig markierte Linkplatzhalter. Dazu kommen ein vorgeschlagener Produktname, kurze Produktbeschreibung und Suchbegriffe. Keine erfundenen Preise, Rabattaktionen, Materialien, Lieferzeiten oder Verkaufsfreigaben. Fehlende Fakten blockieren die Veröffentlichung, nicht die Erstellung eines klar gekennzeichneten Entwurfs.

Die Werbedateien lassen sich rein lesend prüfen:

```bash
.venv/bin/python skills/spreadshirt-product-design/scripts/check_social_assets.py \
  /pfad/Produkte/001-motiv/werbung
```

Der Prüfer erwartet alle fünf Dateien und kontrolliert tatsächliche Pixelmaße, PNG-Format, RGB/RGBA und einen vollständig gedeckten Hintergrund. Er bewertet nicht die Gestaltung, Texte, Shopverfügbarkeit oder Plattformannahme. Exit-Codes entsprechen dem PNG-Prüfer: `0` für bestandene automatische Checks, `1` für verletzte Exportkriterien, `2` für einen nicht verarbeitbaren Aufruf.

Für andere gewünschte Maße eine eigene Presetdatei auf Grundlage von [social-presets.json](skills/spreadshirt-product-design/references/social-presets.json) anlegen und mit `--presets /pfad/presets.json` prüfen. Druckauflösung und Bildschirmauflösung bleiben getrennt: ein gutes Werbebild macht einen zu kleinen Druckmaster nicht druckfertig.

Keine automatische Veröffentlichung auf sozialen Plattformen, keine Anzeigenbuchung und keine Bestellung. Bei fehlenden Bildwerkzeugen benennt der Agent den Blocker; fünf Prompts gelten nicht als fünf fertige Grafiken.

## Druckvorgaben: Quelle statt Vermutung

Der Skill prüft vor der finalen Ausgabe die aktuellen offiziellen Anforderungen. Den datierten Ausgangsstand und die Größenformeln enthält [die Druckreferenz](skills/spreadshirt-product-design/references/print-requirements.md).

Für Digitaldruck ist eine transparente RGB-PNG der bevorzugte Export für freigestellte Illustrationen. Stand 13. Oktober 2026: maximal 10 MB, höchstens 4000 Pixel je Achse, mindestens 200 dpi bei der geplanten Größe. Weißer Hintergrund wird mitgedruckt; er ist keine Transparenz. [Offizielle Pixelgrafik-Vorgaben](https://service.spreadshirt.com/hc/de/articles/360012941280-Pixelgrafiken-f%C3%BCr-den-Druck-optimieren).

Beim Plottdruck gelten andere Grenzen: echte Vektorpfade, bis zu drei Farben und Mindeststärken für Motivteile. Detaillierte Illustrationen müssen dafür häufig vereinfacht werden. [Offizielle Vektorgrafik-Vorgaben](https://service.spreadshirt.com/hc/de/articles/360012941260-Vektorgrafiken-f%C3%BCr-den-Druck-optimieren).

> [!IMPORTANT]
> 4000 × 4000 Pixel ist eine Obergrenze und keine Pflichtgröße. Eine quadratische Datei ist nicht erforderlich. DPI-Metadaten oder einfaches Hochskalieren erzeugen keine zusätzlichen Originaldetails. Die erlaubte physische Druckfläche hängt vom gewählten Produkt ab.

## Der lokale PNG-Prüfer

```bash
.venv/bin/python skills/spreadshirt-product-design/scripts/check_print_png.py \
  /pfad/zum/motiv.png --width-cm 28 --height-cm 35
```

Breite und Höhe beziehen sich auf die **sichtbaren Motivgrenzen ohne leeren Außenrand**. Wenn du nur ein Maß angibst, berechnet das Skript das andere proportional:

```bash
.venv/bin/python skills/spreadshirt-product-design/scripts/check_print_png.py \
  /pfad/zum/motiv.png --width-cm 28
```

Ohne Maßangabe zeigt es die maximal rechnerisch belegte Motivgröße bei 200 dpi und warnt, dass keine konkrete Zielgröße geprüft wurde. Ergebnis als JSON ausgeben und bei Bedarf außerhalb der Druckdatei speichern:

```bash
.venv/bin/python skills/spreadshirt-product-design/scripts/check_print_png.py \
  /pfad/zum/motiv.png --width-cm 28 > /pfad/zum/pruefung.json
```

| Exit-Code | Bedeutung |
| --- | --- |
| `0` | Automatische Dateichecks bestanden; Warnungen und manuelle Prüfungen beachten |
| `1` | Ein überprüfbares Dateikriterium verletzt |
| `2` | Aufruf oder Datei konnte nicht verarbeitet werden |

Konfigurierbare Grenzwerte: `--min-dpi`, `--max-pixels`, `--max-bytes`. Änderungen müssen mit aktuellen Vorgaben begründet werden, nicht nur eine fehlerhafte Datei künstlich bestehen lassen.

Der Prüfer erkennt unter anderem fehlende Transparenz, leere Bilder, übergroße Dateien, zu wenige Motivpixel und verzerrende Zielmaße. Er erkennt **keine** Rechteprobleme, Druckfarben, veraltete Limits, versteckten weißen Hintergrund innerhalb des Motivs oder die ursprüngliche Qualität hochskalierter Daten. Er validiert keine SVG-/AI-/CDR-Dateien und erteilt keine Spreadshirt-Freigabe.

### Ein reales Größenproblem

1122 × 1402 Motivpixel reichen bei 200 dpi ungefähr für **14,25 × 17,81 cm**. Bei 28 cm Motivbreite sind es nur rund 102 dpi. Ein großer Druck kann in der KI-Vorschau überzeugend aussehen, obwohl die Datei dafür nicht ausreicht. Der Skill muss diesen Unterschied sichtbar benennen.

## Qualität auf Shirts und Hoodies

Für schwarze Textilien müssen helle Details die Form tragen. Für helle Textilien kann eine eigene dunkle Variante nötig sein. Eine bloße Farbumkehr kann Augen, Konturen und Schatten verfälschen und ist immer visuell zu prüfen.

Produktvorschauen sind Darstellungen, keine Maß- oder Farbnachweise. KI-Mockups können Texte, Details und Druckgrößen verändern. Maßhaltige Platzierung wird im tatsächlichen Spreadshirt-Produkteditor geprüft. Die Wirkung feiner Details und das Druckergebnis lassen sich abschließend nur an einer realen Produktprobe beurteilen.

## Status klar unterscheiden

| Status | Was er belegt |
| --- | --- |
| Entwurf | Gestaltung vorhanden, Druckkriterien ggf. offen |
| Technisch geprüft für konkrete Größe | Dateikriterien und dokumentierte Sichtprüfung erfüllt |
| Im Produkteditor geprüft | Platzierung und verfügbare Druckfläche kontrolliert |
| Physisch probegedruckt | Reales Textil, Farben und Details beurteilt |

Ein Status ersetzt den nächsten nicht. Fehlende Werkzeuge oder zu geringe Auflösung sind offen auszuweisen.

## Rechte und Datenschutz

Referenzen können fremde Werke sein. Sie sind Inspiration, kein automatischer Nachweis von Verkaufs-, Marken- oder Exklusivrechten. Der Skill verlangt eigenständige Gestaltungen und dokumentiert bekannte Nutzungsrechte, ohne eine rechtliche Freigabe zu behaupten. Das Entfernen eines Wasserzeichens macht eine fremde Vorlage nicht frei nutzbar.

Keine persönlichen Daten, Kontozugänge oder privaten Kundenreferenzen in Skill-Repositories übernehmen. Die MIT-Lizenz dieses Projekts gilt für den Skillcode und die Dokumentation; sie erteilt keine pauschalen Rechte an fremden Referenzen, Schriften, Marken oder später erzeugten Produktmotiven.

## Repository-Struktur

```text
Spreadshirt-Produkt-Design-Skill/
├── README.md
├── LICENSE
├── assets/                         # MGD-Logo und README-Banner
├── skills/spreadshirt-product-design/
│   ├── SKILL.md                    # kompakter Agenten-Einstieg
│   ├── agents/openai.yaml          # Codex-Anzeige und Beispielaufruf
│   ├── requirements.txt
│   ├── references/
│   │   ├── print-requirements.md
│   │   ├── workflow-examples.md
│   │   ├── spreadshirt-seo.md
│   │   ├── ai-transparency.md
│   │   ├── social-creative.md
│   │   └── social-presets.json
│   └── scripts/
│       ├── check_print_png.py      # Druckprüfung
│       └── check_social_assets.py  # Werbeexports prüfen
└── tests/                         # lokale Dateitests
```

## Entwicklung und Tests

```bash
.venv/bin/python -m unittest discover -s tests -v
```

Die Tests verwenden selbst erzeugte temporäre Bilder und prüfen Motivgrenzen, ausreichende Auflösung, DPI-Metadaten, Transparenz inklusive Paletten-PNG, leere Bilder, Größenlimits, Seitenverhältnis und unveränderte Eingabedateien. Zusätzliche Werbetests prüfen das vollständige Fünferpaket, falsche Maße, fehlende Dateien, ungewollte Transparenz und ungültige Presets. Sie benötigen weder Bildgenerierung noch Shopzugang.

Für Codex kann zusätzlich der Validator des installierten `skill-creator` auf `skills/spreadshirt-product-design` angewendet werden. Er prüft die Skillstruktur, keine reale Druckqualität.

## Verwandte MGD-Projekte

- [MGD CI Designmanual](https://github.com/MichaelGahnDESIGN/MGD_CI-Designmanual): Markenregeln, Farben und Gestaltung systematisch festhalten.
- [ChatGPT Video Composer Skill](https://github.com/MichaelGahnDESIGN/ChatGPT-Video-Composer-Skill): Produkt- und Markenclips erstellen.
- [MGD AI PlayTest Skill](https://github.com/MichaelGahnDESIGN/MGD_AI-PlayTest_SKILL): Funktionen und Abläufe aus Nutzersicht prüfen.

Diese Ergänzungen sind optional; der Produktdesign-Skill funktioniert unabhängig davon.

## Lizenz und Herausgeber

[MIT](LICENSE) © 2026 [Michael Gahn DESIGN](https://Michael-Gahn.de).

Unabhängiges Community-Projekt, kein offizieller Spreadshirt-Skill und keine Verbindung zum Anbieter. Spreadshirt wird als Zielplattform genannt.

Herausgeber und Kontakt: [Michael Gahn DESIGN](https://Michael-Gahn.de) · [Impressum](https://michael-gahn.de/impressum/).
