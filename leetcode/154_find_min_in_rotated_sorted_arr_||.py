class Solution:
    def findMin(self, nums) -> int:
        val = nums[0]
        for n in nums:
            val = min(val, n)

        return val
