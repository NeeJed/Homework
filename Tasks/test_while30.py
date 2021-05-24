import unittest
from while30 import numberOfSquares

class TestSquares(unittest.TestCase):
    def test_numbers(self):
        self.assertEqual(numberOfSquares(22,17,2), 88)
        self.assertEqual(numberOfSquares(4,4,4), 1)
        self.assertEqual(numberOfSquares(0,3,5), 0)
        self.assertEqual(numberOfSquares(10,6,8), 0)
        self.assertEqual(numberOfSquares(10,10,1), 100)
        
    def test_types(self):
        self.assertRaises(TypeError, numberOfSquares, "раз")
        self.assertRaises(TypeError, numberOfSquares, false)

    def test_values(self):
        self.assertRaises(ValueError, numberOfSquares, -1)
        self.assertRaises(ValueError, numberOfSquares, -137)
