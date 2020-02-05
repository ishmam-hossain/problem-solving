def is_duplicate(y):
    digits = set()
    while y:
        digits.add(y % 10)
        y = y // 10

    return True if len(digits) == 4 else False


def find_next_beautiful_year(y):
    while True:
        if is_duplicate(y):
            return y
        y += 1


if __name__ == '__main__':
    year = int(input())
    print(find_next_beautiful_year(year + 1))
