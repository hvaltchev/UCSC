#!/usr/bin/env python3
"""Demonstrates if/elif/else and while/else."""

number = 25

print(number, "is", end=' ')
if number < 10:
    print("small")
elif number < 1000:
    print("medium")
else:
    print("large")

if 10 < number < 50:   # "and" is assumed
    print("number is in")
# Alternate syntax since 2.5 -- all one line but less readable.
print(number, "is", end=' ')
print("small" if number < 10 \
              else "medium" if number < 1000 \
              else "large")  
# else can also occur in a loop
div = 2 
while div * div <= number:   
    if number % div == 0:
        print(number, "is divisible by", div)
        break   
    div += 1
else:  
    print(number, "is prime")
