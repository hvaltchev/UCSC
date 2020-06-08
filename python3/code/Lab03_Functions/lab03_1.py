#!/usr/bin/env python3
"""
Pay close attention the specification and our style guide
as you code these little functions:
"""
def JudgeNumber(number):
    """Returns the number formatted to one decimal place
    in the sentence "Good number <number>."
    """
    return f"Good number {number:.1f}."

def PrintSillySentence(noun, verb):
    """prints "All of our <the noun> wanted to <the verb>"
    """
    print(f"All of our {noun} wanted to {verb}.")

def main():
    print("Testing JudgeNumber:")
    for number in (2, 8.3, 'x'):
        try:
            print(JudgeNumber(number))
        except ValueError:
            print(f"JudgeNumber did not like {number}.")

    print("Testing PrintSillySentence:")
    for noun, verb in (("cherry", "run"), (3, 2)):
        PrintSillySentence(noun, verb)

main()
