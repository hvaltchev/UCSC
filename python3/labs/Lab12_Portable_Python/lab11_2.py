#!/usr/bin/env python3
"""
lab11_2.py
Write a function that takes a file name and returns
how many times a non-y vowel appears in the file's text.
"""
import sys
import lab09_6 as count_vowels

def CountVowelsInFile(file_name):
    """Returns the number of vowels in the file named.
    """
    vowel_count = 0
    with open(file_name) as file_obj:
        for line in file_obj:
            vowel_count += count_vowels.CountVowels(line)
    return vowel_count

def main():
    try:
        file_name = sys.argv[1]
    except IndexError:
        file_name = input("File name: ")
    if not file_name:
        file_name = "cats.txt"
    try:
        print(f"There are {CountVowelsInFile(file_name)} vowels in {file_name}.")
    except IOError as info:
        print(info, file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()

"""
$ lab11_2.py
File name: cats.txt
There are 96 vowels in cats.txt.
$ lab11_2.py
File name: 
There are 96 vowels in cats.txt.
$ lab11_2.py
File name: Bogus
[Errno 2] No such file or directory: 'Bogus'
"""
