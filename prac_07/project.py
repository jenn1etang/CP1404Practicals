"""
CP1404-class project
Estimate time: 1hour
Actual time: 9 houre
"""
import datetime


class Project:
    """Represent information about a project"""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Construct a Project from given value"""
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Return string presentation of a project"""
        return f"{self.name},{self.start_date},{self.priority},{self.cost_estimate},{self.completion_percentage}"

    def __getitem__(self, key):
        if key == 'priority':
            return self.priority
        elif key == 'start_date':
            return self.start_date

    def is_complete(self):
        if self.completion_percentage == 100:
            return True
        else:
            return False
