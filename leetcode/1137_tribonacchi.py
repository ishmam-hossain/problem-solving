from functools import lru_cache


class Solution:
    @lru_cache(maxsize=50)
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1

        return self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)

    def iterative_tribonacci(self, n):
        f, s, t = 0, 1, 1
        if n == 0:
            return f

        while n > 2:
            f, s, t = s, t, f + s + t
            n -= 1

        return t


_s = Solution()
for i in range(38):
    print(_s.tribonacci(i) == _s.iterative_tribonacci(i))
    print()
