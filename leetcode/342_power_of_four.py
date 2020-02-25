from math import log


class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num <= 0:
            return False

        res = log(num, 4)
        return int(res) == res


s = Solution()
print(s.isPowerOfFour(5))
