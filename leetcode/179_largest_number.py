from math import log10, floor

class Solution:
    def largestNumber(self, nums):
        largest_num = max(nums)
        largest_num_length = int(log10(largest_num)) + 1

        buckets = [-1]*len(nums)

        return [n // 10 ** floor(int(log10(n))) for n in nums]


s = Solution()
print(s.largestNumber([3, 30, 34, 5, 9, 675]))
