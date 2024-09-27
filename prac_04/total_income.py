"""
total_income = 0

get number_of_month
for number in range(number_of_month)
    get monthly incomes
    store monthly incomes in list
    get number of month
display income_report
"""

"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    # This variable stores the number of months
    number_of_months = int(input("How many months? "))

    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)

    display_monthly_income_report(incomes, number_of_months)


def display_monthly_income_report(incomes, number_of_months):
    """
    This function will print a report of monthly income.
    :param incomes:
    :param number_of_months:
    :return:
    """
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, number_of_months + 1):
        income = incomes[month - 1]
        total += income
        print(f'Month {month:2} - Income: ${income:10.2f}\t\t\tTotal: ${total:10.2f}')


main()
