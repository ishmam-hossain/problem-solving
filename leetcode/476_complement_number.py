class Solution:
    def findComplement(self, num: int) -> int:
        if num == 0:
            return 1
        res = 0
        i = 0
        while num:
            dig = int(num % 2 == 0)
            num //= 2
            res += dig * (2 ** i)
            i += 1

        return res


s = Solution()
print(s.findComplement(5))
