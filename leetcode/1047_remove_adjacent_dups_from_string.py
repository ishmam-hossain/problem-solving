class Solution:
    def removeDuplicates(self, S: str) -> str:
        res = []

        for c in S:
            if res and c == res[-1]:
                res.pop()
            else:
                res.append(c)

        return "".join(res)


s = Solution()
print(s.removeDuplicates("azxxzy"))
