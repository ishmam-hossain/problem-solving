from math import log10
from itertools import combinations


def is_lucky(n):
    count = {}
    if not n >= 4:
        return False, {}

    while n >= 1:
        rem = n % 10
        if rem not in lucky_digits:
            return False, {}
        count[rem] = count.get(rem, 0) + 1
        n = n // 10

    return True, count


def is_super_lucky(n):
    while True:
        lucky, count = is_lucky(n)
        if lucky:
            if 4 in count and 7 in count:
                if count[4] == count[7]:
                    return n
        n += 1


def get_all_combo(n):
    no_of_digits = int(log10(n)) + 1

    for i in combinations(sorted(lucky_digits * no_of_digits), no_of_digits):
        yield i


def get_count(n):
    count = {}
    for i in n:
        count[i] = count.get(i, 0) + 1

    return count


def get_num_from_digit(n):
    digits = len(n)
    _sum = 0
    for i in range(digits):
        _sum += n[i] * 10 ** i

    return _sum


def new_super_lucky(n):
    lucky_digits = (4, 7)
    no_of_digits = int(log10(n)) + 1

    for i in combinations(sorted(lucky_digits * no_of_digits), no_of_digits):
        _i = get_num_from_digit(i)
        print(_i)
        if _i > n:
            count = get_count(i)

            if 4 in count and 7 in count:
                if count[4] == count[7]:
                    return _i


if __name__ == '__main__':
    x = int(input())
    print(new_super_lucky(x))
