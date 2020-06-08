#!/usr/bin/env python3
"""
Reports the number of vowels in the directory structure given.
"""
import os, sys
import lab11_2 as count_vowels_in_file

def CountVowelsInDir(dir_name):
    total = 0
    for this_dir, dir_names, file_names in os.walk(dir_name):
        for file_name in file_names:
            whole_path = os.path.join(this_dir, file_name)
            total += \
            count_vowels_in_file.CountVowelsInFile(whole_path)
    return total

def main(dir_name="cats"):
    print(f"{CountVowelsInDir(dir_name)} vowels in {dir_name} directory")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main()
"""
$ lab12_1.py
576 vowels in cats directory
"""
