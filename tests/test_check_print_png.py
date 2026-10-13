"""Prüft reale Bildinvarianten mit temporären, selbst erstellten Dateien."""
import importlib.util
import tempfile
import unittest
from pathlib import Path

from PIL import Image

SCRIPT = Path(__file__).resolve().parents[1] / 'skills/spreadshirt-product-design/scripts/check_print_png.py'
spec = importlib.util.spec_from_file_location('check_print_png', SCRIPT)
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


class PrintChecks(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.path = Path(self.temp.name) / 'test.png'

    def tearDown(self):
        self.temp.cleanup()

    def motif(self, dpi=None):
        im = Image.new('RGBA', (1000, 1000), (0, 0, 0, 0))
        im.paste((240, 220, 190, 255), (100, 200, 900, 800))
        im.save(self.path, **({'dpi': dpi} if dpi else {}))

    def test_actual_motif_not_empty_padding(self):
        self.motif()
        report = checker.inspect_png(self.path, width_cm=10.16)
        self.assertEqual(report['motif_pixels'], {'width': 800, 'height': 600})
        self.assertEqual(report['effective_motif_dpi'], {'width': 200.0, 'height': 200.0})
        self.assertFalse(report['errors'])

    def test_dpi_metadata_does_not_create_resolution(self):
        self.motif((1200, 1200))
        report = checker.inspect_png(self.path, width_cm=28)
        self.assertTrue(report['errors'])
        self.assertLess(report['effective_motif_dpi']['width'], 100)

    def test_opaque_image_fails_transparency(self):
        Image.new('RGB', (400, 400), 'white').save(self.path)
        self.assertTrue(checker.inspect_png(self.path)['errors'])

    def test_empty_image_is_not_printable(self):
        Image.new('RGBA', (200, 200), (0, 0, 0, 0)).save(self.path)
        self.assertTrue(checker.inspect_png(self.path)['errors'])

    def test_palette_transparency_is_detected(self):
        im = Image.new('P', (100, 100), 0)
        im.putpalette([0, 0, 0, 255, 255, 255] + [0] * 762)
        im.paste(1, (10, 10, 90, 90))
        im.save(self.path, transparency=0)
        self.assertFalse(checker.inspect_png(self.path)['errors'])

    def test_aspect_distortion_fails(self):
        self.motif()
        self.assertTrue(checker.inspect_png(self.path, 10, 10)['errors'])

    def test_partial_opacity_and_required_pixels(self):
        im = Image.new('RGBA', (100, 100), (0, 0, 0, 0))
        im.paste((255, 255, 255, 128), (10, 10, 90, 90))
        im.save(self.path)
        report = checker.inspect_png(self.path, width_cm=28)
        self.assertEqual(report['alpha']['partial_share_of_visible_pixels'], 1.0)
        self.assertEqual(report['required_motif_pixels_at_min_dpi']['width'], 2205)

    def test_limits_and_read_only(self):
        self.motif()
        original = self.path.read_bytes()
        self.assertTrue(checker.inspect_png(self.path, max_pixels=500)['errors'])
        self.assertTrue(checker.inspect_png(self.path, max_bytes=1)['errors'])
        self.assertEqual(original, self.path.read_bytes())


if __name__ == '__main__':
    unittest.main()
