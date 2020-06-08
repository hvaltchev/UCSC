#!/usr/bin/env python3
""" Studying range.
"""
MAX = 10
print('range is used with a "for/in" combination:')
for number in range(3, MAX, 2):
    print(number, end=' ')
print()
print('range outside a "for/in" loop gives:', range(3, MAX, 2))
