#!/usr/bin/env python3
"""
Write a function that reads a file and finds all the
numbers in the file and adds them up. 
"""

import sys, os

# putting apple on the search path 
sys.path.insert(0, os.path.join(os.path.split(__file__)[0], ".."))

import banana.total_text     # banana must have __init__.py

def TotalIt(stream, total=0):
    """Returns the sum of all the numbers in stream, which is 
    an open file object."""
    try:
        for line in stream:
            total += banana.total_text.TotalText(line)
    except UnicodeDecodeError:
        print(stream.name)
        sys.exit()
    return total

def TotalFile(file_name):
    """Returns the sum of all the numbers in the file."""
    with open(file_name) as open_file:
        return TotalIt(open_file)
    
def main():
    while True:
        try:
            file_name = input("File name: ")
        except (KeyboardInterrupt, EOFError):
            print()
            break
        if file_name == '':
            break
        total = TotalFile(file_name)
        if total:
            print(file_name, "totals to", total)

if __name__ == "__main__":
    main()

