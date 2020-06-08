#!/usr/bin/env python3
"""
lab09_3.py Provides a MakeString function that receives a
glue string and any number of any objects, returns a string
containing all of the elements, each separated by the glue
string.  
"""
def MakeString(glue, *objects):
    return glue.join([str(obj) for obj in objects])

def main():
    print(MakeString(", ", *range(10, 0, -1)))
    print(MakeString('*', '1', 2, "word"))

if __name__ == "__main__":
    main()
