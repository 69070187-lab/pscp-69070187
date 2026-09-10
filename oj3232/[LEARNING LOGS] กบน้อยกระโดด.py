"""[LEARNING LOGS] กบน้อยกระโดด"""

def main():
    """[LEARNING LOGS] กบน้อยกระโดด"""
    long_x, long_y = map(int,input().split())
    long_total = 0
    count = 0

    while long_x >= 0:
        long_total += long_x
        count += 1

        if long_total >= long_y:
            print(count)
            return

        long_x -= 2

    print(-1)

main()
