class Solution:
    def maximum69Number(self, num: int) -> int:
        digits = []
        n = num
        while n:
            digits.append(n % 10)
            n //= 10

        for i in range(len(digits)):
            if digits[len(digits) - i - 1] == 6:
                digits[len(digits) - i - 1] = 9
                break

        res = i = 0
        for x in digits:
            res += x * 10 ** i
            i += 1
        return res


s = Solution()
print(s.maximum69Number(9966966))
