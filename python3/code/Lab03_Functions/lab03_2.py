#!/usr/bin/env python3
""" Write a function that returns a total cost from the 
sales price and sales tax.  The default value for the 
tax rate should be 8.25%.
"""


def CalculateCost(price, tax=.0825):
    return price * (1 + tax)

def main():
    print(" price |   .0825 |   .0925")
    for price in range(50, 1001, 50):
        dollars = price/100
        print(f"${dollars:5.2f} | ${CalculateCost(dollars):6.2f}"
           f" | ${CalculateCost(tax=.0925, price=dollars):6.2f}")
            
main()
