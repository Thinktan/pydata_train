import pandas as pd
import numpy as np

# 随机采样和排列

suits = ['H', 'S', 'C', 'D']
card_val = (list(range(1, 11)) + [10]*3) * 4
print(card_val)

base_names = ['A'] + list(range(2, 11)) + ['J', 'K', 'Q']
print(base_names, '\n')

cards = []
for suit in suits:
    cards.extend(str(num) + suit for num in base_names)
print(cards)
print(len(cards), '\n')

deck = pd.Series(card_val, index=cards)
print(deck, '\n')

def draw(deck, n=5):
    return deck.sample(n)

get_suit = lambda card: card[-1]
print(deck.groupby(get_suit).apply(draw, n=2), '\n')