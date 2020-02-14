if __name__ == '__main__':
    k = int(input())
    l = int(input())
    m = int(input())
    n = int(input())
    d = int(input())
    lst = [k, l, m, n]

    count = d

    for i in range(1, d+1):
        if k % i != 0 and l % i != 0 and m % i != 0 and n % i != 0:
            count -= 1

    print(count)
