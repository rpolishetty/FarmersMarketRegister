### Farmers Market Register
'''
Author Rohith Polishetty
'''
from discounts.apply_specials import *
import os


items = load_items()
#loop for multiple baskets
while True:
    user_basket = []
    #input items loop
    print_items()
    while True:
        print "To checkout the basket enter <checkout>, To view basket enter <basket>"
        item = raw_input('Enter Product code to add an Item to the basket: ')
        item = item.strip()
        # Calculates basket and applies specials
        if item == "checkout":
            apply_specials (user_basket)
            break;
        # For reviewing the basket during the purchase
        if item == "basket":
            apply_specials (user_basket)
            continue
        # Handeling the new item case, checking if item is valid
        if item in items:
            user_basket.append (item)
            print ("Item " + item + " Added to the Basket!")
        else:
            print ("Item does not exist!")
    # If user wants to make a new purchase
    new_basket = raw_input('Would you like to input a new basket? (y/n) ')
    if new_basket == "y":
        os.system('clear')
        continue
    elif new_basket == "n":
        print ("Thank You!!")
        break