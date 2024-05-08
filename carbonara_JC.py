# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 11:40:01 2024

@author: fscha
"""

# %%
# ingredients

ingr = (
    "100g guanciale",
    "50g pecorino cheese",
    "50g parmesan",
    "3 large eggs",
    "350g spaghetti",
    "2 plump garlic cloves, peeled and left whole",
    "50g unsalted butter",
    "sea salt and freshly ground black pepper",
)

# # instructions
instr = [
    "chop guanciale",
    "grate pecorino and parmesan",
    "boil water",
    "cook spaghetti",
    "fry pancetta",
    "mix spaghetti with pancetta",
    "mix cheese with eggs",
    "add pasta cooking water",
    "put egg yolk on the pasta",
    "serve immedeately",
]


# Variation: make it vegetarian
ingr[0] = "100g halloumi"

print("\nINGREDIENTS:")
print(*ingr, sep="\n")

print("\nINSTRUCTIONS:")
print(*instr, sep="\n")
