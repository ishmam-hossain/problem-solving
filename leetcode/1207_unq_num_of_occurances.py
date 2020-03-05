class Solution:
    def uniqueOccurrences(self, arr) -> bool:
        d = {}
        for n in arr:
            d[n] = d.get(n, 0) + 1

        return len(d.values()) == len(set(d.values()))
