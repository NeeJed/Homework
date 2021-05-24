import unittest
from integer22 import minutes

class TestMinutes(unittest.TestCase):
    def test_minutes(self):
        self.assertEqual(minutes(7), 7)
        self.assertEqual(minutes(1000), 1000)
        self.assertEqual(minutes(3605), 5)
        self.assertEqual(minutes(17321), 2921)
        self.assertEqual(minutes(0), 0)

    def test_types(self):
        self.assertRaises(TypeError, minutes, true)
        self.assertRaises(TypeError, minutes, "eleven")
        self.assertRaises(TypeError, minutes, 13.7)

    def test_values(self):
        self.assertRaises(ValueError, minutes, -10)
