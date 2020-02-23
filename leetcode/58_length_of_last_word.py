class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if s is None or s.rstrip() == "":
            return 0

        for i, c in enumerate(s.rstrip()[::-1]):
            if c == ' ':
                return i
        else:
            return len(s.rstrip())


s = Solution()
print(s.lengthOfLastWord("a "))
print(s.lengthOfLastWord("aaa"))
