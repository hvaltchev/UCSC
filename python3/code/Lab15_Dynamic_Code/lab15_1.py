#!/usr/bin/env python3
"""soccer_team.py with getattr and setattr."""

import sys 
from soccer_team import NotifyForwards, NotifyDefenders, NotifyMidfielders, NotifyGoalies 

this_module = sys.modules[__name__]

def ProcessTeam(stream):
    position_strs = []
    for line in stream:
        line = line.strip()
        if not line:
            continue
        if line.endswith(":"):
            position = line[:-1]
            setattr(this_module, position, [])
            position_strs += [position]
            continue
        details = line.split(" ", 1)
        setattr(this_module, position,
                getattr(this_module, position) + [details])
        print(f"Yeh {details[1]} #{details[0]} "\
                + getattr(this_module, f"Notify{position}")())
        return stream.name, position_strs

def PrintTeam(team_name, position_strs):
    print(team_name + ":")
    for each in position_strs:
        print("  {each}:")
        for player in sorted(eval(each)):
            print("    " + ": ".join(player))

def main(team_name = "Bees"):
    with open(team_name) as file_obj:
        team_name, position_strs = ProcessTeam(file_obj)
    PrintTeam(team_name, position_strs)
    print(f"\nThe {team_name} data file:")
    with open(team_name) as file_obj:
        sys.stdout.write(file_obj.read())

if __name__ == "__main__":
    main()
