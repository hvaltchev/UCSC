#!/usr/bin/env python3
"""att2.py
You can override assigning and referencing attributes.

referencing: 

      object.x -> calls __getattr__ (if provided)

  but only if the x attribute does not exist.

assignment:

      object.x = 3  -> calls __setattr__ (if provided)
"""  
class Secret: 
    """The secret can only be set on initialization:
    s = Secret("rose") and only the allowed attributes
    can be set. """

    __ALLOWED_ATTRIBUTES = ("members", "purpose")

    def __init__(self, secret):
        self.__dict__["_Secret__secret"] = secret
        # Here we snuck around __setattr__ by adding directly 
        # to the __dict__, so that we could disallow the 
        # secret to be set after initialization.  And, we had
        # to do our own name mangling to keep it pseudo-secret.

    def IsSecret(self, word):
        return self.__secret == word

    def __getattr__(self, attribute_name):
        if attribute_name == "secret":
            return "a secret!"
        raise AttributeError(f"{self.__class__.__name__} instance has no attribute '{attribute_name}'")

    def __setattr__(self, attribute_name, value):
        if attribute_name == "secret":
            raise AttributeError(f"You can't change the {attribute_name} to {value}")
        if not attribute_name in self.__ALLOWED_ATTRIBUTES:
            raise AttributeError(f"{attribute_name} is not an attribute for class {self.__class__.__name__}")
        self.__dict__[attribute_name] = value
        # setattr(self, attribute_name) would loop forever!

def main():
    club = Secret("snake")
    print(f"club.secret is {club.secret}", end=' ')
    print(f'club.IsSecret("snake") {club.IsSecret("snake")}')
    try:
        print(f"club.x is {club.x}")
    except AttributeError as info:
        print(f"\nError: {info}")
    try:
        print(f"club.members is {club.members}")
    except AttributeError as info:
        print(f"\nError: {info}")
    club.members = 7
    print(f"club.members is {club.members}")
    try:
        club.secret = "lizard"
    except AttributeError as info:
        print(f"Error: {info}")
    try:
        print("Setting club.x", end=' ')
        club.x = "cucumber"
    except AttributeError as info:
        print("\nError: {info}")
    print(dir(club))
if __name__ == "__main__":
    main()
