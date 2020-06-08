#!/usr/bin/env python3
"""Optional: A decorator is a function for wrapping another
function, or many other functions.  Here we are timestamping
the function calls.""" 
import time  

def TimeDecorator(Func):
    """Decorator function for reporting when the function
    was called."""
    def WrappedFunction(*args, **kw_args):
        print(f"It's {time.ctime()}, time to {Func.__name__}:")
        return Func(*args, **kw_args)
    return WrappedFunction

def DoBreakfast(meat="bacon", eggs="scrambled"):
    print(f"Have some {meat} and {eggs} eggs.  Enjoy!")

DoBreakfast = TimeDecorator(DoBreakfast) 

@TimeDecorator  # syntax available in 2.5
def DoLunch(**substitutions):
    menu = {"meat":"ham", "cheese":"american", "bread":"white"}
    menu.update(substitutions)
    print(("Here's your %(meat)s and %(cheese)s"
           " on %(bread)s bread." % menu))

@TimeDecorator
def DoTea():
    print("Tea time!")

@TimeDecorator
def DoDinner(menu):
    print(f"{menu.title()} for dinner tonight.")

def main():
    DoBreakfast(meat="sausage", eggs="basted")
    time.sleep(1)
    DoLunch(cheese="swiss", bread="rye")
    time.sleep(1)
    DoTea()
    time.sleep(1)
    DoDinner("roast beef")

if __name__ == "__main__":
    main()
