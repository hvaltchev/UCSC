#!/usr/bin/env python3
"""Function with many arguments and many return values.""" 


def Analyze(one, other):      
    total = sum((one, other)) # sum demands a sequence
    average = total/2.0       # min and max are flexible
    return min(one, other), max((one, other)), total, average 

def Print(min_number, max_number, total, average):
    print(f"min_number={min_number},",
          f"max_number={max_number},",
          f"total={total:.2f},",
          f"average={average:.2f}.")

def main():
    min_number, max_number, total, average = Analyze(1, 8)
    Print(min_number, max_number, total, average)
    """
    Output so far:

min_number=1, max_number=8, total=9.00, average=4.50.
    """
    answer = Analyze(100, 50)
    min_number, max_number, total, average = answer
    Print(min_number, max_number, total, average)
    """
    Output from this:
    
min_number=50, max_number=100, total=150.00, average=75.00.
    """
    numbers = 50, 20
    answers = Analyze(*numbers)
    Print(*answers)
    """
    Output from this:
    
min_number=20, max_number=50, total=70.00, average=35.00.
    """
        
main()
