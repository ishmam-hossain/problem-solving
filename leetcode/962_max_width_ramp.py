class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        """O(N^2) solution. TLE on the way :3"""
        ramp = 0
        for i, m in enumerate(A):
            for j, n in enumerate(A[i+1:], i+1):
                if A[i] <= A[j]:
                    ramp = max(ramp, j-i)

        return ramp
