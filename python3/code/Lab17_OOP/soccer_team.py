#!/usr/bin/env python3
"""                         ------
OO Implementation          | Team |
of a soccer team:           ------
                              / \
                              \ /   ("has" or "contains")
                               |
                        --------------------------------------
                       |                Player                |
                        --------------------------------------
                        /|\        /|\         /|\        /|\ 
                         |          | ("is a" or "inherits from")
                         |          |           |          |
                 ---------   ------------   ----------   --------
                | Forward | | Midfielder | | Defender | | Goalie |
                 ---------   ------------   ----------   --------
"""
import sys

class Player:
    """Base class for soccer players.  A "virtual" class that
    cannot be directly instantiated.
    """
    def __init__(self, line):
        if self.__class__ == Player:
            raise TypeError("Player class cannot be directly instantiated.")
        number, self.name = line.split(' ', 1)
        self.number = int(number)

    def Cheer(self):
        """Cheers the player with an encouragement appropriate
        for the position.
        """
        return f"Yeah {self.name}, #{self.number}! {self.encouragement}"
class Forward(Player):
    encouragement = "Go for the goal!"

class Defender(Player):
    encouragement = "Block that kick!"

class Midfielder(Player):
    encouragement = "Get that ball!"

    
class Goalie(Player):
    encouragement = "Guard the goal!"

class Team:
    """
    Container class for the players.
    """
    def __init__(self, data_file):
        self.players = []
        with open(data_file) as data_obj:
            for line in data_obj:
                line = line.strip()
                if not line or line[0] == '#':
                    continue
                if line.endswith(':'):
                    position = line
                    continue
                if position == "Forwards:":
                    new_player = Forward(line)
                elif position == "Midfielders:":
                    new_player = Midfielder(line)
                elif position == "Defenders:":
                    new_player = Defender(line)
                elif position == "Goalies:":
                    new_player = Goalie(line)
                else:
                    raise ValueError(f"Unknown soccer position: {position}")
                self.players.append(new_player)

    def Cheer(self):
        return "\n".join([player.Cheer() for player in sorted(
            self.players, key=lambda p:p.number)])

def main():
    try:
        data_file = sys.argv[1]
    except IndexError:
        data_file = "../Lab15_Dynamic_Code/Bees"
    team = Team(data_file)
    print(team.Cheer())
    Player("0 Can't happen")

if __name__ == "__main__":
    main()





    
