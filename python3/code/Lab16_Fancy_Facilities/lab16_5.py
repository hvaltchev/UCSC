#!/usr/bin/env python3
"""
Testing dice.py by reading it as a text file, making a little
change, and then executing it, via the exec command.
"""
import sys, os

def GetDiceCodeString():
    """Read the dice.py file as text and change random.randrange
    to be next(doubles_generator_object), and return the text.
    """
    file_path = os.path.join("..", "Lab05_Libraries", "dice.py")
    with open(file_path) as open_file:
        dice_code = open_file.read()

    dice_code = dice_code.replace(
        "random.randrange(1, 7)",
        "next(doubles_generator_object)")
    # The __name__ is "__main__" so the code will run when
    # exec-ed.  Stopping that:
    end_at = dice_code.find("def main")
    dice_code = dice_code[:end_at]
    return dice_code

def RollDeterminedDice():
    """Returns a roll of the dice, in order so that doubles
    are rolled.
    """
    for die in range(1, 7):
        yield die
        yield die

def TestRollem():
    """Tests the Rollem function in dice.py.
    """
    global doubles_generator_object
    # doubles_generator_object needs to be in the global 
    # space for Rollem() to find it.
    
    dice_code = GetDiceCodeString()

    doubles_generator_object = RollDeterminedDice()

    exec(dice_code + "\nfor roll in range(6): print(Rollem())")
    """  This worked in python2 but now exec has its own namespace.
    for roll in range(6):
        print(Rollem())
    """
    
TestRollem()
