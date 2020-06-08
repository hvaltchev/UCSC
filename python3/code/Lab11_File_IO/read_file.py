#!/usr/bin/env python3
"""Demonstrates reading a file line by line, automatic
exception handling in a "context"."""

def PrintFile(f_name):   
    try:
        with open(f_name) as open_file:   
            for line in open_file:   
                print(line, end='')
    except OSError as info:
        print(info)

def main():
    PrintFile("ram_tzu.txt")
    print()
    PrintFile("absent_file")

if __name__ == "__main__":
    main()
