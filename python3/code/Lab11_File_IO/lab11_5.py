#!/usr/bin/env python3
"""Interactive vowel counter."""

import lab09_6
import sys

def main():
    while True:
        sys.stdout.write("Phrase: ")
        sys.stdout.flush()
        count_this = sys.stdin.readline()
        if count_this == '\n':
            break
        sys.stdout.write(f"... has {lab09_6.CountVowels(count_this)} vowels.\n")

if __name__ == "__main__":
    main()

