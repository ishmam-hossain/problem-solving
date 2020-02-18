class Solution:
    def isUgly(self, num: int) -> bool:
        if num <= 0:
            return False
        num = abs(num)
        prime_factor = (2, 3, 5)
        while num >= 2:
            for pf in prime_factor:
                if num % pf == 0:
                    num //= pf
                    break
            else:
                return False
        return True


s = Solution()
print(s.isUgly(6))
