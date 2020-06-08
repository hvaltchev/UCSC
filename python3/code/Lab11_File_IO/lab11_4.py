#!/usr/bin/env python3
"""Finding the movie titles that need unicode."""

def ReportTitlesNeedingUnicode(data_file = "movies.csv"):
    movie_titles_needing_unicode = []
    with open(data_file, encoding="utf-8") as f_obj:
        for line in f_obj:
            title, *fields = line.split(',')
            title = title.strip()
            # if you don't strip it, there is a strange white-space after each title.        
            for char in title:
                if ord(char) > 127:
                    movie_titles_needing_unicode.append(title)
                    break
    print(', '.join(movie_titles_needing_unicode))
                

def main():
    ReportTitlesNeedingUnicode()
    
if __name__ == "__main__":
    main()

