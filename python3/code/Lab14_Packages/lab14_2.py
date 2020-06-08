#!/usr/bin/env python3
"""Using os.walk to accumulate total through the files walked.
"""

import os
import apple.work_here.lab14_1 as totaler

def TotalDeep(starting_dir):
    """Returns (no_of_files, total) where no_of_files is the
    number of files founds in the directory structure starting 
    at starting_dir, and total is the sum of all the numbers 
    found in those files.
    """
    total = no_of_files = 0
    for (this_dir, dir_names,
         file_names) in os.walk(starting_dir):
        for this_file in file_names:
            path_name = os.path.join(this_dir, this_file)
            try:
                total += totaler.TotalFile(path_name)
                no_of_files += 1
            except OSError as info:
                print(path_name, info)
    return (no_of_files, total)

def main():
    stats = TotalDeep("..")
    print(f"That's {stats[0]} files, totaling to {stats[1]}.")

if __name__ == "__main__":
    main()

