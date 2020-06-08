#!/usr/bin/env python3
"""
Function that shows how to isolate "scissors" into the identifier to_cut}
and put the rest into meaningless identifiers, as few as possible?

And demonstrate what happens when there are no identifiers left for the *.
"""
def DoLab():
    tools = "hammer", "wrench", "scissors", "pliers", "ruler"
    to_hit, to_torque, to_cut, *rest = tools
    print(f"a: to_cut = {to_cut}")

    to_hit, to_torque, to_cut, to_pinch, to_measure, *rest = tools
    print(f"b: rest = {rest}")
    
def main():
    DoLab()

main()
