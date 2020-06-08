#!/usr/bin/env python3
"""Demonstrates variable number of arguments with '*'."""

def PrintFavoriteThings(*things):
    print("These are a few of my favorite things: ")
    for thing in things:
        print(thing, end=" ")
    print()

def main():
    my_things = "raindrops", "roses", "whiskers", "kittens"
    PrintFavoriteThings(*my_things)

main()
