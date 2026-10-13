# Entwicklung und Beiträge

## Quellstruktur

`skills/spreadshirt-product-design/SKILL.md` ist der kompakte Agenteneinstieg. `references/` enthält Druck-, Social-, SEO- und KI-Transparenzregeln, die je Aufgabe geladen werden. `scripts/` enthält rein lesende Prüfer. `agents/openai.yaml` enthält Codex-Anzeige und Beispielaufruf.

README erklärt Einstieg und Installation. Die versionierten Wikiseiten liegen in `docs/wiki/`; dieselben Kapitel werden im GitHub-Wiki gepflegt. Private Produktbilder und Kundendaten gehören nicht ins allgemeine Skillrepository.

## Tests

```bash
.venv/bin/python -m unittest discover -s tests -v
```

14 Tests prüfen Druckauflösung, tatsächliche Motivgrenzen, Transparenz inklusive Palette, leere Bilder, Dateilimits, Seitenverhältnis, unveränderte Eingaben und Vollständigkeit/Formate der Werbeexports. Testbilder werden temporär selbst erstellt; kein Bildmodell oder Shopkonto nötig.

Der Skill-Creator-Validator kann zusätzlich auf den Skillordner angewendet werden. Er prüft die Skillstruktur, keine Marketingqualität oder Rechtskonformität. Änderungen an Anweisungen mit realistischen kleinen Briefings gegenprüfen.

## Beiträge

Konkrete Fehler mit reproduzierbarem Beispiel melden. Keine fremden Referenzbilder ohne Rechte veröffentlichen. Veraltete Anbietergrenzen mit offizieller Quelle und Prüfdatum korrigieren. Regeln nur ergänzen, wenn sie Entscheidungen verbessern; keine pauschalen Ausnahmen oder unnötigen Tool-Abhängigkeiten.

## Lizenz

MIT © 2026 Michael Gahn DESIGN für Skillcode und Dokumentation. Keine pauschale Lizenz für fremde Schriften, Marken, Referenzen oder zukünftig erzeugte Motive. Unabhängiges Community-Projekt, kein offizieller Spreadshirt-Service.
