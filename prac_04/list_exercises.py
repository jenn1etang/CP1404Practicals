"""
Determines data in list
"""

numbers = []
describe_data = ['first', 'last', 'smallest', 'largest', 'average of the']
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

for i in range(5):
    number = int(input("Number: "))
    numbers.append(number)

for count in range(0, len(describe_data)):
    print(f"The {describe_data[count]} number is", end=' ')
    if count == 0:
        print(numbers[0])
    elif count == 1:
        print(numbers[-1])
    elif count == 2:
        print(min(numbers))
    elif count == 3:
        print(max(numbers))
    elif count == 4:
        print(sum(numbers)/len(numbers))

print()

username = str(input("Enter username: "))
if username in usernames:
    print("Access granted")
else:
    print("Access denied")
