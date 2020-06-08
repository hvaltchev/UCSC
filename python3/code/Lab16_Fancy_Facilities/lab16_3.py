#!/usr/bin/env python3
"""lab16_3.py (Optional) A logging lotto facility."""
import time
import random

LOG_FILE = "lotto.log"

def LogIt(Func):
    """Decorator function for logging output from the Func."""
    def LoggedFunction(*t_args, **kw_args):
        with open(LOG_FILE, "a") as open_log:
            got = Func(*t_args, **kw_args)
            open_log.write(f"{time.ctime()}  -> {Func.__name__}:{got}\n")
        return got
    return LoggedFunction

@LogIt
def Lotto():
    return random.sample(range(1, 53), 6)

def PrintLotto(the_pick):
    print(", ".join([str(x) for x in the_pick]))

def main():
    PrintLotto(Lotto())
    PrintLotto(Lotto())

if __name__ == "__main__":
    main()

