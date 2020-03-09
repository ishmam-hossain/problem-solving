class Solution:
    def commonChars(self, A):
        if not A:
            return []
        dicts = []
        for word in A:
            temp_dict = {}
            for c in word:
                temp_dict[c] = temp_dict.get(c, 0) + 1
            dicts.append(temp_dict)

        res = []
        for key, val in dicts[0].items():
            if all(key in d for d in dicts):
                min_appeared = 99999999999
                for x in dicts:
                    min_appeared = min(min_appeared, x.get(key))
                res.extend([key]*min_appeared)

        return res


s = Solution()
print(s.commonChars(["bella","label","roller"]))
