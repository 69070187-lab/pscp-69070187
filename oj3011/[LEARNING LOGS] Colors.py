"""color"""

def main():
    """mix color"""
    color_1 = input()
    color_2 = input()

    if color_1 == color_2 == "Red":
        print("Red")
    elif color_1 == color_2 == "Yellow":
        print("Yellow")
    elif color_1 == color_2 == "Blue":
        print("Blue")
    elif color_1 == "Red" or color_2 == "Red":
        if color_1 == "Yellow" or color_2 == "Yellow":
            print("Orange")
        elif color_1 == "Blue" or color_2 == "Blue":
            print("Violet")
        else:
            print("Error")
    elif color_1 == "Yellow" or color_2 == "Yellow":
        if color_1 == "Blue" or color_2 == "Blue":
            print("Green")
        else:
            print("Error")
    else:
        print("Error")

main()
