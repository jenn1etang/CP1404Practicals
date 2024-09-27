"""
CP1404 - Language program
Estimate time: 30mins
Actual time: 20mins
"""

from prac_06.programming_language import ProgrammingLanguage


def main():
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(python)

    programming_languages = [python, ruby, visual_basic]
    print("The dynamically typed languages are:")
    for language in programming_languages:
        if language.is_dynamic() is True:
            print(language.language)


main()

