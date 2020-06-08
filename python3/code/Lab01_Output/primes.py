#!/usr/bin/env python3
"""Produces a list of prime numbers > 2.

Here, we are only checking the "look" of Python code.
"""
MAX = 100                              # '#' starts a comment.   

print("primes less than", MAX, "are:") # A new line is added
                                       # by default.

for number in range(3, MAX, 2):
    div = 2
    while div * div <= number:
        if number % div == 0: 
            break             
        div += 1      
    else:                # Overloaded 'else': control goes
                         # here when the loop finishes and 
                         # doesn't 'break'.
        print(number, end=' ')
        # Use the 'end' keyword argument to control what is
        # printed at the end.
        
print() # This call produces only the new line.
