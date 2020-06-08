#!/usr/bin/env python3
"""The "assert" statement is useful while debugging.  It goes
away under any optimization."""  

def main():
    number = float(input("Give me a positive number: "))

    assert number > 0, f"Input is not positive: {number}"

    print(f"Good. {number} is positive.")

if __name__ == "__main__":
    main()

