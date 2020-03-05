class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_d = {}
        t_d = {}

        for c in s:
            s_d[c] = s_d.get(c, 0) + 1
        for c in t:
            t_d[c] = t_d.get(c, 0) + 1

        for key, val in s_d.items():
            if key not in t_d:
                return False
            if s_d[key] != t_d[key]:
                return False
        else:
            return True
