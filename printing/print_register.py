'''
This module handles to print the basket on Console

Written by Rohith K Polishetty
'''
from decimal import Decimal
from dataload.load_data import *

def print_register(basket, specials):
    items = load_items ()
    # To set total variable of decimal type with two decimal places
    totalprice = Decimal('0.00')
    # This sets header by printing by creating columns of width 17 characters
    print '{:17s} {:>17s}'.format("Item", "Price")
    print '{:17s} {:>17s}'.format("----", "-----")
    # printing items in the basket
    for item in basket:
        totalprice += Decimal(items[item][1])
        # using string format specifier to convert float to string with two decimal places
        print '{:17s} {:>17s}'.format(item, '%.2f' %(items[item][1]))
    # Print discounts calculated in apply_specials function
    for special in specials:
        totalprice += Decimal(special[1])
        # using string format specifier to convert float to string with two decimal places
        print '{:>17s} {:>17s}'.format(special[0], '%.2f' % special[1])

    #Print footer and total value
    print "-----------------------------------"
    print ('%.2f' % totalprice).rjust(35)
    return ('%.2f' % totalprice)

def print_items():
    items = load_items ()
    items_keys = items.keys()
    items = items.values()
    
    print '{:17s} {:>17s}'.format("Item", "Price")
    print '{:17s} {:>17s}'.format("----", "-----")
    # Print all items in the basket
    i = 0
    for item in items:
        # using string format specifier to convert float to string with two decimal places
        print '{:17s} {:>17s}'.format(items_keys[i],'%.2f' %(item[1]))
        i= i+1
    