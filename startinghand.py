"""
Definitions:
- hand: set of hidden cards a player has on his boards
- group: same number, different colors
- sequence: same color, range of numbers
- matching set: group or sequence

There are 2 Questions to answer:
1. What is the probability for a number of cards to have a starting set?
2. How many cards do you need to draw to start?

I calculate 1. here. 2. seems much harder, but may be the same on the average case as 1.
"""

import itertools
import random


COLORS = 'RGBY'
VALUES = list(range(1, 14))
DECK = list(itertools.product(COLORS, VALUES))
DECK = DECK + DECK


def best_hand_value(hand, colors, values):
    """
    Count how many points the best hand has.
    """
    return max(
        (sum_cards(matching_set) for matching_set in generate_sets(hand, colors, values)),
        default=0
    )


def sum_cards(cards):
    return sum(v for c, v in cards)


def generate_sets(hand, colors, values):
    valgroups = {v: set() for v in values}
    colgroups = {c: set() for c in colors}
    for c, v in hand:
        valgroups[v].add((c, v))
        colgroups[c].add((c, v))

    # groups
    for g in valgroups.values():
        if len(g) >= 3:
            yield g
    
    # sequences
    for g in map(sorted, colgroups.values()):
        if len(g) < 3:
            continue

        _, first = g[0]
        _, last = g[0]

        for c, v in g[1:]:
            next_expected = last + 1
            if v == next_expected:
                last = v
            else: # v != next_expected:
                num_elems = last - first + 1
                if num_elems >= 3:
                    yield {(c, v) for v in range(first, last+1)}
                first = v
                last = v

        num_elems = last - first + 1
        if num_elems >= 3:
            yield {(c, v) for v in range(first, last+1)}


def has_starting_set(cards, colors, values):
    return best_hand_value(cards, colors, values) >= 30


def random_hand(num_cards, deck):
    return random.sample(deck, num_cards)


def sample_probability(num_cards, deck, colors, values, num_samples=100000):
    num_starting_hands = 0

    for i in range(num_samples):
        hand = random_hand(num_cards, deck)
        
        if has_starting_set(hand, colors, values):
            num_starting_hands += 1

    return num_starting_hands/num_samples


def calculate_probability(num_cards, deck, colors, values):
    num_hands = 0
    num_starting_hands = 0

    try:
        while True:
            hand = random_hand(num_cards, deck)
            
            num_hands += 1
            if has_starting_set(hand, colors, values):
                num_starting_hands += 1
            
            if num_hands % 10000 == 0:
                print(f"{num_starting_hands/num_hands}")
    except KeyboardInterrupt as e:
        return


def format_cards(cards):
    return " ".join(f"{c}{v}" for c, v in sorted(cards))


def print_cards(cards):
    print(format_cards(cards))


if __name__ == "__main__":
    calculate_probability(14, deck=DECK, colors=COLORS, values=VALUES)
