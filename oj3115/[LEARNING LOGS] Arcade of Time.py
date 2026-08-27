"""[LEARNING LOGS] Arcade of Time: Store Check"""

def main():
    """[LEARNING LOGS] Arcade of Time: Store Check"""

    num, check = map(int,(input()).split())
    start = 0
    stop = 0
    start_list = []
    stop_list = []
    check_input = []
    result = []

    for _ in range(num):
        start, stop = map(int, input().split())
        start_list.append(start)
        stop_list.append(stop)

    check_input = list(map(int, input().split()))

    for i in range(check):
        count = 0
        for j in range(num):
            if start_list[j] <= check_input[i] < stop_list[j]:
                count += 1

        result.append(count)

    print(*result)

main()
