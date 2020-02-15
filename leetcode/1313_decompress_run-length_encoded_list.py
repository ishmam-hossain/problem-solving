class Solution:
    def decompressRLElist(self, nums):
        res = []
        for i in range(0, len(nums), 2):
            a, b = nums[i], nums[i+1]
            res.extend([b]*a)

        return res


s = Solution()
print(s.decompressRLElist([1, 2, 3, 4]))
