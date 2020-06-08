#!/usr/bin/env python3
"""prof.py (Optional) Demonstrates the profiler which reports 
info about the time it takes to run functions.""" 
import cProfile

def TryWay(data, index):
    """Uses try/except to return data or None.
    """
    try:
        return data[index]
    except IndexError:
        return None

def TestWay(data, index):
    """Tests the index to return None if there is no
    data for the index.
    """
    if index < -len(data) or index > len(data) - 1:
        return None
    return data[index]

def TestWay2(data, index):
    """Checks the i (index) against the len(data) to 
    determine if there is no data.
    """
    data_len = len(data)
    if index < -data_len or index > data_len - 1:
        return None
    return data[index]

def TestPercentWrong(percent_wrong, trials=10000):
    """Tests the three functions with the a certain
    percent of failures. """
    print(f"Testing {percent_wrong:.2%} wrong.")
    percent_wrong *= 100
    data = list(range(100))
    good_count = bad_count = 0
    for trial in range(trials):
        for index in range(100):
            if index < percent_wrong:
                index = -index
                bad_count +=1
            else:
                good_count +=1
            TryWay(data, index)
            TestWay(data, index)
            TestWay2(data, index)
    assert bad_count/(bad_count + good_count) == percent_wrong/100
    
def main():
    for percent in (.10, .01):
        cProfile.run(f"TestPercentWrong({percent})")
            
if __name__ == "__main__":
    main()
