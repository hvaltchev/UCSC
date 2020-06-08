#!/usr/bin/env python3
"""
next() is used to make a generator function that walks
a directory structure and delivers tuples to the caller.
Delivered is (file_path, first_line).
"""
import os, sys

def DriveFirstLines():
    if len(sys.argv) == 1:
        start_dirs = ['.']
    else:
        start_dirs = sys.argv[1:]
    for start_dir in start_dirs:
        for path, first_line in FirstLines(start_dir):
            if path:
                print(path, '\t' + first_line, end='')

def FirstLines(start_dir):
    for this_dir, dirnames, file_names in os.walk(start_dir):
        if this_dir == start_dir:
            dirnames.sort()
        for file_name in sorted(file_names):
            whole_path = os.path.join(this_dir, file_name)
            with open(whole_path) as file_object:
                try:
                    first_line = next(file_object, "Can't read it.")
                except UnicodeDecodeError:
                    first_line = "unicode error\n"
            yield (whole_path, first_line)

def main():
     DriveFirstLines()

if __name__ == "__main__":
    main()
