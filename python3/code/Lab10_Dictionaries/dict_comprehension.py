#!/usr/bin/env python3
"""
Demonstrates a dictionary comprehension.
"""
def MakeSqrs(seq):
    return {str(n):n*n for n in seq}

def MakeDict(*seqs):
    return {data[0]:data[1:] for data in zip(*seqs)}

def main():
    print(MakeSqrs(range(5)), end="\n\n")
    people = ["Lorena", "Isabel", "Ricardo", "Paco"]
    instruments = ["guitar", "salterio", "marimba", "vihuela"]
    gender = ["woman", "woman", "man", "man"]
    band = MakeDict(people, instruments, gender)
    print('\n'.join(f"{k:>10}:{band[k]}" for k in sorted(band)))

if __name__ == "__main__":
    main()

