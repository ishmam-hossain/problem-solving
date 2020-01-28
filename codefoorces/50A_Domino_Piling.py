if __name__ == '__main__':
    n, m = map(int, input().split(" "))

    area = n * m
    domino_area = 2 * 1

    print(area // domino_area)
