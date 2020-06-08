#!/usr/bin/env python3
"""Demonstrating the sys module.""" 

import sys 
           
def DemoOpenStreams():
    """Demos stderr, stdout and stdin.  Also sys.exit()"""
    sys.stderr.write("You can write to stderr.\n")
    sys.stderr.flush()   
    print("You might want to redirect print's output.", file=sys.stderr)
    sys.stdout.write("A fancier way to write to stdout.\n")
    sys.stdout.flush()
    print("Type something: ")
    text = sys.stdin.readline()
    print("You said:", text)

def DemoCommandLine(): 
    """Shows the command line."""
    print(f"This program is named: {sys.argv[0]}")
    print(f"The command line arguments are: {sys.argv[1:]}")

def main():
    DemoCommandLine()
    DemoOpenStreams()
main()

