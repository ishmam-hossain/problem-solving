class Solution:
    def findDuplicate(self, nums) -> int:
        for n in nums:
            if nums[abs(n)-1] < 0:
                return abs(n)
            else:
                nums[abs(n)-1] = -nums[abs(n)-1]

    def another_solution_but_not_for_this_one(self, nums):
        arr_sum = sum(nums)
        length = len(nums) - 1
        tot_sum = (length * (length + 1)) // 2
        return arr_sum - tot_sum


s = Solution()
print(s.findDuplicate([1, 3, 4, 2, 2]))
