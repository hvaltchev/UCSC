#!/usr/bin/env python3
"""
Copy the cats.txt into your area.  Change the file so
that all the cats become dogs and dogs become cats.
"""
import do_swap
import shutil  

def Swapper(file_name, apple, orange):
    """ Changes the text in the file, replacing apples with
    oranges and oranges with apples."""
    try:
        with open(file_name, "r+") as open_file:
            text = open_file.read()  
            text = do_swap.DoSwap(text, apple, orange)
            open_file.seek(0, 0)
            open_file.truncate() 
            open_file.write(text)
    except OSError as info:
        print(f"Can't open {file_name} because {info}")

def main():
    shutil.copy("cats.txt", "cats2.txt")
    Swapper("cats2.txt", "cat", "dog")
    Swapper("www.txt", "www", "yyy")
    
if __name__ == "__main__":
    main()
