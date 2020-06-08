#!/usr/bin/env python3
"""
A dictionary with the keys being each day's name, and
the values are a tuple of (temp, precip, wind).
"""
def ShowDailies(*seqs):
    days = "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"
    dailies = {data[0]:data[1:] for data in zip(days, *seqs)}
    for day in sorted(dailies, key=lambda d:days.index(d)):
        print(f"{day:>20}:",
              '\t'.join(f"{n:>10}" for n in dailies[day]))

def main():
    temps = [80, 82, 85, 87, 76]
    precip = [0, 2, 44, 100, 0]
    wind = ["2SW", "7SW", "3S", "10S", "2W"]
    ShowDailies(temps, precip, wind)

if __name__ == "__main__":
    main()
