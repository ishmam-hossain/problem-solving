if __name__ == '__main__':
    n = int(input())
    res = 0

    for i in range(n):
        p, q = map(int, input().split(" "))
        if q - p >= 2:
            res += 1

    print(res)
