#!/usr/bin/env python3
"""Reading data and pointing out the data flaws.
"""
import shutil

class BadData(ValueError):
    pass

def CheckData(d_file, number_across):
    with open(d_file) as f_obj:
        for i, line in enumerate(f_obj, 1):
            number_list = line.split()
            number_of_numbers = len(number_list)
            if number_of_numbers != number_across:
                raise BadData(f"""{d_file} line #{i:4}: {line}
       has {number_of_numbers} elements.""")
            try:
                [float(n) for n in number_list]
            except ValueError:
                raise BadData(f"""{d_file}, line #{i:4}: {line}
       is not all floats.""")
                raise
            
    return f"{d_file} has {i} lines and {number_across * i} numbers."

def main(d_file="data.txt", number_across=8):
    yn = input("Renew the data? ")
    if yn and yn[0] in "yY":
        shutil.copy("bad_data.txt", "data.txt")
    print(CheckData(d_file, number_across))

if __name__ == "__main__":
    main()

