class Solution:
    def reverseWords(self, s: str) -> str:
        x = s.split()
        return " ".join(x[::-1])


s = Solution()
print(s.reverseWords("a good   example"))
