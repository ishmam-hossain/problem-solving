class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        S = list(S)
        lo = 0
        hi = len(S) - 1

        while lo < hi:
            if S[lo].isalpha() and S[hi].isalpha():
                S[lo], S[hi] = S[hi], S[lo]
                lo += 1
                hi -= 1

            if not S[lo].isalpha():
                lo += 1
            if not S[hi].isalpha():
                hi -= 1
        return "".join(S)


s = Solution()
print(s.reverseOnlyLetters("a"))
