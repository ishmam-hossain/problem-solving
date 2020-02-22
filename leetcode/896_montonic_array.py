class Solution:
    def isMonotonic(self, A) -> bool:
        if not A:
            return False

        increasing_sum = 0
        decreasing_sum = 0

        for i, n in enumerate(A[:-1]):
            if n < A[i+1]:
                increasing_sum += 1
            elif n > A[i+1]:
                decreasing_sum += 1
            else:
                increasing_sum += 1
                decreasing_sum += 1

        return increasing_sum == 0 or decreasing_sum == 0 or increasing_sum == len(A) - 1 or decreasing_sum == len(A) - 1


s = Solution()
print(s.isMonotonic([6, 5, 4, 4]))




