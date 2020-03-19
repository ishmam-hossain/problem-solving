class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = d = 0
        for x in num2[::-1]:
            cur_sum = i = carry = 0
            for y in num1[::-1]:
                mul = (int(x) * int(y)) + carry
                digit = mul % 10
                cur_sum += digit * 10 ** i
                i += 1
                carry = mul // 10
            if carry:
                cur_sum += carry * 10 ** i

            res += cur_sum * (10 ** d)
            d += 1
        return str(res)


s = Solution()
print(s.multiply("124", "92"))
