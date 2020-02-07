def sort_and_find():
    x = sorted(f)
    diff = 0
    for i in range(1, n):
        diff += x[i] - x[i-1]
    print(diff)


def optimized_version():
    a = [-1]*n
    print(a)


if __name__ == '__main__':
    n, m = map(int, input().split(" "))
    f = list(map(int, input().split(" ")))

    optimized_version()

