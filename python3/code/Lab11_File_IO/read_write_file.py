#!/usr/bin/env python3
"""Demonstrates writing a file."""

def CapFile(starting_file):
    file_name, ext = starting_file.rsplit('.', 1)
    write_file_name = file_name + "_caps." + ext 
    with open(starting_file) as read_file:   
        with open(write_file_name, "w") as write_file:
            for line in read_file:
                write_file.write(line.upper())
    return write_file_name

def main(starting_file):
    import os
    new_file = CapFile(starting_file)     
    os.system(f"cat {new_file}")

if __name__ == "__main__":
    main("ram_tzu.txt")
