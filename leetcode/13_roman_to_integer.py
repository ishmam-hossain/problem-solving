class Solution:
    vals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    def romanToInt(self, s: str) -> int:
        res = 0
        for i, c in enumerate(s):
            if i + 1 < len(s):
                if self.vals.get(s[i+1]) > self.vals.get(s[i]):
                    res -= self.vals.get(s[i])
                else:
                    res += self.vals.get(s[i])
            else:
                res += self.vals.get(s[i])

        return res


s = Solution()
print(s.romanToInt('MCMXCIV'))
