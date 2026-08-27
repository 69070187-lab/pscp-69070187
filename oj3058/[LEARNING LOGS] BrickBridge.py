"""[LEARNING LOGS] BrickBridge"""

def main():
    """[LEARNING LOGS] BrickBridge"""

    small = int(input())
    big = int(input())
    goal = int(input())

    big = min(big,goal // 5)
    remaining = goal - big * 5

    if remaining <= small:
        print(remaining)
    else:
        print(-1)

main()
