#!/usr/bin/env python3
"""lab20_2.py (Optional)  -- deals card hands:
lab20_2.py  -- deals 4 hands of 5 cards
lab20_2.py -p 6 -c 3  -- deals 6 hands of 3 cards
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.split(__file__)[0], '..'))
import Lab19_Extending_Builtins.lab19_3 as game_dealer

def main():
    import optparse
    parser = optparse.OptionParser(
        "%prog [-p number_of_players=4] [-c number_of_cards=5]")
    parser.add_option("-p", "--players", dest="no_players", 
                      help="number of players", default=4)
    parser.add_option("-c", "--cards", dest="no_cards", 
                      help="number of cards per hand",
                      default=5)
    (options, args) = parser.parse_args()
    if len(args) > 0:
        parser.error(f"I don't recognize {' '.join(args)}")
    print(game_dealer.GameDealer(options.no_players,
                                 options.no_cards))

if __name__ == "__main__":
    main()