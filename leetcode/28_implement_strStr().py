class Solution:
    def old_strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if len(haystack) < len(needle):
            return -1
        i = 0
        start = -1
        while i < len(haystack):
            j = 0
            if haystack[i] == needle[j]:
                start = i
                while j < len(needle) and i < len(haystack) and haystack[i] == needle[j]:
                    i += 1
                    j += 1
                else:
                    return start
            i += 1
        return start

    def strStr(self, haystack, needle):
        if not needle:
            return 0
        if len(haystack) < len(needle):
            return -1

        for i in range(len(haystack)):
            if haystack[i:i + len(needle)] == needle:
                return i

        return -1


s = Solution()
print(s.strStr("aaaa", "bbb"))
