from functools import lru_cache


class Solution:
    def fib_iterative(self, N: int) -> int:
        if N == 0:
            return 0
        first = 0
        second = 1

        while N > 1:
            first, second = second, first + second
            N -= 1

        return second

    @lru_cache(maxsize=30)
    def fib(self, N):
        """with memoization"""
        if N == 0:
            return 0
        if N == 1:
            return 1

        return self.fib(N-1) + self.fib(N-2)


s = Solution()
print(s.fib(4))
