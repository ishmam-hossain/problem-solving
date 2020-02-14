class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x

        start = 1
        end = x // 2
        while start <= end:
            mid = (start + end) // 2

            cal = mid * mid
            if cal == x:
                return mid
            if cal < x:
                ans = mid
                start = mid + 1
            else:
                end = mid - 1
        return ans


from math import sqrt
s = Solution()
print(int(sqrt(149)))
print(s.mySqrt(149))
