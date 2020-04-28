class Solution:
    def canJump(self, nums) -> bool:
        i = reach = 0
        while i < len(nums) and i <= reach:
            reach = max(i + nums[i], reach)
            i += 1
        return i == len(nums)
