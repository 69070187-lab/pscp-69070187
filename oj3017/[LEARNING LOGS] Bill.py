"""Calculator"""

def main():
    """cal"""
    price = int(input())

    service = price * (0.1)

    if service < 50 :
        service = 50
    elif service > 1000:
        service = 1000

    price_vat = (price + service) * (0.07)
    price_all = price + service + price_vat

    print(f"{price_all:.2f}")

main()
