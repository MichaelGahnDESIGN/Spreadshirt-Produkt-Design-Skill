#!/usr/bin/env python3
"""PNG rein lesend prüfen; keine Druckabnahme oder Bildbearbeitung."""
import argparse
import json
import math
import sys
from pathlib import Path

from PIL import Image, UnidentifiedImageError


def positive_number(value):
    """Ungültige Maße verhindern sinnlose Auflösungs- und Größenberichte."""
    result = float(value)
    if not math.isfinite(result) or result <= 0:
        raise argparse.ArgumentTypeError('Wert muss endlich und größer als null sein.')
    return result


def inspect_png(path, width_cm=None, height_cm=None, min_dpi=200,
                max_pixels=4000, max_bytes=10_000_000):
    """Prüft Dateigrenzen und Alpha; Motivpixel zählen ohne leeren Außenrand.

    Ein bestandenes Ergebnis belegt ausschließlich die automatischen Checks.
    Freistellung, Detailqualität und Druckannahme benötigen weitere Prüfung.
    """
    errors, warnings = [], []
    size = path.stat().st_size
    with Image.open(path) as source:
        source.load()
        width, height = source.size
        mode, file_format = source.mode, source.format
        alpha_present = 'A' in source.getbands() or 'transparency' in source.info
        # Die Konvertierung passiert nur im Speicher zum Lesen des Alpha-Kanals.
        alpha = source.convert('RGBA').getchannel('A')
        histogram = alpha.histogram()
        bbox = alpha.getbbox()
        transparent = histogram[0]
        partial = sum(histogram[1:255])
        metadata_dpi = source.info.get('dpi')

    if file_format != 'PNG':
        errors.append('Keine PNG-Datei. Dieser Prüfer bewertet nur PNG-Druckdateien.')
    if mode not in ('RGB', 'RGBA', 'P'):
        errors.append('Kein RGB-/RGBA- oder RGB-Palettenmodus; RGB-Export prüfen.')
    if size > max_bytes:
        errors.append('Dateigröße überschreitet das konfigurierte Limit.')
    if width > max_pixels or height > max_pixels:
        errors.append('Mindestens eine Bildachse überschreitet das konfigurierte Pixel-Limit.')
    if not alpha_present or transparent == 0:
        errors.append('Kein vollständig transparenter Bereich gefunden; Freistellung prüfen.')
    if bbox is None:
        errors.append('Bild ist vollständig transparent und enthält kein druckbares Motiv.')
    if partial:
        warnings.append('Teiltransparente Pixel vorhanden: Kanten und flächige Verläufe visuell unterscheiden.')
    visible = width * height - transparent
    partial_share = partial / visible if visible else 0
    if partial_share > 0.5:
        warnings.append('Mehr als die Hälfte der sichtbaren Pixel ist teiltransparent; Deckkraft des gesamten Motivs prüfen.')
    if not width_cm and not height_cm:
        warnings.append('Keine Zielgröße angegeben; effektive Auflösung für geplanten Druck nicht geprüft.')
    warnings.append('Sichtprüfung, Farbprofil, ursprüngliche Detailauflösung und Produkteditor nicht automatisch geprüft.')

    motif_w = bbox[2] - bbox[0] if bbox else 0
    motif_h = bbox[3] - bbox[1] if bbox else 0
    requested = {'width': width_cm, 'height': height_cm}
    effective = None
    if motif_w and motif_h and (width_cm or height_cm):
        # Ein einzelnes Maß legt das andere proportional fest.
        if width_cm is None:
            width_cm = height_cm * motif_w / motif_h
        elif height_cm is None:
            height_cm = width_cm * motif_h / motif_w
        elif not math.isclose(width_cm / height_cm, motif_w / motif_h, rel_tol=0.01):
            errors.append('Zielmaße verändern das Motivseitenverhältnis um mehr als 1 Prozent.')
        dx, dy = motif_w * 2.54 / width_cm, motif_h * 2.54 / height_cm
        effective = {'width': round(dx, 2), 'height': round(dy, 2)}
        if min(dx, dy) + 1e-9 < min_dpi:
            errors.append('Motivauflösung reicht für die angegebene Zielgröße nicht aus.')

    return {
        'file': str(path),
        'status': 'failed' if errors else 'passed_automated_checks_only',
        'format': file_format, 'mode': mode, 'bytes': size,
        'canvas_pixels': {'width': width, 'height': height},
        'motif_bbox': bbox,
        'motif_pixels': {'width': motif_w, 'height': motif_h},
        'alpha': {'present': alpha_present, 'fully_transparent_pixels': transparent,
                  'partially_transparent_pixels': partial,
                  'partial_share_of_visible_pixels': round(partial_share, 4)},
        'dpi_metadata': metadata_dpi,
        'requested_motif_cm': requested,
        'proportional_target_cm': {'width': width_cm, 'height': height_cm},
        'effective_motif_dpi': effective,
        'required_motif_pixels_at_min_dpi': {
            'width': math.ceil(width_cm / 2.54 * min_dpi),
            'height': math.ceil(height_cm / 2.54 * min_dpi),
        } if width_cm and height_cm and bbox else None,
        'max_motif_cm_at_min_dpi': {'width': round(motif_w * 2.54 / min_dpi, 2),
                                   'height': round(motif_h * 2.54 / min_dpi, 2)},
        'limits': {'min_dpi': min_dpi, 'max_pixels_per_axis': max_pixels,
                   'max_bytes': max_bytes},
        'errors': errors, 'warnings': warnings,
        'spreadshirt_approval': 'not_checked',
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('file', type=Path)
    parser.add_argument('--width-cm', type=positive_number)
    parser.add_argument('--height-cm', type=positive_number)
    parser.add_argument('--min-dpi', type=positive_number, default=200)
    parser.add_argument('--max-pixels', type=int, default=4000)
    parser.add_argument('--max-bytes', type=int, default=10_000_000)
    args = parser.parse_args()
    if args.max_pixels <= 0 or args.max_bytes <= 0:
        parser.error('Datei- und Pixel-Limits müssen größer als null sein.')
    try:
        report = inspect_png(args.file, args.width_cm, args.height_cm,
                             args.min_dpi, args.max_pixels, args.max_bytes)
    except (OSError, UnidentifiedImageError, Image.DecompressionBombError, ValueError) as exc:
        print(json.dumps({'status': 'error', 'error': str(exc)}, ensure_ascii=False))
        return 2
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 1 if report['errors'] else 0


if __name__ == '__main__':
    sys.exit(main())
