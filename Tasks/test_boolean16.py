import unittest
from boolean16 import check_twosimple

class TestSimpleInt(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(check_twosimple(0), false)
        self.assertEqual(check_twosimple(5), false)
        self.assertEqual(check_twosimple(10), true)
        self.assertEqual(check_twosimple(86), true)
        self.assertEqual(check_twosimple(952), false)

    def test_types(self):
        self.assertRaises(TypeError, check_twosimple, 10.32)
        self.assertRaises(TypeError, check_twosimple, "two")
