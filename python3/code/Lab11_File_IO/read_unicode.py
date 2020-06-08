#!/usr/bin/env python3
"""Demonstrates changing encoding.
"""
import locale, os

def ReadFile(f_name, encoding):
    with open(f_name, encoding=encoding) as file_object:
        for line in file_object:
            for char in line:
                if ord(char) > 128:
                    print(line, end='')

def ChangeEncoding(f_name, now_in, change_to):
    path, name = os.path.split(f_name)
    front, ext = name.rsplit('.', 1)
    new_f_name = os.path.join(path, f"{front}_{change_to}.{ext}")
    try:
        with open(f_name,
                  encoding=now_in) as read_file:   
            with open(new_f_name, "w",
                      encoding=change_to) as write_file:
                for line in read_file:   
                    write_file.write(line)
    except OSError as info:
        print(info)
    return new_f_name

def main():
    default_encoding = locale.getpreferredencoding()
    the_file = "../Lab040_Formatting_Strings/uni.py"
    print("Reading with preferred encoding for the computer = "
          f"{default_encoding}:")
    ReadFile(the_file, default_encoding)
    
    other_encoding = "utf-16"
    new_file = ChangeEncoding(the_file, default_encoding,
                              other_encoding)
    print(f'\nReading with "{other_encoding}":')    
    ReadFile(new_file, other_encoding)

    print(f"\nReading with wrong encoding: {default_encoding}:")    
    ReadFile(new_file, default_encoding)

if __name__ == "__main__":
    main()
