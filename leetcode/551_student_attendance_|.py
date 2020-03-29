class Solution:
    def checkRecord(self, s: str) -> bool:
        absent = 2

        for i, c in enumerate(s):
            if c == "A":
                absent -= 1
            if absent == 0:
                return False
            if c == "L" and i+2 < len(s) and s[i+1] == "L" and s[i+2] == "L":
                return False

        else:
            return True


s = Solution()
print(s.checkRecord("PPALLL"))
