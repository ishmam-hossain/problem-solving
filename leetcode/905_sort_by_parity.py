class Solution:
    def sortArrayByParity(self, A):
        evens = []
        odds = []
        for n in A:
            if n % 2 == 0:
                evens.append(n)
            else:
                odds.append(n)
        return evens + odds

    def in_place(self, A):
        lo = 0
        hi = len(A) - 1

        while lo < hi:
            if A[lo] % 2 != 0 and A[hi] % 2 == 0:
                A[lo], A[hi] = A[hi], A[lo]
                lo += 1
                hi -= 1

            if A[lo] % 2 == 0:
                lo += 1
            if A[hi] % 2 != 0:
                hi -= 1

        return A


s = Solution()
print(s.in_place([0, 1]))
