def rotate_array(arr, rotate_by):
    res = [None]*len(arr)
    for i, n in enumerate(arr):
        res[(i + (len(arr) % rotate_by)) % len(arr)] = arr[i]
    return res


if __name__ == '__main__':
    print(rotate_array([1, 2, 3, 4, 5], 3))
