def find_two_missing_numbers(arr):
    for n in arr:
        arr[abs(n)-1] = -abs(arr[abs(n)-1])
    res = [i+1 for i, n in enumerate(arr) if n > 0]
    return res


a = [1, 1, 2, 2, 4]
print(find_two_missing_numbers(a))
