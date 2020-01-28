def helpful_math():
    return "+".join(sorted(s))


if __name__ == '__main__':
    s = list(input().split("+"))
    print(helpful_math())
