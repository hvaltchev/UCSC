#!/usr/bin/env python3
"""
Defines MixColors() which takes in any number of colors and mixes
together the first two primary colors.
"""
import random

def MixColors(*colors):
    """Find the first two primary colors given and mixes them.
    Any problem, "grey" is returned.
    """
    PRIMARY_COLORS = "red", "yellow", "blue"
    both_colors = []
    number_colors = 0
    for color in colors:
        if color in PRIMARY_COLORS:
            both_colors.append(color)
            number_colors += 1
            if number_colors == 2:
                break
    else:
        return "grey"
    
    if both_colors[0] == both_colors[1]:
        return both_colors[0]
    
    if "red" in both_colors:
        if "yellow" in both_colors:
            return "orange"
        if "blue" in both_colors:
            return "purple"

    return "green"

def TestMixColors():
    """Tests MixColors with all possible combiniations of colors.
    """
    colors = ["red", "yellow", "blue", "aqua"]
    for one in colors:
        for other in colors:
            now = one, other   
            print(f"{now[0]} + {now[1]} = {MixColors(*now)}.")

    print("Randoms:")
    colors += "green", "gold"

    for trial in range(3):
        random.shuffle(colors)
        print(f"MixColors({colors}) = {MixColors(*colors)}")
            
def main():
    TestMixColors()
    
main()
