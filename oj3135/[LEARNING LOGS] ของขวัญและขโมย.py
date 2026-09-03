"""[LEARNING LOGS] ของขวัญและขโมย"""

def main():
    """[LEARNING LOGS] ของขวัญและขโมย"""

    person, add, bandit = map(int, input().split())

    if bandit == 1:
        print(1)
        return

    location = 1 + add
    count = 1


    while True:
        if location == bandit:
            count += 1
            break
        if location == 1:
            break

        count += 1
        location += add
        if location > person:
            location -= person

    print(count)

main()
