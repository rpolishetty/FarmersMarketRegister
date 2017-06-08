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
    print_items()
    while True:
        print "To checkout the basket enter <c>"
        item = raw_input('Enter product code to add into the basket: ')
        item = item.strip()
        
        # Calculates basket and applies specials
        if item == "c":
            apply_specials (user_basket)
            break;
        
        # Handeling the new item case, checking if item is valid
        if item in items:
            user_basket.append (item)
            print ("Item " + item + " Added to the Basket!")
            apply_specials (user_basket)
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