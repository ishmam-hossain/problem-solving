class Solution:
    def isPalindrome(self, s: str) -> bool:
        lo, hi = 0, len(s) - 1
        s = s.lower()

        while lo < hi:
            if not s[lo].isalnum():
                lo += 1
            if not s[hi].isalnum():
                hi -= 1
            if s[lo].isalnum() and s[hi].isalnum():
                if s[lo] == s[hi]:
                    lo += 1
                    hi -= 1
                else:
                    return False
        return True


s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))
