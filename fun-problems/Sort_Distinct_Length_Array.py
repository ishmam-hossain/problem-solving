from math import log10


def sort_it(arr):
    result_arr = [-1]*len(arr)
    i = 0
    while i < len(arr):
        index = int(log10(arr[i]))
        result_arr[index] = arr[i]
        i += 1

    print(result_arr)


if __name__ == '__main__':
    a = [6, 131, 59921, 27, 820273, 1036]
    sort_it(a)

