class Solution:
    def fizzBuzz(self, n: int):
        res = []

        for i in range(1, n+1):
            div_3 = (i % 3 == 0)
            div_5 = (i % 5 == 0)

            if i == 1 or i == 2:
                res.append(str(i))
            elif div_3 and div_5:
                res.append("FizzBuzz")
            elif div_3 and not div_5:
                res.append("Fizz")
            elif div_5 and not div_3:
                res.append("Buzz")
            else:
                res.append(str(i))

        return res


s = Solution()
print(s.fizzBuzz(1))
