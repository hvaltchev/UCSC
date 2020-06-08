#!/usr/bin/env python3
""" Remember this lab solution:
---
def DoBreakfast(meat="bacon", eggs="over easy", 
                potatos="hash browns", toast="white", 
                beverage="coffee"):
    print(f"Here is your {meat} and {eggs} eggs with {potatos}"
          f" and {toast} toast.", 
          f"Can I bring you more {beverage}?", sep='\n')

def main():
    DoBreakfast()
    DoBreakfast("ham", "basted", "cottage cheese",
                "cinnamon", "orange juice")
    DoBreakfast("sausage", beverage="chai", toast="wheat")
----
Now we can do this:
"""
               
def DoBreakfast(**substitutions): 
    order = {"meat":"bacon","eggs":"over easy",
                    "potatos":"hash browns",   
                    "toast":"white","beverage":"coffee"}
    # updating values in order from substitutions
    order.update(substitutions)  

    print(f'Here is your {order["meat"]} and {order["eggs"]} with {order["potatos"]} and {order["toast"]} toast.')
    print(f'Can I bring you more {order["beverage"]}?')

    print("str.format: Can I bring you more {beverage}?".format(**order))

    print("%%-style of string formatting: Can I bring you more %(beverage)s?" % order)

def main():
    print("Call:  Do Breakfast()")
    DoBreakfast()
    print('\nCall: DoBreakfast(meat="sausage", toast="wheat", beverage="chai")')
    DoBreakfast(meat="sausage", toast="wheat", beverage="chai")

if __name__ == "__main__":
    main()
