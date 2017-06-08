'''
This Module is responsible for applying specials

Written by Rohith K Polishetty

Multiple Offers/Specials can be combined by assigning "flag = 1" in "flag.json" file inside "data" folder
consider "flag = 0" for not combining the multiple specials and Hence the later offer is only applied
'''

from dataload.load_data import *
from printing.print_register import *


# This Module does the most of the work of applying discounts
def apply_specials(basket):
    specials = []
    new_basket = basket
    items = load_items()
    flags = load_flags()

    # Handelling the BOGO discount
    if "CF1" in basket:
        coffee_count = basket.count("CF1")
        # checking if the items are in accordance with discount condtion
        if coffee_count % 2 == 0:
            specials_count = coffee_count / 2
            # applting specials based on the number of items.
            for i in range(0, specials_count):
                specials.append(("BOGO", -items['CF1'][1]))
        else:
            new_basket.append("CF1")
            specials_count = (coffee_count + 1) / 2
            for i in range(0, specials_count):
                specials.append(("BOGO", -items['CF1'][1]))

    # For CHMK DISCOUNT
    if "CH1" in basket and "MK1" in basket:
        specials.append(("CHMK", -items['MK1'][1]))
    elif "CH1" in basket and "MK1" not in basket :
        new_basket.append("MK1")
        specials.append(("CHMK", -items['MK1'][1]))
    flag = True
    if flags['combine_specials'] == 0:
        flag = False
    apom_flag = False
    app_flag = False
    if "OM1" in basket and "AP1" in basket:
        specials.append(("APOM", -(items["AP1"][1]) / 2))
        apom_flag = True
    # Applying APPL discount
    if basket.count("AP1") >= 3:
        if not flag and apom_flag:
            return print_register(new_basket, specials)
        app_flag = True
        # applying discount on all apple items
        for i in range(0, basket.count("AP1")):
            specials.append(("APPL", -(items["AP1"][1] - 4.50)))
    # calling print function based on calculated discounts
    return print_register(new_basket, specials)


# Just for testing
def apply_specials_test(basket):
    specials = []
    new_basket = basket
    items = load_items()
    # Handelling the BOGO discount
    if "CF1" in basket:
        coffee_count = basket.count("CF1")
        # checking if the items are in accordance with discount condtion
        if coffee_count % 2 == 0:
            specials_count = coffee_count / 2
            # applting specials based on the number of items.
            for i in range(0, specials_count):
                specials.append(("BOGO", -items['CF1'][1]))
        else:
            new_basket.append("CF1")
            specials_count = (coffee_count + 1) / 2
            for i in range(0, specials_count):
                specials.append(("BOGO", -items['CF1'][1]))
    # For CHMK DISCOUNT
    if "CH1" in basket and "MK1" in basket:
        specials.append(("CHMK", -items['MK1'][1]))

    if "OM1" in basket and "AP1" in basket:
        specials.append(("APOM", -(items["AP1"][1]) / 2))
    # Applying APPL discount
    if basket.count("AP1") >= 3:
        # applying discount on all apple items
        for i in range(0, basket.count("AP1")):
            specials.append(("APPL", -(items["AP1"][1] - 4.50)))
    # calling print function based on calculated discounts
    return specials