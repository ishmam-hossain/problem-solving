class Solution:
    def toLowerCase(self, str: str) -> str:
        res = []
        for c in str:
            if 65 <= ord(c) <= 90:
                c = chr(ord(c) + 32)
            res.append(c)

        return "".join(res)


s = Solution()
print(s.toLowerCase("AAAAAAABBBBBBB"))
