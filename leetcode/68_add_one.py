from collections import deque


class Solution:
    def plusOne(self, digits):
        carry = 0
        length = len(digits)

        for i, num in enumerate(digits):
            index = length - i - 1
            _sum = digits[index] + carry + (1 if i == 0 else 0)
            carry = _sum // 10
            now_digit = _sum % 10
            digits[index] = now_digit

        return digits if not carry else [carry, *digits]


s = Solution()
print(s.plusOne([1, 2, 9, 7]))
print(s.plusOne([9, 9, 9, 9]))
