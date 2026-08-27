"""[LEARNING LOGS] จำนวนในช่วง [A,B] ที่หารด้วย d เหลือเศษ r"""

def main():
    """[LEARNING LOGS] จำนวนในช่วง [A,B] ที่หารด้วย d เหลือเศษ r"""

    range_a = int(input())
    range_b = int(input())
    divisor = int(input())
    fraction = int(input())
    count = 0

    for i in range(range_a , range_b + 1):
        if i % divisor == fraction:
            count += 1

    print(count)

main()
