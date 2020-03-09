class Solution:
    def heightChecker(self, heights) -> int:
        s = sorted(heights)
        count = 0
        for m, n in zip(heights, s):
            if m != n:
                count += 1

        return count


s = Solution()
print(s.heightChecker([1,2,3,4,5]))