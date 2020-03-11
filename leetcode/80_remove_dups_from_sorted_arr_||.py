class Solution:
    def removeDuplicates(self, nums, k):
        j = 0
        for i in range(len(nums)):
            if j < 2 or nums[i] > nums[j-k]:
                nums[j] = nums[i]
                j += 1

        nums[:] = nums[:j]
        print(nums)


s = Solution()
# print(s.removeDuplicates([-1, -1, 0, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4], 2))
print(s.removeDuplicates([1], 2))
