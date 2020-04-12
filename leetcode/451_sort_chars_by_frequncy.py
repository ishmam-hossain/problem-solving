class Solution:
    def frequencySort(self, s: str) -> str:
        chars = {}

        for c in s:
            chars[c] = chars.get(c, 0) + 1

        res = [k for k, v in sorted(chars.items(), key=lambda item: item[1], reverse=True)]
        return "".join([f"{key*chars[key]}" for key in res])


s = Solution()
print(s.frequencySort("tree"))
