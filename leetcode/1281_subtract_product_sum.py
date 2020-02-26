class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        _prod = 1
        _sum = 0

        while n:
            digit = n % 10
            n //= 10

            _prod *= digit
            _sum += digit

        return _prod - _sum


s = Solution()
print(s.subtractProductAndSum(4421))
