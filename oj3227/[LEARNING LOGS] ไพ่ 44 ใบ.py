"""[LEARNING LOGS] ไพ่ 44 ใบ"""

def main():
    """[LEARNING LOGS] ไพ่ 44 ใบ"""

    num = {
        "A" : "ace",
        "J" : "jack",
        "Q" : "queen",
        "K" : "king"
    }

    symbol = {
        "D" : "diamonds",
        "H" : "hearts",
        "S" : "spades",
        "C" : "clubs"
    }

    front = ""
    back = ""

    text = input().upper()

    if len(text) == 3:
        front = text[:2]
        back = text[2]
    elif len(text) == 2:
        front = text[0]
        back = text[1]

    if front.isdigit():
        print(front + " of " + symbol[back])
    else:
        print(num[front] + " of " + symbol[back])

main()
