#!/usr/bin/env python3
"""Reading a file and catching errors, and closing the file.
"""
def PrintFile(file_name): 
    try:                                      
        file_obj = open(file_name)            
        for line in file_obj:
            print(line, end='')
    except OSError as info:
        print(info)
    finally:
        try:
            file_obj.close()
        except UnboundLocalError:
            pass

def main():
    PrintFile("ram_tzu.txt")
    print()
    PrintFile("absent_file")

if __name__ == "__main__":
    main()
