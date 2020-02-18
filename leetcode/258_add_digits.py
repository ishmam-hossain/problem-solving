class Solution:
    def addDigits(self, num: int) -> int:
        """iterative solution"""
        while num > 9:
            cur = num
            _sum = 0
            while cur:
                _sum += cur % 10
                cur //= 10
            num = _sum

        return num

    def in_constant_time(self, num):
        """O(1) solution"""
        if num == 0:
            return 0
        if num % 9 == 0:
            return 9
        return num % 9


s = Solution()
print(s.addDigits(0))
print(s.in_constant_time(0))

"""
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

Example:

Input: 38
Output: 2 
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
             Since 2 has only one digit, return it.
             
Follow up:
Could you do it without any loop/recursion in O(1) runtime??????????????????????????
"""