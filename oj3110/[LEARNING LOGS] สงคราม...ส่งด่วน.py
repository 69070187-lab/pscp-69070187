"""[LEARNING LOGS] สงคราม...ส่งด่วน"""

def main():
    """[LEARNING LOGS] สงคราม...ส่งด่วน"""

    start, end = map(str,input().split())
    weigth = float(input())

    starting_fee = 0
    weigth_fee = 0
    price_all = 0

    if start == "BKK" and end == "CNX":
        starting_fee = 10
        weigth_fee = 30
        price_all = starting_fee + (weigth_fee * weigth)
        print(f"{price_all:.2f}")
    elif start == "CNX" and end == "UBP":
        starting_fee = 15
        weigth_fee = 40
        price_all = starting_fee + (weigth_fee * weigth)
        print(f"{price_all:.2f}")
    elif start == "UBP" and end == "BKK":
        starting_fee = 20
        weigth_fee = 40
        price_all = starting_fee + (weigth_fee * weigth)
        print(f"{price_all:.2f}")
    elif start == "BKK" and end == "PKT":
        starting_fee = 25
        weigth_fee = 50
        price_all = starting_fee + (weigth_fee * weigth)
        print(f"{price_all:.2f}")
    elif start == "PKT" and end == "CNX":
        starting_fee = 30
        weigth_fee = 60
        price_all = starting_fee + (weigth_fee * weigth)
        print(f"{price_all:.2f}")
    elif start == "UBP" and end == "PKT":
        starting_fee = 40
        weigth_fee = 70
        price_all = starting_fee + (weigth_fee * weigth)
        print(f"{price_all:.2f}")
    else:
        print("Error")

main()
