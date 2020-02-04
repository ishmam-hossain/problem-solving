def bin_search_find_occurrence(arr, x, low, hi, is_first=False):
    res = -1

    while low <= hi:
        mid = (low + hi) // 2
        if arr[mid] == x:
            res = mid
            if is_first:
                hi = mid - 1
            else:
                low = mid + 1

        elif x > arr[mid]:
            low = mid + 1
        else:
            hi = mid - 1

        bin_search_find_occurrence(arr, x, low, hi)

    return res


if __name__ == '__main__':
    a = [1, 2, 2, 2, 3, 4, 4, 5, 5, 7, 9, 16]
    n = 9

    first_occurrence = bin_search_find_occurrence(a, n, 0, len(a)-1, True)
    if first_occurrence >= 0:
        last_occurrence = bin_search_find_occurrence(a, n, 0, len(a)-1)
        print("Total appearance -->\t", last_occurrence - first_occurrence + 1)
    else:
        print("Not found!")


