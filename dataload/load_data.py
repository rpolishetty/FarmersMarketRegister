'''
This Module loads the items to dictionary
It creates a dictionary items_list, reads the items/products from JSON file and load into dictionary

Written by Rohith K Polishetty 

'''

import json

def load_items ():
    try:
        with open("./data/item.json", 'rb') as inputFile:
            items_list = json.loads (inputFile.read())
            return items_list
    except (IOError):
        print ("Data File Not Found")
def load_flags ():
    try:
        with open("./data/flags.json", 'rb') as inputFile:
            flags = json.loads (inputFile.read())
            return flags
    except (IOError):
        print ("Data File Not Found")