#!/usr/bin/env python3
"""Demonstrates input in a while loop."""
     
while True: # True/False are Python's boolians.   
    answer = input("What is your favorite number? ")
    try:  
        number = int(answer)
    except ValueError:
        print(answer, "is not a number! Please try again.")
    else:
        break
print("I got your %s!" % (number))     # % replacement
print("I got your {}!".format(number)) # str.format method
print(f"I got your {number}!")         # f-string
