class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num1) > len(num2):
            longest_str = num1
            smallest_str = num2
        else:
            longest_str = num2
            smallest_str = num1

        _sum = []
        _carry = 0
        lsl = len(longest_str)
        ssl = len(smallest_str)

        for i in range(lsl):
            if i >= ssl:
                smallest_str_val = '0'
            else:
                smallest_str_val = smallest_str[ssl - 1 - i]

            cur_sum = int(longest_str[lsl - i - 1]) + int(smallest_str_val) + _carry
            _sum.append(str(cur_sum % 10))
            _carry = cur_sum // 10

        if _carry:
            _sum.append(str(_carry))

        return "".join(_sum[::-1])


s = Solution()
print(s.addStrings("408", "5"))
