from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = -1
        for i, a in enumerate(height):
            for j, b in enumerate(height[i:], i):
                volume = (j - i) * min(a, b)
                max_water = max(max_water, volume)

        return max_water


s = Solution()
print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
