class Solution:
    def getSum(self, a: int, b: int) -> int:
        if -a == b:
            return 0

        while b != 0:
            carry = a & b
            a = a ^ b
            if b > 0:
                b = carry << 1
            else:
                b = carry >> 1

            print(a, b, carry)

        return a


s = Solution()
print(s.getSum(3, -2))
