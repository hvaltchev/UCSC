#!/usr/bin/env python3
"""A Circle class, acheived by overriding __getitem__
which provides the behavior for indexing, i.e., [].
This also provides the correct cyclical behavior whenever
an iterator is used, i.e., for, enumerate() and sorted().
reversed() needs __reversed__ defined.
"""

class Circle: 

    def __init__(self, data, times):
        """Put the "data" in a circle that goes around
        "times" times."""
        self.data = data
        self.times = times

    def __getitem__(self, i): 
        """circle[i] --> Circle.__getitem__(circle, i)."""
        l_self = len(self)
        if i >= self.times * l_self:
            raise IndexError(f"Circle object goes around {self.times} times")
        return self.data[i % l_self]

    def __len__(self):
        return len(self.data)

def main():
    circle = Circle("around", 3)

    print("Works with circle[i], for i > len(circle) too:")
    for i in range(3 * len(circle) + 1):
        try:
            print(f"circle[{i:2d}] = {circle[i]}")
        except IndexError as info:
            print(info)
            break

    print("Works with sorted:")
    print(sorted(circle))

    print("Works for loops:")
    small_circle = Circle("XO", 2)
    for i, elementi in enumerate(small_circle):
        print(f"small_circle[{i}] = {elementi}")

        
    print("Works for nested loops:")
    for i, elementi in enumerate(small_circle):
        for j, elementj in enumerate(small_circle):
            print(f"{i:3d}:{j:3d} -> {elementi}{elementj}")

if __name__ == "__main__":
    main()

