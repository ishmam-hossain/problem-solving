if __name__ == '__main__':
    n, k = map(int, input().split(" "))

    for _ in range(k):
        rem = n % 10
        if rem == 0:
            n = n // 10
        else:
            n -= 1
    print(n)
