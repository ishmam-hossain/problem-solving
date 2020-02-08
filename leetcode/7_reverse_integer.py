from math import log10


class Solution:
    def reverse(self, x: int) -> int:
        if x == 0 or not (-2) ** 31 <= x <= (2 ** 31) - 1:
            return 0

        is_negative = False

        if x < 0:
            is_negative = True
            x = x * -1

        l = int(log10(x))
        res = 0
        while x:
            rem = x % 10
            x = x // 10
            res += rem * 10 ** l
            l -= 1

        if not (-2) ** 31 <= res <= (2 ** 31) - 1:
            return 0
        return res if not is_negative else res * -1


s = Solution()
print(s.reverse(1534236469))
