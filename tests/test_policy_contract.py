"""Validate the proposal's current policy without third-party dependencies."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class PolicyContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.policy = json.loads((ROOT / "policy.json").read_text(encoding="utf-8"))

    def test_marker_identity(self):
        self.assertEqual(self.policy["standard"], "AR-Spatial-Privacy-Marker")
        self.assertEqual(self.policy["marker_id"], "ASPM-V1-OPT-OUT")
        self.assertEqual(self.policy["version"], "1.0.0")

    def test_physical_width_positive(self):
        width = self.policy["physical_width_meters"]
        self.assertIsInstance(width, (int, float))
        self.assertNotIsInstance(width, bool)
        self.assertGreater(width, 0)

    def test_restrictions_boolean(self):
        required = (
            "block_plane_detection", "block_3d_meshing",
            "block_persistent_anchors", "detach_existing_anchors",
            "block_vps_upload",
        )
        for key in required:
            with self.subTest(key=key):
                self.assertIs(type(self.policy["restrictions"][key]), bool)

    def test_printable_marker_exists(self):
        self.assertTrue((ROOT / "assets/ar-privacy-marker-v1.svg").is_file())


if __name__ == "__main__":
    unittest.main()
