def next_rounders():
    passing_score = scores[k - 1]
    count = 0
    for val in scores:
        if not val >= passing_score:
            return count
        elif val > 0:
            count += 1
    return count


if __name__ == '__main__':
    n, k = map(int, input().strip().split(" "))
    scores = list(map(int, input().strip().split(" ")))
    print(next_rounders())

