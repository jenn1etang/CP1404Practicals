"""
CP1404 - programming language class
"""


class ProgrammingLanguage:

    def __init__(self, language, typing, reflection, _year):
        self.language = language
        self.typing = typing
        self.reflection = reflection
        self._year = _year

    def is_dynamic(self):
        if self.typing == 'Dynamic':
            return True
        else:
            return False

    def __str__(self):
        return f"{self.language}, {self.typing} Typing, Reflection={self.is_dynamic()}, First appeared in {self._year}"

