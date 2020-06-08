#!/usr/bin/env python3
"""A coin flipping emulation. """
import random

def FlipCoin():
    """Simulates the flip of a coin."""

    if random.randrange(0, 2) == 0:
        return "tails"
    return "heads"

def main(num_times):
    """Driver for testing."""
    heads = 0
    for n in range(num_times):
        if FlipCoin() == "heads":
            heads += 1
    print(f'With {num_times} flips, "heads" came up {heads} '
          f"times, or {heads/num_times:.1%} of the flips.")

main(100)
