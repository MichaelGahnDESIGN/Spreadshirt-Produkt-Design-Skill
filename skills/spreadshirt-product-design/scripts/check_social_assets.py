#!/usr/bin/env python3
"""Werbebilder rein lesend gegen Produktionspresets prüfen."""
import argparse
import json
import sys
from pathlib import Path

from PIL import Image

DEFAULT_PRESETS = Path(__file__).resolve().parents[1] / 'references/social-presets.json'


def inspect_assets(directory, presets):
    """Vollständigkeit und echte Exportmaße prüfen, keine Inhaltsfreigabe."""
    reports = []
    for asset in presets['assets']:
        filename = asset['filename']
        # Projektpresets dürfen nicht außerhalb des Werbeordners lesen.
        if Path(filename).name != filename or filename in ('.', '..'):
            raise ValueError('Preset-Dateiname muss ein einfacher Dateiname sein.')
        width, height = asset['width'], asset['height']
        if type(width) is not int or type(height) is not int or min(width, height) <= 0:
            raise ValueError('Preset-Maße müssen positive ganze Zahlen sein.')
        path = directory / filename
        report = {'filename': filename, 'expected_pixels': [width, height], 'errors': []}
        try:
            with Image.open(path) as im:
                im.load()
                report.update(actual_pixels=list(im.size), mode=im.mode, format=im.format)
                if im.size != (width, height):
                    report['errors'].append('Exportmaße stimmen nicht mit dem Produktionspreset überein.')
                if im.format != 'PNG':
                    report['errors'].append('Keine PNG-Datei.')
                if im.mode not in ('RGB', 'RGBA'):
                    report['errors'].append('Werbeexport muss RGB oder RGBA sein.')
                if im.mode == 'RGBA' and im.getchannel('A').getextrema()[0] < 255:
                    report['errors'].append('Werbekomposition hat transparente Bereiche; auf vollständigen Hintergrund exportieren.')
        except (OSError, ValueError, Image.DecompressionBombError) as exc:
            report['errors'].append(str(exc))
        reports.append(report)
    if not reports:
        raise ValueError('Presets enthalten keine Werbegrafiken.')
    return {'status': 'failed' if any(r['errors'] for r in reports) else 'passed_automated_checks_only',
            'assets': reports,
            'not_checked': ['Texte und Alttexte', 'Motivtreue', 'Lesbarkeit und UI-Ränder',
                            'Produktdaten und Rechte', 'aktuelle Plattformannahme']}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('directory', type=Path)
    parser.add_argument('--presets', type=Path, default=DEFAULT_PRESETS)
    args = parser.parse_args()
    try:
        report = inspect_assets(args.directory, json.loads(args.presets.read_text(encoding='utf-8')))
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(json.dumps({'status': 'error', 'error': str(exc)}, ensure_ascii=False))
        return 2
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 1 if report['status'] == 'failed' else 0


if __name__ == '__main__':
    sys.exit(main())
