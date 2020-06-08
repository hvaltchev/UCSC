    weather_d = {"bad": 4, "ok": 7, "good": 10}

	def PredictHarvest(self):
        """Returns a sentence predicting the harvest for the 
		Veggie.
        """
        harvest_index = self.weather_d[self.weather] - self.bug_index
        judgement = "great" if harvest_index > 8 else "ok" if harvest_index > 5 else "disappointing" if harvest_index > 3 else "zilch"
        return f"{self} will be {judgement} this year."
