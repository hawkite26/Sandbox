def main():
    scores = []
    score = int(input("Score: "))
    while score >= 0:
        scores.append(score)
        score = int(input("Score: "))
    if len(scores) == 0:
        print("You have no scores")
    else:
        print("Your highest score is {}".format(max(scores)))


main()
