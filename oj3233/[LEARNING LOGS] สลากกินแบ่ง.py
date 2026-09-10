"""[LEARNING LOGS] สลากกินแบ่ง"""

def main():
    """[LEARNING LOGS] สลากกินแบ่ง"""

    id_lot1, num_lot1 = map(str,input().split())
    id_lot2, num_lot2 = map(str,input().split())
    money = 0

    if id_lot1 == id_lot2:
        if num_lot1 == num_lot2:
            money = 1000000
        elif num_lot1[2:] == num_lot2[2:]:
            money = 2000
        elif num_lot1[3:] == num_lot2[3:]:
            money = 1000
        else:
            money = 20
    else:
        if num_lot1 == num_lot2:
            money = 100000
        elif num_lot1[2:] == num_lot2[2:]:
            money = 200
        elif num_lot1[3:] == num_lot2[3:]:
            money = 100

    print(money)

main()
