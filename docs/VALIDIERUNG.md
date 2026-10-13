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
