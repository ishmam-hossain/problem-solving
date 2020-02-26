class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        while num:
            if num % 2 == 0:
                num //= 2
            else:
                num -= 1
            steps += 1

        return steps


s = Solution()
print(s.numberOfSteps(14))


