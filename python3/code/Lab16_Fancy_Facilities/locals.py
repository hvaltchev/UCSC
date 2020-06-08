#!/usr/bin/env python3
"""Demonstrates the locals() dictionary.
"""

def ReportAnimals(insect, bird, **more):
    cat = "Persian"
    fish = "platies"
    PrintDict("locals()", locals())
    locals().update(more)
    print("After update:")
    PrintDict("locals()", locals())
    print("Format tricks:")
    print("dog={dog}, bird={bird}, cat={cat}".format(**locals()))
    print("dog=%(dog)s, bird=%(bird)s, cat=%(cat)s" % locals())
    # dog is in the locals but f-string cannot find it
    # print(f"dog={dog}, bird={bird}, cat={cat}")
    
def PrintDict(message, the_dict):
    print(message)
    for key in sorted(the_dict):
        if type(the_dict[key]) == dict:
            PrintDict(f"{key} is internal dict in {message}:",
                      the_dict[key])
            print()
        else:
            print(f"{key:>20}:{the_dict[key]}")

def main():
    ReportAnimals("moth", "robin", dog="Collie", horse="Arabian")

if __name__ == "__main__":
    main()
