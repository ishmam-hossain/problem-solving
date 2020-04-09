class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        return self.sanitize(S) == self.sanitize(T)

    def sanitize(self, s):
        res = [""] * len(s)
        j = 0
        for i, c in enumerate(s):
            if c == "#":
                j -= 1
                if j < 0:
                    j = 0
                res[j] = ""
                continue

            res[j] = c
            j += 1

        return "".join(res)