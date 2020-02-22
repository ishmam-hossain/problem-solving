import random


def count_sort(arr):
    max_num = max(arr)
    counter = [0]*(max_num+1)

    for i in arr:
        counter[i] += 1

    res = [[i]*n for i, n in enumerate(counter)]
    return [y for x in res for y in x]


if __name__ == '__main__':
    a = [random.randint(1, 100) for _ in range(100)]
    print(count_sort(a))
