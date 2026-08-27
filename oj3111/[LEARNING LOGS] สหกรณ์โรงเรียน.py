"""[LEARNING LOGS] สหกรณ์โรงเรียน"""
from decimal import Decimal, ROUND_HALF_UP


def main():
    """[LEARNING LOGS] สหกรณ์โรงเรียน"""

    status = input()
    num = int(input())
    price_all = Decimal("0")

    for _ in range(num):
        price_all += Decimal(input())

    if status == "Y":
        price_all *= Decimal("0.95")
    elif status == "N" and price_all >= Decimal("500"):
        price_all *= Decimal("0.97")

    price_all = price_all.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

    print(f"{price_all:.2f}")

main()
