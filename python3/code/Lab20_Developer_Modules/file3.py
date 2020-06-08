#!/usr/bin/env python3
"""Demonstrates the "finally" clause -- and making it happen.
"""    
def PrintFile(file_name, fail_on_read=False):
    try:
        open_file = file(file_name) #file is an alias for open
        try:                 
            for line in open_file:
                print(line, end='')
                if fail_on_read:
                    raise IOError("Failed while reading.")
        finally:
            print("Finally")
            open_file.close()
    except IOError as info:
        print(info)

def main(file_name="ram_tzu.txt"):
    print(f'\nCalling PrintFile("{file_name}")')
    PrintFile(file_name)
    print(f"""\nCalling PrintFile("{file_name}", fail_on_read=True)""")
    PrintFile(file_name, fail_on_read=True)
    print("""\nCalling PrintFile("absent_file")""")
    PrintFile("absent_file")

if __name__ == "__main__":
    main() 
