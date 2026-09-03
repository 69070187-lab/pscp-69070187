"""[LEARNING LOGS] หาจำนวนเฉพาะ"""

def main():
    """[LEARNING LOGS] หาจำนวนเฉพาะ"""

    start, stop = map(int,input().split())
    count = 0
    primes = []

    if start <= stop:
        for i in range(start,stop + 1):
            if i < 2:
                continue

            for j in range(1, i + 1):
                if not i % j:
                    count += 1

            if count == 2:
                primes.append(i)

            count = 0
        if primes:
            print(*primes)

        print(f"Total primes: {len(primes)}")
    else:
        print("ERROR")
main()
