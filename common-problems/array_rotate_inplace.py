def swapper(i, j, arr):
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    return arr


def rotate_right_inplace(arr, k):
    length = len(arr)
    arr = swapper(0, length - 1, arr)
    arr = swapper(0, k - 1, arr)
    arr = swapper(k, length - 1, arr)
    return arr


print(rotate_right_inplace([1, 2, 3, 4, 5], 4))
