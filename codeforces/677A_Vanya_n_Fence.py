if __name__ == '__main__':
    n, h = map(int, input().split(" "))
    a = map(int, input().split(" "))

    width = 0
    for x in a:
        width += 2 if x > h else 1

    print(width)

