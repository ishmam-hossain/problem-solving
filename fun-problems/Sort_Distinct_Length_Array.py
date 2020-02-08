from math import log10


def sort_it(arr):
    result_arr = [-1]*len(arr)
    i = 0
    while i < len(arr):
        index = int(log10(arr[i]))
        result_arr[index] = arr[i]
        i += 1

    print(result_arr)


def sort_it_in_place(arr):
    i = 0
    temp = arr[i]
    while i < len(arr):
        index = int(log10(temp))
        if i == index:
            i += 1
            temp = arr[i]
            continue

        print("INDEX: ", index)
        nxt = arr[index]
        arr[index] = temp
        temp = nxt
        i += 1

        print("temp: ", temp, "next: ", nxt)
        print(arr)

    print("******")
    print(arr)


if __name__ == '__main__':
    # a = [131, 59921, 27, 820273, 6, 1036]
    a = [13, 552352, 271, 62674, 1036, 1]
    # sort_it(a)
    sort_it_in_place(a)

