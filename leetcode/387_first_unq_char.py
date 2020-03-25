class Solution:
    def firstUniqChar(self, s: str) -> int:
        res = {}
        for i, c in enumerate(s):
            found = res.get(c, {"count": 0, "pos": -1})
            up = {"count": found["count"] + 1, "pos": i}
            res[c] = up

        res = {k: v for k, v in res.items() if v["count"] == 1}
        if not res:
            return -1

        r = [v["pos"] for v in list(res.values())]
        return min(r)

class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i, c in enumerate(s):
            if s.count(c) == 1:
                return i
        else:
            return -1


s = Solution()
print(s.firstUniqChar("llohe"))
