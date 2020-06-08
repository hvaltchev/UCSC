#!/usr/bin/env python3
"""Reads all the .py files in the current directory and
lists the unique words.
"""
import os, string 

def FindUniqueWords():
    """Finds the set of unique words in all the ".txt" files in
    the current directory.
    """
    unique_words = set()
    for file_name in os.listdir('.'):
        if not file_name.endswith(".txt"):
            continue
        with open(file_name) as f_obj:
            for line in f_obj:
                for word in line.split():
                    word = word.strip(string.punctuation)
                    unique_words.add(word.lower())
    return unique_words

def FormatWords(words, width=50): 
    def ProcessWord(word):
        nonlocal line_len  # for namespace between here and global
        word_len = len(word) 
        line_len += word_len
        if line_len > width:
            line_len = word_len
            ret_lines.append(''.join(this_lines_words))
            this_lines_words.clear()
        this_lines_words.append(word)
        
    ret_lines = []
    this_lines_words = []
    line_len = 0
    words = sorted(list(words))
    for word in words[:-1]:
        word = word + ", "
        ProcessWord(word)
    ProcessWord("and " + words[-1] + '.')
    ret_lines.append(''.join(this_lines_words))
    return '\n'.join(ret_lines)

def main():
    unique_words = FindUniqueWords()
    if unique_words:
        print(FormatWords(unique_words))

if __name__ == '__main__':
    main()

