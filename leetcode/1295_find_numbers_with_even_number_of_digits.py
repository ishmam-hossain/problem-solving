from math import log10


class Solution:
    def findNumbers(self, nums) -> int:
        total_even_digit_nums = 0
        for n in nums:
            if (int(log10(n)) + 1) % 2 == 0:
                total_even_digit_nums += 1

        return total_even_digit_nums


s = Solution()
print(s.findNumbers([1, 45, 6, 5454, 8788]))
