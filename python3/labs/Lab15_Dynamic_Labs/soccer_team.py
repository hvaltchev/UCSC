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
"""
$ soccer_team.py
Yeh Bruce Penge #7 Go for the goal!
Yeh Maureen Mezzabo #1 Go for the goal!
Yeh Samantha Smith #8 Go for the goal!
Yeh Juvenal Ramirez #6 Go for the goal!
Yeh Xavier Perra #4 Get that ball!
Yeh Laura Dot #2 Get that ball!
Yeh Malcolm Diamond #5 Get that ball!
Yeh Mary Bart #9 Get that ball!
Yeh Linda Jarvis #3 Block that kick!
Yeh Jose Acosta #11 Guard the goal!
Yeh Tracy Lowe #10 Guard the goal!

Bees:
  Forwards:
    1: Maureen Mezzabo
    6: Juvenal Ramirez
    7: Bruce Penge
    8: Samantha Smith
  Midfielders:
    2: Laura Dot
    4: Xavier Perra
    5: Malcolm Diamond
    9: Mary Bart
  Defenders:
    3: Linda Jarvis
  Goalies:
    10: Tracy Lowe
    11: Jose Acosta

The Bees data file:
Forwards:
7 Bruce Penge
1 Maureen Mezzabo
8 Samantha Smith
6 Juvenal Ramirez
Midfielders:
4 Xavier Perra
2 Laura Dot
5 Malcolm Diamond
9 Mary Bart
Defenders:
3 Linda Jarvis
Goalies:
11 Jose Acosta
10 Tracy Lowe
$"""
