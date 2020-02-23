class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        vowel_positions = []
        res = [None]*len(s)

        for i, c in enumerate(s):
            if c in vowels:
                vowel_positions.append(i)
            else:
                res[i] = c

        start = 0
        end = len(vowel_positions) - 1

        while start <= end:
            res[vowel_positions[start]], res[vowel_positions[end]] = s[vowel_positions[end]], s[vowel_positions[start]]
            start += 1
            end -= 1

        return "".join(res)


s = Solution()
print(s.reverseVowels("aA"))
