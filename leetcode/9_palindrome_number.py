from math import log10


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x == 0:
            return True

        l = int(log10(x)) + 1
        res = [None]*l
        while x:
            rem = x % 10
            res[l-1] = rem
            l -= 1
            x = x // 10

        for i in range(len(res)):
            if res[i] == res[l-1-i]:
                continue
            else:
                return False
        return True


s = Solution()
print(s.isPalindrome(0))
