class Solution:
    def countPrimes(self, n: int) -> int:
        """ Sieve of Eratosthenes Algorithm """
        if n <= 2:
            return 0

        nums = [False, False, True]  # 0, 1, 2 resolved
        nums.extend([True for _ in range(n - 3)])

        cur = 2
        while cur * cur <= n:
            for i, x in enumerate(nums[3:]):
                if (i + 3) > cur and (i + 3) % cur == 0:
                    nums[i + 3] = False
            cur += 1

        return nums.count(True)