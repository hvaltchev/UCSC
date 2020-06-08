#!/usr/bin/env python3
"""
Deals a poker hand.
Demonstrates an import from within a package.
"""
import sys, os, random
sys.path.insert(0, os.path.join(os.path.split(__file__)[0], '..'))
print(f"Inserted into sys.path is: {os.path.abspath(sys.path[0])}")
import Lab09_Functional_Programming.lab09_5 as cards

def DealPokerHand(shuffled_deck, number_of_cards=5):
    hand = [shuffled_deck.pop() for card in range(number_of_cards)]
    return hand

def main():
    the_deck = cards.GetCards()
    random.shuffle(the_deck)
    ordinals = "First", "Second", "Third", "Fourth"
    for player in range(4):
        print(f"{ordinals[player]} player: {', '.join(DealPokerHand(the_deck))}")

if __name__ == "__main__":
    main()
