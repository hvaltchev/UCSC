#!/usr/bin/env python3
""" 
Get info about your caught exception from sys and traceback
modules."""

import sys      
import traceback  
                     
def Fun():    
    raise ArithmeticError("Fake message.")

if __name__ == "__main__":
    try:
        Fun()
    except:
        print("sys.exc_type =", sys.exc_info()[0])
        print("sys.exc_value =", sys.exc_info()[1])
        print("---")
        print(traceback.format_exc(), end=' ')
        print("---")

