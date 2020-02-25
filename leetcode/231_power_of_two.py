from math import log2


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        num = log2(n)
        return int(num) == num


s = Solution()
print(s.isPowerOfTwo(256))
