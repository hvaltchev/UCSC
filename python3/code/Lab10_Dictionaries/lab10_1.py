#!/usr/bin/env python3
"""Dictionary implementation for demonstrating a dictionary.

   ... with a new option will print out the dictionary 
   alphabetically by the meanings. """

from py_dict_def import *  # Careful of this!

def ListDefinitions(py_dict):
    """Prints out the dictionary, alphabetically by the
    meanings"""
    defs = [] 
    for k, v in py_dict.items(): 
        defs += [(v, k)]
    # or: defs = [(v, k) for (k, v) in py_dict.items()]        
    defs.sort()
    for (v, k) in defs:
        print(v, ':', k)

def ListDefinitions(py_dict):
    """Prints out the dictionary, alphabetically by
    the meanings -- implemented via the sort key option."""
    def ValueKey(k):
        return py_dict[k]

    for each in sorted(py_dict, key=ValueKey):
        print(py_dict[each], ':', each)



















        
def RunMenu(py_dict):
    """Runs the user interface for dictionary manipulation."""
    # The choices dictionary has function names for values.
    choices = {"add": CollectEntries,
               "definitions": ListDefinitions,
               "find": FindDefinitions, "print": PrintEntries}
    prompt = MakePrompt(choices)

    while True:
        raw_choice = input(prompt)
        if not raw_choice:
            break
        given_choice = raw_choice[0].lower()
        for maybe_choice in choices: 
            if maybe_choice[0] == given_choice:
                # The appropriate function is called
                # using the dictionary value for the name
                # of the function.    
                choices[maybe_choice](py_dict)
                break
        else:
            print(f"{raw_choice} is not an acceptible choice.")

def main():
    py_dict = SetUpPyDict()
    RunMenu(py_dict)

if __name__ == "__main__":
    main()
