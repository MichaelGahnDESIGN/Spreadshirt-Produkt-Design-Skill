# Werbepaket für jedes Produktmotiv

## Umfang und Formatstatus

Standardmäßig fünf Plattformgrafiken in jeweils zwei Fassungen erstellen, also zehn Social-Bilddateien. Maßdefinitionen stehen zentral in `social-presets.json`. Dies sind konfigurierbare Arbeitsformate für statische Werbegrafiken, keine Garantie für jedes Konto, jede Anzeigenart oder jedes Placement. Organische Beiträge und bezahlte Anzeigen unterscheiden. Ohne Anzeigenauftrag ein organisch nutzbares Werbepaket vorbereiten, keine Kampagne schalten.

| Datei | Gestaltung |
| --- | --- |
| instagram-feed.png | Hochformat 4:5, großes Produkt oder Motiv, knappe prägnante Headline |
| instagram-story.png | Vollbild 9:16, Produkt, kurze Headline, CTA außerhalb der UI-Ränder |
| facebook-feed.png | Quadrat 1:1, verständliche Produktbotschaft, Shirt/Hoodie gut erkennbar |
| facebook-story.png | Vollbild 9:16, plattformspezifische CTA-Prüfung |
| pinterest-pin.png | Hochformat 2:3, suchorientierter Produktkontext, klare Marke, gut lesbarer Titel |

Quelle/Prüfstand 13. Oktober 2026:

