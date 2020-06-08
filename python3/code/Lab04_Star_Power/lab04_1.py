#!/usr/bin/env python3
"""DoBreakfast() with 5 items.  -- From last lab.
"""
def DoBreakfast(meat="bacon", eggs="over easy", 
                potatos="hash browns", toast="white", 
                beverage="coffee"):
    print(f"Here is your {meat} and {eggs} eggs with {potatos}"
          f" and {toast} toast.", 
          f"Can I bring you more {beverage}?", sep='\n')

def main():
    items = ("ham", "poached", "home fried", "English muffin")
    DoBreakfast(*items)
    
main()
