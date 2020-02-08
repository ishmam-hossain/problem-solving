class Solution:
    def isValid(self, s: str) -> bool:
        p = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = []
        keys = p.keys()
        for c in s:
            if c not in keys:
                stack.append(c)
            else:
                if not stack:
                    return False
                if stack.pop() != p.get(c):
                    return False
                else:
                    continue

        return True if not stack else False


C = Solution()
print(C.isValid("()[}"))


