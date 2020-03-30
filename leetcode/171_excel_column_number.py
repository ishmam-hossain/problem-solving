class Solution:
    def titleToNumber(self, s: str) -> int:
        column = 0
        for i, c in enumerate(s):
            n = ord(c) - ord('A') + 1
            print(n)



s = Solution()
print(s.titleToNumber("AB"))
