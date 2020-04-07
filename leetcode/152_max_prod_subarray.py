class Solution:
    def maxProduct(self, nums) -> int:
        maximum = big = small = nums[0]
        for n in nums[1:]:
            big, small = max(n, n * big, n * small), min(n, n * big, n * small)
            maximum = max(maximum, big)
        return maximum


s = Solution()
print(s.maxProduct([2, 3, -2, 4]))
