class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        """with sort -- O(nlog(n)) time"""
        max_diff = 0

        if len(nums) < 2:
            return max_diff

        nums.sort()

        for i, n in enumerate(nums[:-1]):
            max_diff = max(max_diff, nums[i + 1] - n)

        return max_diff