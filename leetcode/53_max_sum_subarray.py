class Solution:
    def maxSubArray(self, nums) -> int:
        cur_sum = 0
        max_sum = -9999999999999

        for n in nums:
            cur_sum += n
            max_sum = max(cur_sum, max_sum)
            print(cur_sum, max_sum)
            if cur_sum < max_sum:
                cur_sum = 0

        return max_sum


s = Solution()
print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
