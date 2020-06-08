#!/usr/bin/env python3
"""
Defines function that displays colors, 4 on a line.
"""
def DisplayColors():
    colors = ["beige", "silver", "charcoal", "royal blue",
              "aquamarine", "forest green", "chartreuse",
              "lime", "golden", "goldenrod", "coral", "salmon",
              "hot pink", "fuchsia", "lavender", "plum",
              "indigo", "maroon", "crimson", "lemon"]
    for i, color in enumerate(sorted(colors)):
        print(f"{color:15}", end=' ')
        if i % 4 == 3:
            print()
            
def main():
    DisplayColors()

if __name__ == "__main__":
    main()
