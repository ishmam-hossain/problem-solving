class Solution:
    def balancedStringSplit(self, s: str) -> int:
        result = 0
        bal_count = 0
        for c in s:
            if c == 'R':
                bal_count += 1
            elif c == 'L':
                bal_count -= 1

            if bal_count == 0:
                result += 1

        return result