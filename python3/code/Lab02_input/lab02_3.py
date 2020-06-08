#!/usr/bin/env python3
"""I'm thinking-of-a-number game. """

print("Think of a number between 1 and 10",
      "and I'll try to guess it.")
high = 10
low = 1
guesses = 0
while high >= low:
    guesses += 1
    guess = (high + low)//2
    print(f"Is your number {guess}?")
    while True:
        answer = input("""Please press:
        'y' for yes
        'n' for no
        """)
        answer = answer[0].lower() # details coming
        if answer in "yn":
            break
        print("Please follow directions.")
    if answer == 'y':
        print(f"Hurray! Only {guesses} guesses.")
        break

    while True:
        answer = input(f"""No?  Then please press:
        'h' if {guess} is higher than your number
        'l' if {guess} is lower than your number
        """)
        if answer[0].lower() in "lh":
            break
        print("Please follow directions")

    if answer == 'l':
        low = guess + 1
    else:
        high = guess - 1

