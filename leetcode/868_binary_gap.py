class Solution:
    def binaryGap(self, N: int) -> int:
        """O(N^2) solution and I'm pleasantly surprised! :v"""

        s = bin(N)
        max_gap = 0

        for i, c in enumerate(s[2:], 2):
            if c == "1":
                for j, d in enumerate(s[i+1:], i+1):
                    if d == "1":
                        max_gap = max(max_gap, j-i)
                        break
        return max_gap


s = Solution()
print(s.binaryGap(8738937297397273629376273823862947368947568))
