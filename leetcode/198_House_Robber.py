class Solution:
    def rob(self, nums):
        odd_sum = 0
        even_sum = 0

        for i, n in enumerate(nums):
            if i % 2 == 0:
                even_sum += n
            else:
                odd_sum += n

        return max(odd_sum, even_sum)


s = Solution()
print(s.rob([1, 2, 3, 5, 7]))
