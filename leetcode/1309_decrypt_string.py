# s = "10#11#12"
# s = "12345"
#
# a = s.split("#")
#
# for i in a[:-1]:
#     k = chr(ord('a') + int(i) - 1)
#     print(k)
#
# for


class Solution:
    def freqAlphabets(self, s: str) -> str:
        chars = []
        i = 0
        while i < len(s):
            if i + 2 < len(s) and s[i+2] == "#":
                chars.append(s[i:i+2])
                i += 3
            else:
                chars.append(s[i])
                i += 1

        return "".join([chr(ord('a') + int(c) - 1) for c in chars])


s = Solution()
print(s.freqAlphabets("12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"))
