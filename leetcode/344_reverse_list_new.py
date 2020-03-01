class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        length = len(s)
        while i < length // 2:
            s[i], s[length - 1 - i] = s[length - 1 - i], s[i]
            i += 1
