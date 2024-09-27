"""
CP1404/CP5632 - Practical
Determines score status
"""


from random import randint


def main():
    score = float(input("Enter score: "))
    result = determine_score_result(score)
    print(result)

    random_score = randint(1, 100)
    print('\nRandom score:', random_score)
    result = determine_score_result(random_score)
    print(result, end=' ')


def determine_score_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    else:
        if score >= 90:
            return "Excellent"
        elif score >= 50:
            return "Passable"
        if score < 50:
            return "Bad"


main()
