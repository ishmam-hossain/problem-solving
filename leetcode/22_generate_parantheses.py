def combos(chars, length):
    if length == 0:
        yield ''
        return
    for char in chars:
        for combo in combos(chars, length - 1):
            yield f'{char}{combo}'


def validate_parentheses(paran):
    stack = []
    for c in paran:
        if c == '(':
            stack.append(c)
        else:
            try:
                if stack.pop() != '(':
                    return False
            except IndexError:
                return False
    return True if not stack else False


class Solution:
    def generateParenthesis(self, n: int):
        final = []
        res = combos(('(', ')'), n * 2)
        for r in res:
            if validate_parentheses(r):
                final.append(r)

        return final


s = Solution()
print(s.generateParenthesis(2))


"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

for 2
[
    "(())",
    "()()"
]

"""