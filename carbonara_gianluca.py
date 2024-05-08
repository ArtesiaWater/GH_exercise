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
    'mix spaghetti, yolk and cheese and guanciale',
    'add pasta cooking water to make a creamy sauce',
    'serve immedeately',
]

# # instructions for vegetarians
veg_instr = [
    'slice the squash (the best squash is the "napoletana squash" that you find only in Sicily )',
    'fry the squash in hot olive oil'
    'mix spaghetti, yolk and cheese and fried squash',
]



# Variation: make it vegetarian
ingr_opt = ['300g fried squash']

print('\nINGREDIENTS:')
print(*ingr, sep='\n')

print('\nOPTIONAL INGREDIENTS FOR VEGETARIAN (NO GUANCIALE):')
print(*ingr_opt, sep='\n')

print('\nINSTRUCTIONS FOR PISSING YOUR ITALIAN GUESTS OFF:')
print(*instr, sep='\n')

print('\nINSTRUCTIONS FOR MAKING THE ITALIANS HAPPY:')
print(*instr[0:4], sep='\n')
print('add spagetti to boiling water with salt', sep='\n')
print('cook spaghetti for the time indicated by producer - 2/3 minutes', sep='\n')
print(*instr[6:10], sep='\n')

print('\nINSTRUCTIONS FOR VEGETARIANS (SUBSTITUTE STEPS 1,2 & 8):')
print(*veg_instr, sep='\n')