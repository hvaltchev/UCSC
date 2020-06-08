#!/usr/bin/env python3
"""
Another input pattern.
"""   
PER_GALLON = 200      # A can of paint covers 200 square feet
sq_ft = 0 
while sq_ft == 0:
    said = input("Number of square feet to paint: ")
    if not said:   # or if said == '':
        print("Thank you anyway.") 
        break
    try:
        sq_ft = int(said)
    except ValueError:
        print("Please give a whole number.")
else:
    no_cans = sq_ft//PER_GALLON   # // is integer division
    if sq_ft % PER_GALLON > 0:    # Leftover after division
        no_cans += 1
        print(f"You need {sq_ft/PER_GALLON:.1f} cans"
              " so you'd better buy", end= ' ')
    else:
        print("You need exactly", end=' ')
    print(f"{no_cans} {'can' if no_cans==1 else 'cans'}.")
