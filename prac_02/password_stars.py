"""
To enter appropriate password and display in stars.
"""


# imports
# CONSTANTS

def main():
    password_minimum_character = 10
    password = get_password(password_minimum_character)
    print("\nYou have create a password.", sep=' ')
    display_asterisks(password)


def display_asterisks(password):
    print(password * '*')


def get_password(password_minimum_character):
    password = password_length_check("Enter password: ", password_minimum_character)
    return password


def password_length_check(prompt, minimum_length):
    """Gets the password and check with minimum_length and returns length of password"""
    password = str(input(prompt))
    while len(password) < minimum_length:
        print("Invalid password.")
        password = str(input(prompt))
    return len(password)


main()

