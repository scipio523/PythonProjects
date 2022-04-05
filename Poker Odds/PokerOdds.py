# Verifying various poker odds for texas holdem via monte carlo.

import random

# Create an unshuffled deck. The deck is a list of tuples where each card is a tuple.
def create_deck():
    ranks = ['A', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'J', 'Q', 'K']
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


# Odds of flopping a flush draw, or flush, assuming your hole cards are suited
def flush_draw_two_suited_hole_cards(trials=10000):
    num_flush_draws = 0
    for trial in range(trials):

        # Assume our two hole cards are always Ace of clubs and King of clubs. Calc the probability that we hit two more clubs on the flop.
        shuffled_deck = shuffle_deck(create_deck())
        shuffled_deck.remove(('A', 'Clubs'))
        shuffled_deck.remove(('K', 'Clubs'))

        flop = shuffled_deck[0:3]

        club_count = 0
        for card in flop:
            if card[1] == 'Clubs':
                club_count += 1
        
        if club_count >= 2:
            num_flush_draws += 1

    return num_flush_draws / trials
    

# Odds of flopping an open ended straight draw, or straight, assuming your hole cards are connected
def straight_draw_two_connected_hole_cards(trials=10000):
    num_straight_draws = 0
    for trial in range(trials):

        # Assume our two hole cards are always Seven of clubs and Eight of clubs. Calc the probability that we hit two more clubs on the flop.
        shuffled_deck = shuffle_deck(create_deck())
        shuffled_deck.remove(('Seven', 'Clubs'))
        shuffled_deck.remove(('Eight', 'Clubs'))

        flop = shuffled_deck[0:3]
        ranks = [card[0] for card in flop]

        # We need one of these card combinations on the flop in order to make a straight draw
        if ('Five' in ranks and 'Six' in ranks) or ('Six' in ranks and 'Nine' in ranks) or ('Nine' in ranks and 'Ten' in ranks):
            num_straight_draws += 1

    return num_straight_draws / trials



print( flush_draw_two_suited_hole_cards() )
print( straight_draw_two_connected_hole_cards() )