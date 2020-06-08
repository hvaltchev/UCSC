#!/usr/bin/env python3
"""Demonstrates catching an exception on error."""

answer = input("What is your favorite number? ")
print("You like", answer, '?')
print("You really like " + answer + '?')
print(answer, "is", end=' ')
try:               
    number = int(answer)
except ValueError:
    print("not a number!")
else:
    if number < 10:
        print("small.")
    elif number < 1000:
        print("medium.")
    else:
        print("large.")

    print("But you like " + str(number) + '!')
