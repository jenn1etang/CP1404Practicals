for i in range(1, 21, 2):
    print(i, end=' ')
print()

# a. count in 10s from 0 to 100
for count in range(0, 101, 10):
    print(count, end=' ')
print()

# b. count down from 20 to 1
for count in range(20, 0, -1):
    print(count, end=' ')
print()

# c. print n stars
stars_in_line = int(input("Number of stars: "))
for count in range(stars_in_line):
    print("*", end='')
print()

# d. print n lines of increasing stars
number_of_stars = int(input("Number of stars: "))
for count in range(1, number_of_stars + 1):
    print(count * "*", sep=' ')
print()

