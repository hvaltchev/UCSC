#!/usr/bin/env python3
"""
lab16_1.py
Write a function that receives a dictionary as an argument,
and returns a tuple of two formatted strings.
"""

def FormatEvent(event_d):
    """Returns three strings for the event:
    one formatted for a calendar,
    one formatted for an invitation,
    one for a banner.
    """
    calendar = "{date}:{theme} {what}".format(**event_d)
    invitation = "Come to a %(theme)s %(what)s on %(date)s!" % event_d
    banner = f'{event_d["theme"]} {event_d["what"]}'.title()
    yield calendar
    yield invitation
    yield banner

def main():
    event_d = {"what": "party", "date": "Oct 31",
               "theme": "Halloween"}
    for each in FormatEvent(event_d):
        print(each)

if __name__ == "__main__":
    main()

