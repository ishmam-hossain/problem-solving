class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num <= 0:
            return False
        if num == 1:
            return True
        low = 1
        hi = num // 2

        while low <= hi:
            mid = (low + hi) // 2
            sqr_val = mid * mid

            if sqr_val == num:
                return True
            elif sqr_val > num:
                hi = mid - 1
            else:
                low = mid + 1

        return False


s = Solution()
print(s.isPerfectSquare(1))
