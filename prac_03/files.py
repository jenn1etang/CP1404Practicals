"""
Program on loading contents in file and add up numbers within it.
"""

# 1. get user's name and open a file using the name.
name = str(input("Name: "))
out_file = open(f'{name}.txt', 'w')
print(name, file=out_file)
out_file.close()

# 2. read file and display the name
in_file = open(f'{name}.txt', 'r')
content = in_file.read()
in_file.close()
print(f"Your name is {content}")

# 3. read first two numbers in numbers.txt and display in total.
two_number_total = 0
in_numbers_file = open('numbers.txt', 'r')
for line in range(2):
    number = int(in_numbers_file.readline())
    two_number_total += number
in_numbers_file.close()
print(f"First two number in total: {two_number_total}")

# 4.
numbers_in_total = 0
in_numbers_file = open('numbers.txt', 'r')
for line in in_numbers_file:
    number = int(line.strip('\n'))
    numbers_in_total += number
in_numbers_file.close()
print(f"All numbers in total: {numbers_in_total}")
