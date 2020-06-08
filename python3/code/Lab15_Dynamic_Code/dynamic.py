#!/usr/bin/env python3
"""Demonstrates the exec and eval builtin functions, used
for dynamic code generation.
""" 
import sys 

ATTRIBUTES = ("name", "zip", "phone", "SSN")

def GetAttributes(attributes):
    for each in attributes:
        answer = input(f"{each} please: ")
        exec(f"{each} = '{answer}'", globals())

def PrintAttributes(attributes):
    for each in attributes:
        print(f"{each} = {eval(each)}")

def main():
    if len(sys.argv) > 1:
        attributes = sys.argv[1:]
    else:
        attributes = ATTRIBUTES
    GetAttributes(attributes)
    PrintAttributes(attributes)

main()
