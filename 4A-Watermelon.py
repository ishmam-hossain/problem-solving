def is_divisible(w):
    return "YES" if w > 2 and w % 2 == 0 else "NO"


if __name__ == '__main__':
    print(is_divisible(int(input())))

