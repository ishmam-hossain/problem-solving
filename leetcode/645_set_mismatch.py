class Solution:
    def findErrorNums(self, nums):
        seen = set()
        _sum = 0
        dup = None
        for n in nums:
            if n in seen:
                dup = n
            else:
                seen.add(n)
                _sum += n

        length = len(nums)
        missing = (length * (length + 1) // 2) - _sum

        return [dup, missing]


s = Solution()
print(s.findErrorNums([1, 2, 2, 4]))
