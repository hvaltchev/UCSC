#!/usr/bin/env python3
"""
Demonstrates what happens in the caller when passing in mutable
and immutable types.
"""
def Manipulate(this):
    this[1] = "tomatoes"

def TestManipulate(this):
    print(f"this = {this}")
    try:
        Manipulate(this)
    except TypeError as msg:  # msg has more info.
        print(f"Oops {this} broke with {msg}.")
    else:
        print(f"OK. Now we have {this}.")
        
def main():
    a_list = ["sirloin", "t-bone", "chuck"]
    a_str = "coleslaw"
    a_tuple = ("berries", "peaches", "watermelon")
    a_number = 4.4
    for thing in a_list, a_str, a_tuple, a_number:
        TestManipulate(thing)

if __name__ == "__main__":
    main()
