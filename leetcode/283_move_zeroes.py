class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """This is the most optimized one"""
        zero_at = num_at = 0

        while zero_at < len(nums) and num_at < len(nums):
            if nums[zero_at] != 0:
                zero_at += 1
            if nums[num_at] == 0:
                num_at += 1
            if num_at < zero_at:
                num_at += 1
                continue

            if zero_at < len(nums) and num_at < len(nums) and nums[zero_at] == 0 and nums[num_at] != 0:
                nums[zero_at], nums[num_at] = nums[num_at], nums[zero_at]
                zero_at += 1
                num_at += 1


class SolutionBad:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums[:-1])):
            for j, n in enumerate(nums[:-1]):
                if n == 0:
                    nums[j], nums[j+1] = nums[j+1], nums[j]

    def move_zeroes_not_efficient(self, nums) -> None:
        count = 0
        for i, n in enumerate(nums):
            if n == 0:
                nums.remove(nums[i])
                nums.append(0)
                count += 1


"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""