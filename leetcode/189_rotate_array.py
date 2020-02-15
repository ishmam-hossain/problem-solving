def rotate_array(nums, k):
    # ln = len(arr)
    # for i in range(k):
    #     arr[i], arr[(i + 1 + (ln % k)) % ln] = arr[(i + 1 + (ln % k)) % ln], arr[i]
    #
    # return arr
    nums[:k], nums[k:] = nums[len(nums) - k:], nums[:len(nums) - k]

    return nums


if __name__ == '__main__':
    print(rotate_array([1, 2, 3, 4, 5, 6, 7], 2))
