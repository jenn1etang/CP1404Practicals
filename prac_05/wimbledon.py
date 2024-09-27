"""
Count Champion won time and display the countries
Estimate: 40 minutes
Actual:   64 minutes
"""

FILENAME = 'wimbledon.csv'


def main():
    champion_won_count = {}
    won_countries = []
    print("Wimbledon Champions: ")
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            line = line.split(',')
            champion = line[2]
            country = line[1]
            if champion in champion_won_count:
                champion_won_count[champion] += 1
            else:
                champion_won_count[champion] = 1

            if country not in won_countries:
                won_countries.append(country)

        for champion, count in champion_won_count.items():
            print(champion, count)

    print("\nThese 12 countries have won Wimbledon: ")
    won_countries = ', '.join(sorted(won_countries))
    print(won_countries)


main()
