"""[LEARNING LOGS] หาร 10"""

def main():
    """เลขหาร 10 ลงตัว"""
    num = int(input())
    i = 0
    result = []

    for i in range(num + 1):
        if not i % 10:
            result.append(i)

    result.sort(reverse = True)
    result = [str(i) for i in result]
    result = " ".join(result)
    print(result)

main()
