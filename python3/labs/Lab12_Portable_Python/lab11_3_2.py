#!/usr/bin/env python3
"""lab11_3 again.  This time using the builtin file
iterator, so that all the file isn't in memory at one time,
and using tempfile."""
import os
import shutil
import tempfile   
import do_swap

def Swapper(file_name, apple, orange):
    """ Changes the text in the file, replacing apples with
    oranges and oranges with apples."""
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        # temp_file is an open file object, open for writing
        try:
            with open(file_name) as open_file:
                for line in open_file:
                    swapped_line = do_swap.DoSwap(line, apple, orange)
                    temp_file.write(bytes(swapped_line,
                                        encoding="utf-8"))
        except OSError as info:
            print(f"Problem with {file_name} because {info}")            

    os.rename(temp_file.name, file_name) # For Windows, first:
                                         # os.remove(file_name)
def main():
    shutil.copy("cats.txt", "cats2.txt")
    Swapper("cats2.txt", "cat", "dog")
    Swapper("www.txt", "www", "yyy")

if __name__ == "__main__":
    main()
"""
$ lab11_3_2.py
Problem with www.txt because [Errno 2] No such file or directory: 'www.txt'
$ cat cats2.txt

In my house we have 3 dogs who love to tease our old cat.  The old cat
gets quite bewildered when they take turns running in front of him and
getting in his way.  He steps around one dog, then the next dog, then
[The rest of the output is deleted.]"""
