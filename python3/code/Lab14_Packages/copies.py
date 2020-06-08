#!/usr/bin/env python3
"""copies.py

Demonstrating shallow and deep copies.  With dict.copy(), you
get a shallow copy where the dictionary values are references
of the same values that are in the original dictionary.
"""

import copy  
    
nest = {'a':[1, 2, 3], 'b':[11, 12, 13]}  
nest_copy = nest.copy()
print(f"     nest: {nest}")
print()

print("Hopefully, if you change one, you don't change the other.")
nest['b'] = [21, 22, 23]
print("After nest['b'] = [21, 22, 23]")
print(f"     nest: {nest}")
print(f"nest_copy: {nest_copy}")
print()

print("OK.  That worked.  But what if you change an element of a list (item assignment)?  Because the copy has a reference to the list, both reflect the change.")
nest['a'][1] = "surprise"
print('''After nest['a'][1] = "surprise"''')
print(f"     nest: {nest}")
print(f"nest_copy: {nest_copy}")
print()

print("""If you don't like that behavior, you can do a "deepcopy".""")
deep_copy = copy.deepcopy(nest)
nest['a'][1] = "independence"
print('''After nest['a'][1] = "independence"''')
print(f"     nest:{nest}")
print(f"deep_copy: {deep_copy}")
