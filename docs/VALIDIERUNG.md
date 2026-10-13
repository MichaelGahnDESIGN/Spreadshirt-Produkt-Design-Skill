# Validierung – 0.1.0

Stand: 13. Oktober 2026.

- Skill-Creator-Validator: bestanden.
- Acht Unit-Tests des PNG-Prüfers: bestanden.
- Relative Dokumentationslinks: vorhanden.
- MGD-Logo: gültige Bilddatei, aus öffentlichem MGD-Skill übernommen.
- Realer lokaler PNG-Durchlauf: transparenter Entwurf mit 1121 × 1402 Motivpixeln. Bei 28 cm Breite korrekt abgelehnt (101,69 dpi), bei 14 cm Breite automatische Checks bestanden (203,38 dpi). Keine Kundendatei in dieses Repository kopiert.
- Unabhängiger rein lesender Agentendurchlauf: keine blockierenden Skillfehler; unzureichende Masterauflösung korrekt benannt. Daraus ergänzt: benötigte Zielpixel und Anteil teiltransparenter sichtbarer Pixel im Bericht.

Die Prüfung verwendet die vorhandene lokale Pillow-Installation. Eine frische Installation aller unterstützten Python-/Pillow-Kombinationen wurde nicht getestet. Die dokumentierten CLI-Optionen wurden mit realen PNG-Daten verwendet; keine externe Bildgenerierung für den Skilltest, keine Shopaktion und keine Produktbestellung.

Nicht bestätigt: tatsächlicher Textildruck, Spreadshirt-Annahme einer erzeugten Produktdatei, Qualität zukünftiger Bildmodelle oder zukünftige Anbieterlimits. Der Skill trennt diese Nachweise ausdrücklich.

## Erweiterung 0.2.0 – Werbepaket

Automatische Werbeexports für Instagram-Feed/-Story, Facebook-Feed/-Story und Pinterest-Pin ergänzt. Dazu getrennte Veröffentlichungstexte, Alttexte, Pinterest-Titel und Produkttext-Entwürfe. Kleinere Korrekturen aktualisieren das vorhandene Set; expliziter Verzicht auf Werbung bleibt möglich.

- 14 Unit-Tests einschließlich sechs neuer Werbeexport-Tests bestanden.
- Skill-Creator-Validator und relative Dokumentationslinks geprüft.
- PNG-Werbeprüfer arbeitet rein lesend, prüft fünf Dateien und tatsächliche Maße, Format und Farbraum; verhindert transparente Werbehintergründe.
- Pinterest-Best-Practices öffentlich gelesen. Meta-Ads-Guide beim Abruf login-/zugriffsgesperrt; Meta-Maße als Produktionspresets dokumentiert und nicht als live bestätigte Pflichtwerte ausgegeben.
- Tests nutzen ausschließlich selbst erzeugte temporäre Farbflächen. Eine echte Fünferkampagne wurde für diese Skilländerung nicht gerendert oder veröffentlicht; Layoutqualität und Plattformannahme dadurch nicht belegt.
- Unabhängiger rein lesender Agentendurchlauf für ein Produktbriefing ohne Shoplink/Preis sowie „nur Druckdatei, keine Werbung“: vollständiges Standardpaket, Faktenplatzhalter und Scope-Ausnahme korrekt erkannt. Keine blockierenden Widersprüche; engeren Nutzerauftrag zusätzlich im Einstieg klargestellt.

## Erweiterung 0.3.0 – Produkttexte und Metadaten

Eigene METADATEN.md, PRODUKTBESCHREIBUNG.md und TAGS.md pro Artikel ergänzt. Quellenstand 13. Oktober 2026: offizielle Spreadshirt-Metadatenhilfe sowie Spreadshop-Metadaten-/SEO-Hinweise gelesen. Kurze Designfelder und redaktionelle Produkttexte werden unterschieden; die empfohlene Titellänge ist kein erfundenes hartes Limit. Keine maximale Tagzahl oder Suchvolumina erfunden.

14 Dateitests, Skill-Creator-Validator und Diffprüfung bestanden. Praktische Anwendung außerhalb dieses Repositorys: winterliches Aquarellmotiv für helle Textilien, fünf native Werbelayouts mit unverändert eingebundener Illustration, korrekte Exportmaße und separate Textdateien. Designbeschreibung 167 Zeichen, Designname 21 Zeichen. Produktdateien und private Referenzen werden nicht im allgemeinen Skillrepository veröffentlicht.

Druckfreigabe und Shopveröffentlichung nicht erfolgt. Die erzeugte Illustration reicht nativ bei 200 dpi nur für ungefähr 14,25 × 17,81 cm; groß dargestellte Mockups sind Konzepte. Tatsächliche Produktvarianten und Alters-/Größenangebote bleiben vor Verkauf zu prüfen.

Unabhängige rein lesende Textgegenprüfung: Designfelder, Zeichenzahlen, Tagtrennung und fehlende Fakten korrekt; einen internen Produktionshinweis aus dem Hoodie-Kundentext entfernt und die Trennung als Referenzregel ergänzt. Keine blockierenden Skillwidersprüche festgestellt.

## Erweiterung 0.4.0 – Marketing und KI-Transparenz

Kampagnenplan, Produktinszenierung und sichtbare Qualitätsabnahme ergänzt. KI-Model-/Mockup-Hinweise direkt am Export, Caption und zusätzliche Gestaltungshinweise am Ende kopierbarer Produkttexte; KI-TRANSPARENZ.md je Artikel. Rechtliche Verpflichtung, Plattformregel und freiwillige Skillpraxis getrennt; keine Rechtsgarantie.

Quellen: EU-Kommissions-Suchauszüge zu Artikel 50, öffentlich gelesener EU AI Act Service Desk, aktualisierter Meta-GenAI-Werbetransparenzbeitrag und Pinterest Gen-AI-Labels. FAQ-Vollabruf zeitweise 429; konkreter Rechtsfall und Plattformupload bleiben separat zu prüfen.

14 Tests und Skill-Validator bestanden. Fünf neue PNG-Werbeexports für den Winterraben außerhalb des Skillrepositorys geprüft, produktbezogene Lifestyle-/Stilllife-Kompositionen und sichtbare KI-Hinweise erstellt. Unabhängiger Lesetest bestätigt Scope und Transparenzabgrenzung. Die Abnahmeregel wurde geschärft: ein einzelner Wahrheits-/Pflichtfehler genügt für Korrektur; zwei gestalterische Schwächen lösen zusätzliche Layoutüberarbeitung aus.

Keine gemessene Marketingperformance, echte Produktprüfung oder Rechtsabnahme. Produktmodell und große Druckfläche bleiben als ungeprüft gekennzeichnet. Private Produktbilder und synthetische Modelbilder werden nicht in dieses allgemeine Skillrepository übernommen.
