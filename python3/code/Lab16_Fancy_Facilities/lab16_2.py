#!/usr/bin/env python3
"""
A generator-based function to deal cards.
"""
import os, random, sys
sys.path.insert(0, os.path.join(os.path.split(__file__)[0], ".."))
import Lab09_Functional_Programming.lab09_5 as cards

def DealCard():
    """Generator to yield one card at a time from a deck."""
    deck = cards.GetCards()
    random.shuffle(deck)
    for card in deck:
        yield card

def main():
    for i, card in enumerate(DealCard()):
        print(card, end=' ')
        if i % 5 == 4:
            print()

if __name__ == "__main__":
    main()
