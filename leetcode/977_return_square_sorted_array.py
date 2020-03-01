from collections import deque


class Solution:
    def sortedSquares(self, A):
        a = [n**2 for n in A]
        a.sort()
        return a


s = Solution()
print(s.sortedSquares([-4, -2, -1, 0, 1, 4, 6, 9]))
