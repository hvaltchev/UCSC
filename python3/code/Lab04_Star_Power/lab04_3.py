#!/usr/bin/env python3
"""
lab04_3.py - a a MakePizza() function.  It takes in any number of
arguments. The first two are the main ingredients and are required.
"""
def MakePizza(first, second, *rest):
    print(f"Here's your {first} and {second} pizza, with", end='')
    for ingredient in rest:
        print(f" {ingredient}", end='')
    print("\nEnjoy!")
    
def main():
    ingredients = "anchovies", "garlic", "oregano", "tomato", "peppers"
    MakePizza(*ingredients)
    MakePizza("cheese", *ingredients)

main()
