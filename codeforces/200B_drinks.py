if __name__ == '__main__':
    n = int(input())
    drinks = map(int, input().split(" "))

    ratio = (100 / n) / 100
    final_ratio = sum([drink * ratio for drink in drinks])

    print(final_ratio)

