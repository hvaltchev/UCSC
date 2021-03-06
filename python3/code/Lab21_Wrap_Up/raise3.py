#!/usr/bin/env python3
"""The argument you give to your raise can be anything, 
a string is most common, but a sequence is possible."""
     

def GetPositiveNumber(prompt):
    """Writes the prompt to stdout and collects the response.
    Returns an int > 0 if one was given, ValueError otherwise,
    giving back the non-positive number, if that was the
    problem.
    """
    said = input(prompt)
    number = float(said)
    if number > 0:
        return number
    raise ValueError("Number given must be positive.", number)

def main():
    try:
        print(GetPositiveNumber("Positive number: "))
    except ValueError as exception_object:
        print(exception_object)

main()

