"""Prüft Werbeexports, keine generierten Produktbilder erforderlich."""
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'skills/spreadshirt-product-design/scripts/check_social_assets.py'
spec = importlib.util.spec_from_file_location('check_social_assets', SCRIPT)
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


class SocialChecks(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.directory = Path(self.temp.name)
        self.presets = json.loads(checker.DEFAULT_PRESETS.read_text())

    def tearDown(self):
        self.temp.cleanup()

    def create_set(self):
        for asset in self.presets['assets']:
            Image.new('RGB', (asset['width'], asset['height']), 'black').save(self.directory / asset['filename'])

    def test_complete_set_and_read_only(self):
        self.create_set()
        before = {p.name: p.read_bytes() for p in self.directory.iterdir()}
        report = checker.inspect_assets(self.directory, self.presets)
        self.assertEqual(report['status'], 'passed_automated_checks_only')
        self.assertEqual(len(report['assets']), 5)
        self.assertEqual(before, {p.name: p.read_bytes() for p in self.directory.iterdir()})

    def test_missing_platform_file(self):
        self.create_set()
        (self.directory / 'pinterest-pin.png').unlink()
        self.assertEqual(checker.inspect_assets(self.directory, self.presets)['status'], 'failed')

    def test_wrong_export_size(self):
        self.create_set()
        Image.new('RGB', (800, 600)).save(self.directory / 'instagram-story.png')
        self.assertEqual(checker.inspect_assets(self.directory, self.presets)['status'], 'failed')

    def test_transparent_ad_fails(self):
        self.create_set()
        Image.new('RGBA', (1080, 1080), (0, 0, 0, 0)).save(self.directory / 'facebook-feed.png')
        self.assertEqual(checker.inspect_assets(self.directory, self.presets)['status'], 'failed')

    def test_path_escape_rejected(self):
        with self.assertRaises(ValueError):
            checker.inspect_assets(self.directory, {'assets': [{'filename': '../outside.png', 'width': 100, 'height': 100}]})

    def test_empty_manifest_rejected(self):
        with self.assertRaises(ValueError):
            checker.inspect_assets(self.directory, {'assets': []})


if __name__ == '__main__':
    unittest.main()
