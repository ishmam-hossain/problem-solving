class Solution:
    def bitwiseComplement(self, N: int) -> int:
        if N == 0:
            return 1
        res = 0
        i = 0
        while N:
            digit = ~N % 2
            res += digit * (2 ** i)
            N //= 2
            i += 1

        return res


s = Solution()
print(s.bitwiseComplement(0))
