def find_peak_iteratively():
    length = len(arr)
    for i, num in enumerate(arr):
        if i == 0:
            if num >= arr[i+1]:
                print(num, arr[i+1])
        elif i == length - 1:
            if num >= arr[i-1]:
                print(num, arr[i-1])

        if 0 < i < length-1:
            prev = arr[i-1]
            nxt = arr[i+1]
            if prev <= num and num >= nxt:
                print(prev, num, nxt)


if __name__ == '__main__':
    arr = [1, 4, 3, 4, 1, 2, 5, 3, 9, 1]
    find_peak_iteratively()
