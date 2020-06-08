#!/usr/bin/env python3
"""Interactive vowel counter."""

import lab08_1

def main():
    while True:
        count_this = input("Phrase: ")
        if not count_this:
            break
        print(f"... has {lab08_1.CountVowels(count_this)} vowels.")

if __name__ == "__main__":
    main()

