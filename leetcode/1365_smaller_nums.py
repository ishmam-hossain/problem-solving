class Solution:
    def smallerNumbersThanCurrent(self, nums):
        """O(n**2) solution"""
        res = []
        for i, n in enumerate(nums):
            count = 0
            for j, n in enumerate(nums):
                if i != j and nums[i] > nums[j]:
                    count += 1
            res.append(count)

        return res
