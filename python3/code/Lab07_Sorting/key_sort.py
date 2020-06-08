#!/usr/bin/env python3
"""Demonstrates the key keyword for list.sort.
"""

def MagicNumber(string):
    """Returns the sum of the mapping of each
    character into its place in the alphabet.
    """
    ALPHABET = "abcdefghijklmnopqrstuvwxyz"
    total = 0
    for char in string.lower():
        total += ALPHABET.index(char)
    return total

def ReportInternalSortKey(names):
    """Reports the tuple that the sort will use when this
    function is named as the 'key'.
    """
    sort_keys = []
    for name in names:
        sort_keys += [(MagicNumber(name), name)]
    print(f"MagicNumber keys: {sort_keys}")
        
def main():
    names = ["June", "Alejandro", "Ann", "I", "Izzy"]

    print(f"            Names list: {names}")
    print(f"          Default sort: {sorted(names)}")
    print(f"      Sorted by length: {sorted(names, key=len)}")
    ReportInternalSortKey(names)
    names.sort(key=MagicNumber)
    print(f"Sorted by magic number: {names}")

main()
