#!/usr/bin/env python3
"""
lab19_2.py (Optional) A Veggie class hierarchy, with a class
method and a staticmethod.
"""

class Veggie:
    """Instantiate: in subclass.
    """

    weather = "good"
    weather_d = {"bad": 4, "ok": 7, "good": 10}

    def PredictHarvest(self):
        """Returns a sentence predicting the harvest for the 
		Veggie.
        """
        harvest_index = self.weather_d[self.weather] - self.bug_index
        judgement = ("great" if harvest_index > 8
                     else "ok" if harvest_index > 5
                     else "disappointing" if harvest_index > 3
                     else "zilch")
        return f"{self} will be {judgement} this year."

    @classmethod
    def UpdateBugIndex(cls, bug_index):
        """Changes the bug_index in the appropriate class.
        """
        if cls == Veggie:
            raise ValueError(
                "UpdateBugIndex must called from a subclass.")
        cls.bug_index = bug_index

    @staticmethod
    def UpdateWeather(weather):
        """Changes the weather in this class.
        """
        if weather not in Veggie.weather_d:
            raise ValueError("weather must be "
                             f"{' or '.join(Veggie.weather_d.keys())}")
        Veggie.weather = weather

    def __str__(self):
        return self.__class__.__name__

class Asparagus(Veggie):
    bug_index = 2

class Corn(Veggie):
    bug_index = 1

class Squash(Veggie):
    bug_index = 3

def main():
    Veggie.UpdateWeather("good")
    veggies = (Asparagus(), Corn(), Squash())
    for veggie in veggies:
        print(veggie.PredictHarvest())
    asparagus, corn, squash = veggies
    print("No bugs for asparagus.")
    Asparagus.UpdateBugIndex(0)
    for veggie in veggies:
        print(veggie.PredictHarvest())
    print('Weather degraded to "ok".')
    Veggie.UpdateWeather("ok")
    for veggie in veggies:
        print(veggie.PredictHarvest())
    try:
        Veggie.UpdateWeather("hot")
    except ValueError as msg:
        print(msg)
    else:
        print("Unexpected behavior.")
    try:
        Veggie.UpdateBugIndex(7)
    except ValueError as msg:
        print(msg)
    else:
        print("Unexpected behavior.")

if __name__ == "__main__":
    main()

