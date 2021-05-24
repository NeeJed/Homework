import unittest
from boolean31 import triangle_true

class TestTriangle(unittest.TestCase):
    def test_triangle(self):
        self.assertEqual(triangle_true(0,1,2), false)
        self.assertEqual(triangle_true(1,2,3), false)
        self.assertEqual(triangle_true(3,4,3), true)
        self.assertEqual(triangle_true(10,10,8), true)
        self.assertEqual(triangle_true(3,4,5), false)

    def test_types(self):
        self.assertRaises(TypeError, triangle_true, 10.32)
        self.assertRaises(TypeError, triangle_true, "two")
