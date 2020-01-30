lucky_digits = [4, 7]


def get_lucky(n):
    while n > 0:
        rem = n % 10
        n = n // 10
        yield rem


def find_lucky(_num):
    for i in range(4, _num + 1, 1):
        for x in get_lucky(i):
            if x not in lucky_digits:
                break
        else:
            yield i


if __name__ == '__main__':
    num = int(input())

    for y in find_lucky(num):
        if num % y == 0:
            print("YES")
            break
    else:
        print("NO")

