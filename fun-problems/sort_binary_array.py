from random import randint


def sort_array(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]

    return arr


a = [randint(10, n) % 2 for n in range(100, 110)]
print(a)
print(sort_array(a))
