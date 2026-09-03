"""[LEARNING LOGS] เกมสะสมแต้ม"""

def main():
    """[LEARNING LOGS] เกมสะสมแต้ม"""

    num = int(input())
    score = 0

    for _ in range(num):
        command = input()

        if command == "+":
            score += 10
        elif command == "-":
            score -= 5

    print(score)

main()
