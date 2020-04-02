class Solution:
    def maxWidthRamp(self, A) -> int:
        seen = {}
        for i, n in enumerate(A):
            seen.setdefault(n, []).append(i)

        ind = float("inf")
        ramp = 0
        for n in sorted(A):
            ramp = max(ramp, seen[n][-1] - ind)
            ind = min(ind, seen[n][0])

        return ramp

    def bad_solution(self, A):
        ramp = 0
        for i, m in enumerate(A):
            for j, n in enumerate(A[i + 1:], i + 1):
                if A[i] <= A[j]:
                    ramp = max(ramp, j - i)

        return ramp


s = Solution()
# print(s.maxWidthRamp([6, 0, 8, 2, 1, 5]))
print(s.maxWidthRamp([9, 8, 1, 0, 1, 9, 4, 0, 4, 1]))
