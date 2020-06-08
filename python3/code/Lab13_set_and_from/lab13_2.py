#!/usr/bin/env python3
"""
A function that gather texts interactively and reports the
non-white-space characters that all the texts have in common.
"""
import string
def ReportCharsInCommon():
    """Collects number_of_texts texts from the user and reports
    the printable characters that all the texts have in common.
    """
    common_chars = set(string.printable)
    while True:
        text = input("Type something: ")
        if not text:
            break
        text_chars = set(''.join(text.split()))
        common_chars = common_chars.intersection(text_chars)
        
    in_common_list = sorted(list(common_chars))
    if in_common_list:
        print(f"Your texts have the characters: {', '.join(in_common_list[:-1])} and {in_common_list[-1]} in common.")
    else:
        print(f"Your texts have no characters in common.")

def main():
    ReportCharsInCommon()

if __name__ == "__main__":
    main()
