#!/usr/bin/env python3
"""Global/module-level identifier behavior.""" 

pies = 1 # global identifier 

def DoApple(): 
   """alters the local pies, shadows the global identifier"""
   pies = 25 
   print(f"Apple: local pies in DoApple() is {pies}.")
   pies += 1
   print(f"Apple ends: local pies = {pies}")

def DoBerry():
   """assigning the global identifier pies"""
   global pies
   print(f"Berry: global pies is {pies}.")
   pies *= 10
   print(f"Berry ends: global pies is {pies}.") 

def DoCherry():
   """referencing the global identifer"""
   print(f"Cherry: no problem with referencing global pies = {pies}")

def DoMud():
   """assigning after reference -- reference doesn't work"""
   print(f"Mud(): pies = {pies}")
   pies = 999

DoApple()
DoBerry()
DoCherry()
DoMud()
