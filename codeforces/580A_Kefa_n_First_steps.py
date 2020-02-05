def max_non_decreasing_sub_segment():
    start = end = 0
    res = 1

    for i in range(len(a) - 1):
        if a[i] <= a[i+1]:
            end += 1
            temp = end - start + 1
            if temp > res:
                res = temp

        else:
            temp = end - start + 1
            if temp > res:
                res = temp
            start = i
            end = i

    return res


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split(" ")))
    print(max_non_decreasing_sub_segment())

