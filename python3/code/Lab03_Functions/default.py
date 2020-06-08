#!/usr/bin/env python3
"""Demonstrates defaulted arguments."""

def GoToThePark(name, best_friend="Jose'"): 
    print(f"""{name} and {best_friend}
go to the park
play hide-and-seek
till long after dark
""")

GoToThePark("Charlie", "Josephine")
GoToThePark("Judi")
