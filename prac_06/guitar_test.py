"""
CP1404 - test Guitar class using programs
Estimate time: 20mins
Acutal time: 23mins
"""

from prac_06.guitar import Guitar

name = "Gibson L-5 CES"
year = 1922
cost = 16035.40
print(f"My guitar: {name}, first made in {year}")
print()

first_guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
second_guitar = Guitar("Another Guitar", 2013, 16035.40)

print(f"{first_guitar.name} get_age() - Expected 100. Got {first_guitar.get_age()}")
print(f"{second_guitar.name} get_age() - Expected 9. Got {second_guitar.get_age()}")
print(f"{first_guitar.name} is_vintage() - Expected True. Got {first_guitar.is_vintage()}")
print(f"{second_guitar.name} is_vintage() - Expected False. Got {second_guitar.is_vintage()}")

