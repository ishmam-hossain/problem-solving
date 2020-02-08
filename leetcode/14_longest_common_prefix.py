class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if not strs:
            return ""
        longest_prefix = []
        for i, c in enumerate(strs[0]):
            for s in strs[1:]:
                if i >= len(s):
                    return "".join(longest_prefix)
                else:
                    if s[i] == c:
                        continue
                    else:
                        return "".join(longest_prefix)
            else:
                longest_prefix.append(c)

        return "".join(longest_prefix)


s = Solution()
print(s.longestCommonPrefix(["flower", "flow", "flight"]))
print(s.longestCommonPrefix(["dog", "racecar", "car"]))
print(s.longestCommonPrefix(["dogo", "dog", "dogogogo"]))
print(s.longestCommonPrefix(["aca", "cba"]))

