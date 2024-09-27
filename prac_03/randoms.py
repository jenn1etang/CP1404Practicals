"""
Comments for each line tests on console.

import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3
"""

# line 1
# for line 1, the largest number is 20 and the smallest is 5.

# line 2
# for line 2, the largest number is 9 and te smallest is 3.
# line 2 could not produce a 4, because it produces a range by step of 2 before a random item is selected.
# With a start number of 3, the next number is 5.

# line 3
# for line 3, the largest number I get is 5.362455591037363. However, the largest number should be 5.5 and
# the smallest number should be 2.5 according to the code.
# Because this randomly select a number including decimals, this requires to test a lot to get the largest
# and the smallest number.

# print a random number from 1 to 100 and inclusive
import random
print(random.randint(1, 100))
