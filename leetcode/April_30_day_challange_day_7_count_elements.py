class Solution:
    def countElements(self, arr) -> int:
        count = {}
        for n in arr:
            count[n] = count.get(n, 0) + 1

        res = 0

        for n in arr:
            if n + 1 in count and count[n + 1] > 0:
                res += 1

        return res
