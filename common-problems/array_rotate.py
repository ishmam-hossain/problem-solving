def rotate_array(arr, rotate_by):
    # I have no idea what I did here :3
    res = [None] * len(arr)
    for i, n in enumerate(arr):
        res[(i + (len(arr) % rotate_by)) % len(arr)] = arr[i]
    return res


def right_rotate(arr, k):
    # This one is done
    ln = len(arr)
    res = [None]*ln

    for i, n in enumerate(arr):
        res[(i+k) % ln] = arr[i]
    return res


def right_rotate_in_place(arr, k):
    # in-place pore korbo :3
    ln = len(arr)

    for i, n in enumerate(arr):
        temp = arr[(i + k) % ln]
        arr[(i + k) % ln] = arr[i]
    return arr


if __name__ == '__main__':
    # print(rotate_array([1, 2, 3, 4, 5, 6, 7], 3))
    print([1, 2, 3, 4, 5, 6, 7])
    print("-----------------")
    print(right_rotate([1, 2, 3, 4, 5, 6, 7], 2))
    print("-----------------")
    print(right_rotate_in_place([1, 2, 3, 4, 5, 6, 7], 2))
