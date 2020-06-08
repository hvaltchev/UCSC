#!/usr/bin/env python3
"""
Demonstrates a dictionary comprehension.
"""
def ReverseDict(text):
    return {k.lower():k.lower()[::-1] for k in text.split()}

def main():
    word_dict = ReverseDict("Keep a fire burning in your eye.")
    print('\n'.join(f"{k:>10}:{word_dict[k]}"
                    for k in sorted(word_dict)))

if __name__ == "__main__":
    main()

