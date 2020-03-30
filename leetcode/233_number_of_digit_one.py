from math import log10


class Solution:
    def countDigitOne(self, n: int) -> int:
        def count_by_number_of_digits(x):
            nod = int(log10(x)) + 1

            if nod == 1:
                return 1
            if nod == 2:
                return 19

            return count_by_number_of_digits(x % 10) + count_by_number_of_digits(x % 100)

        return count_by_number_of_digits(n)


s = Solution()
print(s.countDigitOne(13))
