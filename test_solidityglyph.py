# test_solidityglyph.py
"""
Tests for SolidityGlyph module.
"""

import unittest
from solidityglyph import SolidityGlyph

class TestSolidityGlyph(unittest.TestCase):
    """Test cases for SolidityGlyph class."""

    def test_initialization(self):
        """Test class initialization."""
        instance = SolidityGlyph()
        self.assertIsInstance(instance, SolidityGlyph)

    def test_run_method(self):
        """Test the run method."""
        instance = SolidityGlyph()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
