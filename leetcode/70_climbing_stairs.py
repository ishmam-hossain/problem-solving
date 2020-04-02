from functools import lru_cache


class Solution:
    def best_solution(self, n):
        f = s = 1
        for i in range(2, n + 1, 1):
            f, s = s, f + s

        return s

    def second_best_solution(self, n):
        dp = [-1] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1, 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[-1]

    @lru_cache(maxsize=128)
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2

        return self.climbStairs(n - 1) + self.climbStairs(n - 2)