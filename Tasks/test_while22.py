import unittest
from while22 import check_true

class Testwhile22(unittest.TestCase):
    def test_while22(self):
        self.assertEqual(check_true(0), false)
        self.assertEqual(check_true(1), true)
        self.assertEqual(check_true(2), false)
        self.assertEqual(check_true(3), true)
        self.assertEqual(check_true(17), true)
        
