import unittest
from if30 import rangeNumbers

class TestRangeNumbers(unittest.TestCase):
    def test_types(self):
        self.assertRaises(TypeError, rangeNumbers, false)
        self.assertRaises(TypeError, rangeNumbers, "девять")

    def test_values(self):
        self.assertRaises(ValueError, rangeNumbers, 0)
        self.assertRaises(ValueError, rangeNumbers, -10)
