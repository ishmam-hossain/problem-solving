class Solution:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        length = len(s)
        for i in range(length//2):
            s[i], s[length - 1 - i] = s[length - 1 - i], s[i]

        print(s)


s = Solution()
print(s.reverseString(list("hello")))
