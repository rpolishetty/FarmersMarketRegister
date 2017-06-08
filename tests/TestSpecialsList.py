import unittest
from decimal import Decimal
from discounts.apply_specials import *

class TestSpecials(unittest.TestCase):
    def setUp(self):
        pass
    # Test for list creation on all products
    def test_special1(self):
        basket = ["AP1", "AP1", "AP1"]
        total = apply_specials_test (basket)
        original_total = [("APPL", -1.50),
         ("APPL", -1.50),
         ("APPL", -1.50)
         ]
        self.assertListEqual(original_total, total)
    def test_special2(self):
        basket = ["CH1", "AP1", "AP1","AP1","MK1"]
        total = apply_specials_test (basket)
        original_total = [("CHMK", -4.75),
         ("APPL", -1.50),
         ("APPL", -1.50),
         ("APPL", -1.50)
         ]        
        self.assertListEqual(original_total, total)
    def test_special3(self):
        basket = ["CF1", "CF1"]
        total = apply_specials_test (basket)
        original_total = [("BOGO", -11.23)]
        self.assertListEqual(original_total, total)

if __name__ == '__main__':
    unittest.main()