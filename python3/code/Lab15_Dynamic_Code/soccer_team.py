#!/usr/bin/env python3
"""Processing team data using exec and eval."""
import sys
def NotifyForwards(): 
    return "Go for the goal!" 
def NotifyDefenders():
    return "Block that kick!"
def NotifyMidfielders():
    return "Get that ball!"
def NotifyGoalies():
    return "Guard the goal!"

def ProcessTeam(stream):
    position_strs = []
    for line in stream:
        line = line.strip()
        if not line:
            continue
        if line.endswith(':'):
            position = line[:-1]
            exec(f"{position} = []", globals())
            position_strs += [position]
            continue
        details = line.split(' ', 1)
        exec(f"{position} += [details]")
        exec(f"print('Yeh {details[1]} #{details[0]} ' + Notify{position}())")
    return stream.name, position_strs

def PrintTeam(team_name, position_strs):
    print(f"\n{team_name}:") 
    for each in position_strs:
        print(f"  {each}:")
        for player in sorted(eval(each)):
            print("    " + ": ".join(player))

def main(team_name = "Bees"):
    with open(team_name) as file_obj:
        team_name, position_strs = ProcessTeam(file_obj)
    PrintTeam(team_name, position_strs)
    print(f"\nThe {team_name} data file:")
    with open(team_name) as file_obj:
        sys.stdout.write(file_obj.read())

main()
