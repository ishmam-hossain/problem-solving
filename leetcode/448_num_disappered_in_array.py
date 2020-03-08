class Solution:
    def findDisappearedNumbers(self, nums):
        if not nums:
            return []
        res = [None] * len(nums)

        for n in nums:
            res[n-1] = n

        return [i+1 for i, n in enumerate(res) if n is None]


s = Solution()
print(s.findDisappearedNumbers([4,3,2,7,8,2,3,1]))
