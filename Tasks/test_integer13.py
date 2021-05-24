import unittest
from integer13 import replace

class TestReplace(unittest.TestCase):
    def test_replace(self):
        self.assertEqual(replace(0), false)
        self.assertEqual(replace(13), false)
        self.assertEqual(replace(135), true)
        self.assertEqual(replace(952), true)
        self.assertEqual(replace(-3), false)

    def test_types(self):
        self.assertRaises(TypeError, replace, false)
        self.assertRaises(TypeError, replace, "seven")

    def test_values(self):
        self.assertRaises(ValueError, replace, 10)
        self.assertRaises(ValueError, replace, -3)