- [Pinterest Creative Best Practices](https://business.pinterest.com/en-gb/creative-best-practices/): 2:3, zum Beispiel 1000 × 1500 Pixel, Produkt als Hauptmotiv, Branding und kurze gut lesbare Texte. Öffentlich gelesen.
- [Pinterest Produktspezifikationen](https://help.pinterest.com/en/business/article/pinterest-product-specs): konkrete Anzeigenart prüfen.
- [Meta Instagram Feed](https://www.facebook.com/business/ads-guide/update/image/instagram-feed), [Facebook Feed](https://www.facebook.com/business/ads-guide/update/image/facebook-feed) und [Instagram Story](https://www.facebook.com/business/ads-guide/update/image/instagram-story): beim letzten Abruf Login-/Zugriffssperre, Werte nicht live bestätigt. Meta-Presets daher als Arbeitsformate, nicht als verifiziert aktuelle Anzeigenpflicht behandeln. Für bezahlte Anzeigen das konkrete Placement im aktuellen Ads Guide/Ads Manager prüfen.

Bei gesperrten Quellen nicht wiederholt versuchen oder Angaben aus Sekundärseiten als offizielle Bestätigung ausgeben. Konkrete Benutzerformate gehen vor; angepasste Presets als separate Projektdatei speichern und mit `--presets` prüfen.

## Ein zusammengehöriges Set gestalten

Produkte und Druckmotiv sind die Hauptdarsteller. Die Marke und die Atmosphäre des Motivs bestimmen Hintergrund, Farben und Typografie. Für Gothic etwa dunkle elegante Inszenierung, für humorvolle Motive ein leichterer Ton. Keine Gothic-Vorgabe für alle Nutzer.

Feed: ein klarer Blickfang, ein lesbarer Motivname und kurze Handlungsaufforderung. Story: großes Produkt, kurze Botschaft, ausreichend freie Bereiche für App-Bedienelemente. Pinterest: bildstarker, suchorientierter Titel und ein Produktkontext, der auch ohne Caption verständlich ist.

Für Storys als interne konservative Layoutreserve oben und unten jeweils etwa 15 Prozent und seitlich 5 Prozent freihalten. Das ist eine Gestaltungsreserve, keine offiziell bestätigte feste Safe Zone. Aktuelle App-/Anzeigenvorschau zusätzlich ansehen; wichtige Elemente nicht unter Buttons, Profilzeilen oder Linkstickern platzieren. Schrift auf Smartphonegröße prüfen.

Ein hochwertiges Set braucht keinen eigenen KI-Aufruf pro Format. Identische Storygestaltung kann für beide Plattformen verwendet werden, wenn Text und Ränder passen. Wiederverwendung dokumentieren. Möglichst exakt erhaltene Motiv-/Produktbilder mit sauber gesetzten Texten kombinieren; keine verzerrte Druckgröße, erfundene Details oder falsch geschriebene Marken zulassen.

## Wahrheitsgemäße Aussagen

Nur bestätigte Angaben nutzen: Produkttyp, Textilfarbe, Motiv und Marke. Keine erfundenen Rabatte, Bewertungen, „Bestseller“, limitierte Auflage, Nachhaltigkeits-/Qualitätsversprechen, Lieferzeiten oder Materialien. Goldfarbe ist kein metallischer Golddruck. Preise, Launchtermine und tatsächliche Bestellbarkeit brauchen eine Quelle aus dem Nutzerauftrag oder geprüften Shopdaten.

Ohne Shoplink einen textlichen Platzhalter `[PRODUKTLINK]` in `texte.md` verwenden. Ohne belegte Verfügbarkeit keine Grafik mit „Jetzt kaufen“ als fertige Werbung ausgeben. Stattdessen eine Konzept-/Teaserfassung mit neutraler Aussage wie „Entdecke das Motiv“ und den offenen Veröffentlichungsschritt dokumentieren. Platzhalter gehören nicht in endgültige Grafikexporte.

Für bezahlte Anzeigen Zombie-/Horrormotive und weitere sensible Bildinhalte gezielt an den aktuellen Plattformrichtlinien prüfen. Keine Zulässigkeit aus erfolgreichem Bildexport ableiten. Das Produktdesign nicht still entschärfen; gegebenenfalls separate mildere Werbeversion vorschlagen.

## Texte und Produktdaten

`texte.md` enthält getrennte Abschnitte:

- Instagram: Caption mit passendem Hook, kurzer Motivbeschreibung, CTA, wenigen relevanten Hashtags und Alttext.
- Facebook: eigenständiger verständlicher Post, CTA, bestätigter Link oder markierter Platzhalter und Alttext.
- Pinterest: suchorientierter Titel, Beschreibung, Linkfeld und Alttext; kein bloßer Instagram-Hashtagblock.
- Produkt: vorgeschlagener Name, kurze sachliche Produktbeschreibung, sinnvolle Suchbegriffe. Unbekannte Material-/Pflegeinformationen offen lassen.

Texte sind Entwürfe bis Links, Produktdaten und Verfügbarkeit bestätigt sind. Sprache aus dem Auftrag übernehmen. Alttexte beschreiben visuell, ohne Keyword-Spam. Maximallängen bei tatsächlicher Veröffentlichung aktuell prüfen.

## Ablage und Abnahme

```text
werbung/
├── instagram-feed.png
├── instagram-story.png
├── facebook-feed.png
├── facebook-story.png
├── pinterest-pin.png
├── texte.md
└── PRUEFUNG.md
```

Optional Quelldatei und maschinenlesbaren Check ergänzen. Keine leeren Platzhalterdateien als Deliverables zählen.

`PRUEFUNG.md` nennt tatsächliche Maße, verfügbare Produkte, Motivtreue, Schreibweise, Lesbarkeit, UI-Ränder, Quellenstand, Wiederverwendungen und offene Fakten. Je Asset Status `Entwurf`, `technisch geprüft` oder `in Plattformvorschau geprüft`. PNG-Export ist keine Werbefreigabe. Keine Veröffentlichung, Ads-Buchung oder Kontoverbindung ohne entsprechende Beauftragung.

## Marketingqualität statt Motivplakat

Vor der Erstellung je Motiv einen kurzen Kampagnenplan in `werbung/KAMPAGNE.md` festhalten: Zielgruppe, konkretes Kommunikationsziel, Bildidee je Plattform, Hook und belegbarer CTA. Ohne bestätigte Bestellbarkeit lautet das Ziel z. B. Interesse am Design statt Kaufabschluss.

Produkt als groß erkennbaren Hauptdarsteller inszenieren. Lifestyle oder hochwertige Still-Life-Aufnahme wählen, wenn es Marke und Motiv hilft. Keine standardmäßige Formel „riesiges Motiv, kleine Kleidungsminiaturen, langer Titel“. Nicht jedes Format bekommt identische Layouts: Instagram kann Atmosphäre und Stil tragen, Facebook das Produktangebot verständlich zeigen, Pinterest eine konkrete Outfit-/Motivinspiration liefern. Hook knapp halten, Motivname und Details bei Bedarf in Caption verschieben. Ein klarer visueller Fokus, bewusst genutzter Freiraum und höchstens wenige Schriftgrößen.

Realistisch wirkende KI-Menschen und Produktaufnahmen nach [ai-transparency.md](ai-transparency.md) kennzeichnen. Vor einer echten Werbung konkrete Kleidungsmodelle und belegte Druckgrößen als Referenz verwenden. Eine große Fantasie-Druckfläche nicht als reales Leistungsversprechen präsentieren.

Im Prüfbericht pro Grafik bewerten: Produkt auf den ersten Blick erkennbar? Motiv gut sichtbar? Hook und CTA auf Smartphone lesbar? Eigener Nutzen/Anlass erkennbar? Bild-/Textgewicht passend? Ränder und KI-Hinweis sichtbar? Marken- und Motivtreue? Unbelegte Behauptungen entfernt? Mindestens eine sichtbare Gegenprüfung durchführen. Falsche Marken-/Produktangaben, irreführende Behauptungen und fehlende nötige Kennzeichnungen immer korrigieren, auch wenn es nur ein Fehler ist. Werden zwei rein gestalterische Kernpunkte verfehlt, die Gestaltung zusätzlich überarbeiten statt nur technisch korrekt exportieren. Kein Erfolg oder Conversion-Uplift ohne Daten versprechen.

## Export mit und ohne untere Textboxen

Pro Produktansicht und Plattformgrafik beide Fassungen aus demselben Layout ausgeben:

- **Mit-Textboxen:** unterer Informationsbereich mit Motiv-/Produktname, passendem CTA sowie zutreffendem KI- und Konzeptstatus.
- **Ohne-Textboxen:** unteren Informationsbereich entfernen. Bei Social-Grafiken obere Headlines, Branding und seitliche Markenzeile erhalten. Produktbilder können ohne angehängten Footer direkt aus der unveränderten Quelle ausgegeben werden.

Für beide Fassungen dieselbe Bildquelle und identische Motivdarstellung verwenden. Keine Neugenerierung des Produkts nur zum Entfernen des Footers. Produktbilder dürfen durch Weglassen des angehängten Footers kürzer werden; Social-Grafiken behalten ihre definierten Plattformmaße. Originale erhalten und die Varianten eindeutig ablegen:

```text
Varianten/
├── README.md
├── Mit-Textboxen/
│   ├── produktbilder/             # je beauftragtem Produkttyp ein PNG
│   └── werbung/                   # alle fünf Plattform-PNGs
└── Ohne-Textboxen/
    ├── produktbilder/
    └── werbung/
```

Bei Shirt und Hoodie: 14 PNG-Exporte je Motiv, davon zehn Social-Grafiken. Native Quelldateien mit getrennten Bild- und Textebenen nach Möglichkeit beilegen. Die Variantenübersicht verlinkt jede Datei und erklärt, welche Texte entfernt wurden. Beide Social-Ordner separat mit `check_social_assets.py` prüfen; Maßkontrolle und Sichtprüfung im Artikel-Prüfbericht dokumentieren.

Herkunfts- und Prüfhinweise bleiben in Begleitdateien erhalten. Die footerfreie Arbeitsfassung ist nicht automatisch veröffentlichungsfertig: Bei erforderlicher direkter Bildkennzeichnung oder greifender konservativer Skillpraxis vor Veröffentlichung einen separaten lesbaren Bildhinweis außerhalb der entfernten Textbox ergänzen. Den Status je Fassung dokumentieren; keine Befreiung aus dem fehlenden Footer oder einem Anime-Look ableiten. Caption, Plattformlabel und Bildhinweis erfüllen unterschiedliche Aufgaben; siehe `ai-transparency.md`.
