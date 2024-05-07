# -*- coding: utf-8 -*-
'''
Created on Thu Apr 18 11:40:01 2024

@author: fscha
'''
# modified by Gianluca

# %%
# ingredients

ingr = (
    '100g guanciale',
    '50g pecorino cheese',
    '50g parmesan',
    '3 large eggs, only yolk',
    '350g spaghetti',
    'sea salt and freshly ground black pepper',
)

# # instructions
instr = [
    'chop guanciale',
    'fry guanciale and pepper',
    'grate pecorino and parmesan',
    'mix grated cheese and yolk',
    'add spagetti to water & salt and turn heat on',
    'cook spaghetti for the time indicated by producer',
    'drain spaghetti, keeping a bit of cooking pasta',
    'mix spaghetti, yolk and cheese',
    'add pasta cooking water',
    'serve immedeately',
]


# Variation: make it vegetarian
ingr[0] = '100g fried squash'

print('\nINGREDIENTS:')
print(*ingr, sep='\n')

print('\nINSTRUCTIONS:')
print(*instr, sep='\n')
