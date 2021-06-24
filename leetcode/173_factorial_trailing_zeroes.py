class Solution:
    def factorial(self, _num):
        f = 1
        for i in range(1, _num+1):
            f *= i
        return f

    def trailingZeroes(self, n: int) -> int:
        f = self.factorial(n)
        count = 0
        while f:
            trailing_digit = f % 10
            if trailing_digit != 0:
                break
            count += 1
            f = f // 10

        return count


s = Solution()
num = 9187
print(s.trailingZeroes(num))


"""
Given an integer n, return the number of trailing zeroes in n!.

Follow up: Could you write a solution that works in logarithmic time complexity?

 

Example 1:

Input: n = 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:

Input: n = 5
Output: 1
Explanation: 5! = 120, one trailing zero.
Example 3:

Input: n = 0
Output: 0
 

Constraints:

0 <= n <= 104
"""
