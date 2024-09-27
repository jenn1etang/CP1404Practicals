"""
pseudocode:
get name
display menu
get choice
while choice != Q
   if choice == H
       display "hello" name
   else if choice == G
       display "goodbye" name
   else
       display invalid message
   display menu
   get choice
display finished message
"""

name = str(input("Enter name: ")).capitalize()
menu_option = '(H)ello\n(G)oodbye\n(Q)uit'
print(menu_option)
choice = str(input(">>> ")).upper()

while choice != 'Q':
    if choice == 'H':
        print("Hello", name)
    elif choice == 'G':
        print("Goodbye", name)
    else:
        print("Invalid choice")
    print(menu_option)
    choice = str(input(">>> ")).upper()
print("Finished.")

