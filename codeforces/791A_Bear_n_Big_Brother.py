def weight_time(a, b):
    year = 1
    while a <= b:
        a *= 3
        b *= 2
        if a > b:
            break
        year += 1

    return year


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(weight_time(a, b))
