#!/usr/bin/env python3
"""
Egg and Basket classes.
"""
import random
class Egg:

    def __init__(self, bird_type, color):
        self.bird_type, self.color = bird_type, color

    def Report(self):
        return f"{self.color} {self.bird_type} egg"

class Basket:
    
    def __init__(self, max_eggs=12, **egg_dict):
        self.eggs = []
        self.max_eggs = max_eggs
        self.number_of_eggs = 0
        for bird_type in egg_dict:
            self.AddEgg(bird_type, egg_dict[bird_type])

    def AddEgg(self, bird_type, color):
        if self.max_eggs == self.number_of_eggs:
            print(f"Only {self.max_eggs} are allowed in this basket.")
            return
        self.eggs.append(Egg(bird_type, color))
        self.number_of_eggs += 1

    def Report(self):
        report = f"Basket for {self.max_eggs} with {self.number_of_eggs}:\n\t"
        number_width = len(str(self.max_eggs))
        report += "\n\t".join(f"{i:{number_width}}: {b.Report()}" for (i,b) in
                              enumerate(sorted(self.eggs, key=lambda b:b.bird_type),
                                        start=1))
        return report
        
def main():
    egg_data = {"hummingbird":"white",
                "song thrush":"blue",
                "tawny owl":"beige",
                "buzzard": "speckled brown",
                "chicken": "brown",
                "ostrich":"speckled yellow",
                "emu":"black" }
        
    basket = Basket(**egg_data)
    birds = list(egg_data.keys())
    how_many_left = basket.max_eggs - len(birds)
    for bird in range(how_many_left + 1):
        this_bird = random.choice(birds)
        basket.AddEgg(this_bird, egg_data[this_bird])

    print(basket.Report())
    
if __name__ == "__main__":
    main()

