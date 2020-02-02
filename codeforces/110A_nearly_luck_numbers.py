def is_lucky(n):
    if not n >= 4:
        return "NO"

    while n >= 4:
        rem = n % 10
        if rem not in luck_digits:
            return "NO"
        n = n // 10

    return "YES"


def find_almost_lucky(n):
    counter = 0
    while n > 0:
        rem = n % 10
        if rem in luck_digits:
            counter += 1
        n = n // 10

    return is_lucky(counter)


if __name__ == '__main__':
    luck_digits = (4, 7)
    x = int(input())
    print(find_almost_lucky(x))
