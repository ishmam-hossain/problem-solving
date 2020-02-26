
from random import randint


def sort_array(arr):
    lo = 0
    hi = len(arr) - 1

    while lo < hi:
        if arr[lo] == 0:
            lo += 1
        if arr[hi] == 1:
            hi -= 1

        if arr[lo] > arr[hi]:
            arr[lo], arr[hi] = arr[hi], arr[lo]
            lo += 1
            hi -= 1

    return arr


a = [randint(10, n) % 2 for n in range(100, 130)]
print(a)
print(sort_array(a))
