# Verifying various poker odds for texas holdem via monte carlo.

import random
from collections import Counter
import numpy as np

# Create an unshuffled deck. The deck is a list of tuples where each card is a tuple.
def create_deck():
    ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'J', 'Q', 'K', 'A']
    suits = ['Clubs', 'Spades', 'Hearts', 'Diamonds']
    deck = []
    for rank in ranks:
        for suit in suits:
            deck.append((rank, suit))
    return deck

def shuffle_deck(deck):
    random.shuffle(deck)
    return deck

# Deal N cards from a shuffled deck
def deal_cards(num_cards):
    deck = shuffle_deck(create_deck())
    hand = deck[0:num_cards]
    return hand

def convert_ranks_to_numbers(hand):
    mapping = {'Two':2,
                'Three':3,
                'Four':4,
                'Five':5,
                'Six':6,
                'Seven':7,
                'Eight':8,
                'Nine':9,
                'Ten':10,
                'J':11,
                'Q':12,
                'K':13,
                'A':14}
    new_hand = []
    for card in hand:
        rank = mapping[card[0]]
        suit = card[1]
        new_hand.append((rank, suit))
    return new_hand

# Input two hole cards, output a 5-card hand (post flop)
def make_hand(hole_cards):
    shuffled_deck = shuffle_deck(create_deck())
    for card in hole_cards:
        shuffled_deck.remove(card)
    flop = shuffled_deck[0:3]
    return hole_cards + flop

def has_flush_draw(hand):
    suit_counts = Counter(card[1] for card in hand)
    if max(suit_counts.values()) >= 4:
        return True
    else:
        return False

def has_open_ended_straight_draw(hand):
    hand = convert_ranks_to_numbers(hand)
    ranks_high = sorted([card[0] for card in hand]) # Ace is high by default
    ranks_low = sorted([1 if rank == 14 else rank for rank in ranks_high])
    for ranks in [ranks_high, ranks_low]:
        if ranks[:-1] == list(range(ranks[0], ranks[-1])):
            if 1 not in ranks[:-1] and 14 not in ranks[:-1]: # isn't open ended if it has an Ace
                return True
        elif ranks[1:] == list(range(ranks[1], ranks[-1]+1)):
            if 1 not in ranks[1:] and 14 not in ranks[1:]: # isn't open ended if it has an Ace
                return True
    return False

def has_flush_draw_or_open_ended_straight_draw(hand):
    if has_flush_draw(hand) or has_open_ended_straight_draw(hand):
        return True
    else:
        return False

def monte_carlo(hole_cards, func, trials=10000):
    count = 0
    for trial in range(trials):
        hand = make_hand(hole_cards)
        count += func(hand)
    return count / trials

hole_cards = [('Seven', 'Clubs'), ('Eight', 'Clubs')]
print(monte_carlo(hole_cards, func=has_flush_draw_or_open_ended_straight_draw))