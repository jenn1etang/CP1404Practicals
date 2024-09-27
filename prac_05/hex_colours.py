"""
Get colour name to display colour code
"""

COLOUR_NAME_TO_CODE = {"acidgreen": "#b0bf1a", "amber": "#ffbf00", "apricot": "#fbceb1", "aqua": "#00ffff",
                       "ashgrey": "#b2beb5", "beige": "#f5f5dc", "black": "#000000", "gray": "#bebebe",
                       "indigo": "#4b0082", "maroon": "#b03060"}


def main():
    colour_name = str(input("Enter colour name: ")).lower()

    while colour_name != "":
        try:
            print(colour_name, "is", COLOUR_NAME_TO_CODE[colour_name])
        except KeyError:
            print("Invalid colour name")
        colour_name = input("Enter colour name: ").lower()


main()
