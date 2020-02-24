class Solution:
    def missingNumber(self, nums) -> int:
        length = len(nums)
        return (length * (length+1)) // 2 - sum(nums)


s = Solution()
print(s.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))
print(s.missingNumber([3, 0, 1]))
