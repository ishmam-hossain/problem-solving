class Solution:
    def singleNonDuplicate(self, nums) -> int:
        res = 0
        for n in nums:
            res ^= n
        return res

