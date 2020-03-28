class Solution:
    def findWords(self, words):
        row_to_keys = {
            1: {"Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"},
            2: {"A", "S", "D", "F", "G", "H", "J", "K", "L"},
            3: {"Z", "X", "C", "V", "B", "N", "M"}
        }

        final = []
        for word in words:
            res = []
            for c in word:
                for k, v in row_to_keys.items():
                    if c.upper() in v:
                        res.append(k)

            if len(set(res)) == 1:
                final.append(word)

        return final


s = Solution()
print(s.findWords(["Hello", "Alaska", "Dad", "Peace"]))
