#!/usr/bin/env python3
"""
Another inheritance example, using the previous examples
by importing the old code.  This one implements __call__,
__str__, and __del__ and a class attribute."""

import sys, os
sys.path.insert(0, os.path.join(os.path.split(__file__)[0], ".."))

import Lab17_OOP.lab17_4 as employee_def   
import Lab17_OOP.greeter5_def as greeter_def 
     
class Welcomer(greeter_def.NamedGreeter,
               employee_def.SalariedEmployee):
    """Inherits from Salaried Employee"""
    welcomers = 0

    def __init__(self, name, pay_rate):
        Welcomer.welcomers += 1
        employee_def.SalariedEmployee.__init__(self, name, 
                                               pay_rate)

    def __call__(self, something): 
        print(f"{something} yourself!")

    def __del__(self):
        Welcomer.welcomers -= 1
        print(f'{self} says "Oh no!"')

    def __str__(self):
        return self.name

def main():
    Joe = Welcomer("Joe", 20000) # style-guide anxiety here!
    Joe.Greet()
    print(Joe, f"here's ${Joe.CalculatePay(80):.2f} for you. ")
    print()
    marsha = Welcomer("Marsha", 19500)
    marsha("Get to work")
    print()
    print(marsha, f"here's ${marsha.CalculatePay(80):.2f} for you. ")
    print()
    print(f"There are {Welcomer.welcomers} welcomers.")
    Joe("Goodbye")
    print("Deleting Joe")
    del Joe
    print(f"There are {Welcomer.welcomers} welcomers.")
    print()    
    marsha.Greet()
    print("marsha is going out of scope so runs through del.")

if __name__ == "__main__":
    main()
