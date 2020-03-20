class Solution:
    def get_xor(self, arr):
        x = 0
        for c in arr:
            x ^= ord(c)
        return x

    def findTheDifference(self, s: str, t: str) -> str:
        return chr(self.get_xor(s) ^ self.get_xor(t))


s = Solution()
print(s.findTheDifference("abcd", "abecd"))
