"""
Get a valid score and display the result and stars.
"""


def main():
    # Display menu
    menu = '(G)et a valid score (must be 0-100 inclusive)\n(P)rint result (copy or import your function to determine ' \
           'the result from score.py)\n(S)how stars (this should print as many stars as the score)\n(Q)uit'
    print(menu)
    choice = str(input(">>> ")).lower()
    score = 0
    while choice != 'q':
        if choice == 'g':
            score = get_valid_score('Score: ', 0, 100)
        elif choice == 'p':
            print(determine_score_result(score))
        elif choice == 's':
            print('*' * score)
        else:
            print("Invalid option.")
        print(menu)
        choice = str(input(">>> ")).lower()
    print("Farewell")


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


def get_valid_score(prompt, minimum_num, maximum_num):
    score = int(input(prompt))
    while score < minimum_num or score > maximum_num:
        print('Invalid score.')
        score = int(input(prompt))
    else:
        return score


main()

