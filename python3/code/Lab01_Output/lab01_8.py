#!/usr/bin/env python3
"""Produces a christmas tree pattern of stars."""

blanks = 18
stars = 1
for line in range(10):
    print(blanks * ' ', stars * '* ')
    blanks -= 2
    stars += 2

