"""
CP1404 - Guitar class
Estimate time: 20mins
Actual time:20mins
"""


class Guitar:
    def __init__(self, name="", _year=0, _cost=0):
        self. name = name
        self.year = _year
        self.cost = _cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost}"

    def get_age(self, current_year=2022):
        return current_year-self.year

    def is_vintage(self):
        if self.get_age() >= 50:
            return True
        else:
            return False
