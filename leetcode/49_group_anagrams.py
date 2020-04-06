class Solution:
    def groupAnagrams(self, strs):
        res = {}
        for s in strs:
            key = self.ascii_key(s)
            res.setdefault(key, []).append(s)

        return res.values()

    def ascii_key(self, s):
        arr = [0] * 26
        for c in s:
            arr[ord(c) - ord('a')] += 1

        return str(arr)


s = Solution()
print(s.groupAnagrams(["cab", "tin", "pew", "duh", "may", "ill", "buy", "bar", "max", "doc"]))
