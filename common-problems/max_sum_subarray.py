def get_max_sum_sub_arr(arr):
    max_sum = cur_sum = arr[0]

    for n in arr[1:]:
        cur_sum = max(cur_sum+n, n)
        max_sum = max(max_sum, cur_sum)

    return max_sum


a = [1, -2, 3, 4, -7, 1]
print(get_max_sum_sub_arr(a))
