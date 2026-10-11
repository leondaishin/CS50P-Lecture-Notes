# Library
# Importing the random Library
# Random = from all of the python functions 
import random

# From a specific place ("from") than saying random.
# importing choice makes the random.choice to just choice()
# from random import choice

# Takes a sequence/list (remember list from the previous weeks)
# "" to de]cribe strings, [] for defining the list, () for the choice function
# Takes the list and picks random element from the list with the ame probability
# coin = random.choice(["heads", "tails"])

# if u have from random import choice 
coin = random.choice(["heads", "tales"])
print(coin)

# for making the random away u can do from random import randint
# if u want to output a RANDOM number from a to b
number = random.randint(1, 10)
print(number)

# shuffle a deck of cards 
# this is the list of cards 
cards = ["jack", "queen", "king", "ace"]
#shuffling the cards
random.shuffle(cards)
#for each of the card in cards, print card
for card in cards: 
    print(card)

