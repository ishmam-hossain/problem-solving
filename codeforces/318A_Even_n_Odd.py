if __name__ == '__main__':
    n, k = map(int, input().split(" "))

    odd_last_at = ((n // 2) - 1 if n % 2 == 0 else (n // 2)) + 1

    if k <= odd_last_at:
        print((k * 2) - 1)
    else:
        print((k - odd_last_at) * 2)


