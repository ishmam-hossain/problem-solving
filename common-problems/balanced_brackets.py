def isBalanced(s):
    brackets = {
        ")": "(",
        "}": "{",
        "]": "["
    }

    stack = []

    for c in s:
        if c not in brackets:
            stack.append(c)
        else:
            if not c in brackets:
                stack.append(c)
            else:
                if stack and stack.pop() == brackets[c]:
                    continue
                else:
                    return "NO"

    return "YES" if not stack else "NO"


print(isBalanced("("))
