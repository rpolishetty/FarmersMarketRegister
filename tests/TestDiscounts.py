import unittest
from decimal import Decimal
from discounts.apply_specials import *

class TestTotal(unittest.TestCase):
    def setUp(self):
        pass

    # Test for list creation on all products
    def test_total1(self):
        basket = ["AP1", "AP1", "AP1"]
        total = apply_specials (basket)
        original_total = "13.50"
        self.assertEqual(original_total, total)
    def test_total2(self):
        basket = ["CH1", "AP1", "CF1", "MK1"]
        total = apply_specials (basket)
        original_total = "20.34"
        self.assertEqual(original_total, total)
    def test_total3(self):
        basket = ["CF1", "CF1"]
        total = apply_specials (basket)
        original_total = "11.23"
        self.assertEqual(original_total, total)
    def test_total4(self):
        basket = ["AP1", "AP1", "CH1", "AP1"]
        total = apply_specials (basket)
        original_total = "16.61"
        self.assertEqual(original_total, total)

if __name__ == '__main__':
    unittest.main()