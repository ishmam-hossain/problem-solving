class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}

        for i in range(len(s)):
            if s[i] not in s_dict and t[i] not in t_dict:
                s_dict[s[i]] = t[i]
                t_dict[t[i]] = s[i]
            else:
                if s_dict.get(s[i]) != t[i] or t_dict.get(t[i]) != s[i]:
                    return False

        return True


s = Solution()
print(s.isIsomorphic("aa", "ab"))
print(s.isIsomorphic("ab", "aa"))
