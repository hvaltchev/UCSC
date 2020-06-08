#!/usr/bin/env python3
"""Coin flip Experiments, continued. """

import random

def FlipCoin():
    """Simulates the flip of a coin."""

    if random.randrange(0, 2) == 0:
        return "tails"
    return "heads"

def GetHeads(target):
    """Flips coins until it gets target heads in a row."""

    heads = count = 0
    while heads < target:
        count += 1
        if FlipCoin() == "heads":
            heads += 1
        else:          # "tails"
            heads = 0
    return count

def GetAverage(number_of_experiments, target):
    """Calls GetHeads(target) that number_of_experiments
    times and reports the average."""

    total = 0
    for n in range(number_of_experiments):
        total += GetHeads(target)
    print(f"Averaging {number_of_experiments} experiments, it took {total/number_of_experiments:.1f} coin flips to get {target} in a row.")

GetAverage(100, 3)
