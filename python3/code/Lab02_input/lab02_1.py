#!/usr/bin/env python3
"""
Asks the user for her name, then asks for the amount of
money she has. It then asks for half the money.
"""
name = input("Name please: ")
while True:  
    try:  
        money = float(input("How much money do you have? "))
        break
    except ValueError:
        print("Please try again.")

print(f"{name}, give me ${money/2:.2f}.")
