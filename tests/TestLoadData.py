import unittest
from decimal import Decimal
from discounts.apply_specials import *

class TestLoadData(unittest.TestCase):
    def setUp(self):
        pass

    # Test for list creation on all products
    def test_Load(self):
        items = load_items ()
        items_test_list = {
        "CH1": ["Chai", 3.11], 
        "OM1": ["Oatmeal", 3.69], 
        "AP1": ["Apples", 6.0], 
        "MK1": ["Milk", 4.75], 
        "CF1": ["Coffee", 11.23]
        }

        self.assertDictEqual(items, items_test_list)

if __name__ == '__main__':
    unittest.main()