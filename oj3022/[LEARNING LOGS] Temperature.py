"""[LEARNING LOGS] Temperature"""

def temp_change(temp, temp_after):
    """change temp"""
    if temp_after == "C":
        pass
    elif temp_after == "K":
        temp = temp + 273.15
    elif temp_after == "F":
        temp = (temp * 9 / 5) + 32
    elif temp_after == "R":
        temp = (temp + 273.15) * 9 / 5

    print(f"{temp:.2f}")

def main():
    """main calculate"""
    temp = float(input())
    temp_before = input()
    temp_after = input()

    if temp_before == "C":
        temp_change(temp, temp_after)
    elif temp_before == "F":
        temp = (temp - 32) * (5 / 9)
        temp_change(temp, temp_after)
    elif temp_before == "K":
        temp = temp - 273.15
        temp_change(temp, temp_after)
    elif temp_before == "R":
        temp = (temp * 5 / 9) - 273.15
        temp_change(temp, temp_after)

main()
