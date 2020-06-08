#!/usr/bin/env python3
"""
lab18_2.py Tree and Forest classes with __str__.			  
"""
import random
import sys

class Tree:
    """Instantiate:  Tree(20) to make a tree 20 ft tall.
    """
    def __init__(self, height):
        self.height = height

    def __str__(self):
        return f"tree, {self.height:.1f} feet tall"

class Forest:
    """Instantiate: Forest(size="medium")
    if size == "large", it will have 8 trees.
            == "medium", it will have 5 trees.
            == "small", it will have 2 trees.
    """
    def __init__(self, size="medium"):
        if size not in ("small", "medium", "large"):
            raise ValueError(f"""Intantiate with: Forest([size="medium"]) where size can be "small", "medium", or "large", not "{size}".""")
        self.size = size
        self.number_of_trees = 8 if self.size == "large" else 5 if self.size == "medium" else 2
        self.trees = [Tree(random.randrange(1, 200)) 
                      for count in range(self.number_of_trees)]

    def __str__(self):
        say = f"{self.size} forest with {self.number_of_trees} trees:"
        say += ", ".join([str(t) for t in self.trees])
        return say

def main():
    forest = Forest("small")
    print("print output:", forest, sep='\n')
    print(f"f-string:\n{forest}")
    print("str.format:\n{}".format(forest))
    print("Format replacement:\n%s" % forest)
    print("And with str:\n" + str(forest))

if __name__ == "__main__":
    main()
