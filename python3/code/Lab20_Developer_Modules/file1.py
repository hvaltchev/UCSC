#!/usr/bin/env python3
"""Demonstrates reading a file line by line."""

def PrintFile(f_name):   
    with open(f_name) as open_file:   
        for line in open_file:   
            print(line, end=' ')

def main(f_name):
    PrintFile(f_name)

if __name__ == "__main__":
    main("ram_tzu.txt")
