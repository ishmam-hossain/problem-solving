class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        column = 0

        for i, c in enumerate(reversed(columnTitle)):
            char_num = ord(c) % 64
            column += char_num * 26 ** i

        return column


s = "ZY"
x = Solution()
print(x.titleToNumber(s))
