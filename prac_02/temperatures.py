"""
To converts Celsius to Fahrenheit and vice versa.
"""


def main():
    option = '(C)elsius to Fahrenheit\n(F)ahrenheit to Celsius\n(Q)uit'
    print(option)
    choice = str(input(">>> ")).lower()
    while choice != 'q':
        if choice == 'f':
            celsius = fahrenheit_to_celsius('Fahrenheit: ')
            print(f"{celsius:.2f}")
        elif choice == 'c':
            fahrenheit = celsius_to_fahrenheit('Celsius: ')
            print(f"{fahrenheit:.2f}")
        else:
            print("Invalid option.")
        choice = str(input(">>> ")).lower()


def fahrenheit_to_celsius(prompt):
    fahrenheit = float(input(prompt))
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius


def celsius_to_fahrenheit(prompt):
    celsius = float(input(prompt))
    fahrenheit = celsius / 5 * 9 + 32
    return fahrenheit


main()
