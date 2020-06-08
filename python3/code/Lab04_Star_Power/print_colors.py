#!/usr/bin/env python3
"""Demonstrates using * unwrap a sequence into a call.
"""
def PrintColors(one_color, two_color, three_color):
    print(f"{one_color}, {two_color}, {three_color}.")

def main():
    """All sequences are good for unwrapping into a function call.
    """
    colors_plain = "red", "orange", "yellow"
    PrintColors(*colors_plain)
    colors_parens = ("red", "orange", "yellow")
    PrintColors(*colors_parens)
    colors_squares = ["red", "orange", "yellow"]
    PrintColors(*colors_squares)
    a_str = "hey"
    PrintColors(*a_str)

main()
