"""[LEARNING LOGS] SurprisingVote"""

def main():
    """[LEARNING LOGS] SurprisingVote"""
    score_all = float(input())
    score_high = float(input())
    score = score_all - (score_high * 2)

    if score_high - score > 2:
        print("Surprising")
    else:
        print("Not surprising")

main()
