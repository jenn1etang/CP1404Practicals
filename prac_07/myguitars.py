"""
CP1404 - Guitar class
Estimate time: 1hour
Actual time: 1:15mins
"""


class Guitar:
    """Represent information about a guitar"""

    def __init__(self, name, year, cost):
        """Construct a Guitar from given value"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string presentation of a Guitar"""
        return f"{self.name},{self.year},{self.cost}"

    def __lt__(self, other):
        return self.year < other.year


def using_guitar_from_csv():
    guitars = []
    in_file = open('guitars.csv', 'r')
    in_file.readline()
    for line in in_file:
        parts = line.strip().split(',')
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        guitars.append(guitar)
    # Close the file as soon as we've finished reading it
    in_file.close()
    guitars.sort()
    for guitar in guitars:
        print(guitar)


def using_guitar_from_user():
    # store guitar information into a list
    guitars = []
    is_name_blank = False
    name = str(input("Name: "))
    year = int(input("Year: "))
    cost = float(input("Cost: "))
    while not is_name_blank:
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        name = str(input("Name: "))
        if name == '' or ' ':
            break
        year = int(input("Year: "))
        cost = float(input("Cost: "))
    # write guitar information in guitars.csv
    guitars.sort()
    out_file = open('guitars.csv', 'w')
    for guitar in guitars:
        print(guitar, file = out_file)
    # Close the file as soon as we've finished reading it
    out_file.close()


using_guitar_from_user()
