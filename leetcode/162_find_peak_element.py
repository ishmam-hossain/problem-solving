class Solution:
    def findPeakElement(self, nums) -> int:
        for i, n in enumerate(nums):
            if i != 0 and i != len(nums) - 1 and nums[i-1] < n > nums[i+1]:
                return i
        return 0 if nums[0] > nums[-1] else len(nums) - 1
