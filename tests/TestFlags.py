import unittest
from decimal import Decimal
from discounts.apply_specials import *

class TestSpecials(unittest.TestCase):
    def setUp(self):
        pass
    # Test for list creation on all products
    def test_special1(self):
        flags = load_flags()
        original_flags = {"combine_specials": 1}      
        self.assertDictEqual(flags, original_flags)

if __name__ == '__main__':
    unittest.main()