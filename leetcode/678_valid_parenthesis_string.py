class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        stars = bad = 0

        for c in s:
            if c == "*":
                stars += 1
                stack.append("*")

            elif c == "(":
                stack.append("(")

            else:
                if not stack:
                    return False
                if c == stack.pop():
                    continue
                else:
                    bad += 1
        return bad + stars >= len(stack) and stars >= stack.count("(")


sol = Solution()
print(sol.checkValidString("((()**))"))
print(sol.checkValidString("()((()(*))*())"))
print(sol.checkValidString(")))"))
print(sol.checkValidString("())((((********)(**))())"))
print(sol.checkValidString("(((()"))
print(sol.checkValidString("))))"))
print(sol.checkValidString("*()(())*()(()()((()(()()*)(*(())((((((((()*)(()(*)"))
print(sol.checkValidString("(*()"))
print(sol.checkValidString("((*)"))









"""
         # if not s:
        #     return True
        #
        # p = {
        #     ")": "(",
        # }
 

            # if c not in p:
            #     stack.append(c)
            # else:
            #     if stack:
            #         val = stack.pop()
            #         if val == "*":
            #             stars += 1
            #         else:
            #             if val == p[c]:
            #                 continue
            #             else:
            #                 bad += 1
            #     else:
            #         continue

        print(bad, stars)
        print(stack)
 
 """