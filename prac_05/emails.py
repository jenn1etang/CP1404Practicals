"""
Email
Estimate: 30minutes
Actual:   27minutes
"""


def main():
    user_data = {}
    user_email = str(input("Email: "))

    while user_email != "":
        name = extract_name(user_email)
        is_name = str(input(f"Is your name {name}? (Y/n) ")).upper()
        name = get_correct_name(is_name, name)
        user_data[name] = user_email
        user_email = str(input("Email: "))

    print()
    for name, user_email in user_data.items():
        print(f"{name} ({user_email})")


def get_correct_name(is_name, name):
    if is_name != 'Y' and is_name != "":
        name = str(input("Name: "))
    return name


def extract_name(user_email):
    name = user_email.split("@")[0]
    name = name.split(".")
    name = [word.title() for word in name]
    name = " ".join(name)
    return name


main()
