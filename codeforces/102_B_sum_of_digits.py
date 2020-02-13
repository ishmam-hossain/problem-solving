from math import log10


def cast_spell(cur, count):
    if not int(log10(cur)) + 1 > 1:
        return count
    _sum = 0
    while cur:
        _sum += cur % 10
        cur = cur // 10

    return cast_spell(_sum, count+1)


def manual_cast_spell(num):
    count = 0
    while int(log10(num)) + 1 > 1:
        count += 1
        _sum = 0

        while num:
            _sum += num % 10
            num = num // 10
        num = _sum

    return count


if __name__ == '__main__':
    n = int(input())
    if n > 0:
        print(manual_cast_spell(n))
    else:
        print('0')


"""
def manual_cast_spell(num):
    count = 0
    while int(log10(num)) + 1 > 1:
        count += 1
        _sum = 0

        while num:
            _sum += num % 10
            num = num // 10
        num = _sum

    return count


if __name__ == '__main__':
    n = int(input())
    if n > 0:
        print(manual_cast_spell(n))
    else:
        print('0')


"""