#!/usr/bin/env python3 
"""The builtin next() function is handy to scrape one value
off an iterator.
"""
import generator

veggie_generator = generator.Harvest()

print(next(veggie_generator))

for veggie in veggie_generator:
    print(veggie)

toy_list = ["yo-yo", "ball", "doll"]
toy_generator = iter(toy_list)
print(next(toy_generator))
for toy in toy_generator:
    print(toy)

print(toy_list[0])
print('\n'.join(toy for toy in toy_list[1:]))

print(next(toy_list))

