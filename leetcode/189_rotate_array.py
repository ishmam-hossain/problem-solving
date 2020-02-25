def swapper(i, j, arr):
    while i <= j:
        print(i, j)
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    return arr


class Solution:
    def rotate(self, nums, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return nums
        length = len(nums)
        if k >= 8:
            k %= length

        nums = swapper(0, length - 1, nums)
        nums = swapper(0, k - 1, nums)
        nums = swapper(k, length - 1, nums)
        return nums


s = Solution()
print(s.rotate([1, 2, 3, 4, 5, 6, 7], 8))
