class Solution:

    def get_chunk_result(self, chunk):
        chunk_len = len(chunk)
        if chunk_len == 4:
            return ((chunk[0] * chunk[1]) // chunk[2]) + chunk[3]
        elif chunk_len == 3:
            return (chunk[0] * chunk[1]) // chunk[2]
        elif chunk_len == 2:
            return chunk[0] * chunk[1]
        return chunk[0]

    def clumsy(self, n: int) -> int:
        chunks = [[i for i in range(r, r-4, -1) if i > 0] for r in range(n, 0, -4)]
        cf = self.get_chunk_result(chunks[0])
        for chunk in chunks[1:]:
            cf -= self.get_chunk_result(chunk)
        return cf

# 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1
#     18                10            2

# 9 * 8 / 7 + 6 - 5 * 4 / 3 + 2 - 1 = 11
# 72 / 7 + 6 - 20 / 3 + 2 -1
# 10 + 6 - 6 + 2 - 1
# 16 - 8 - 1
s = Solution()
# print(s.clumsy(4))
# print('-'*50)
# print(s.clumsy(5))
# print('-'*50)
# print(s.clumsy(6))
# print('-'*50)
# print(s.clumsy(7))
# print('-'*50)
# print(s.clumsy(10))
print(s.clumsy(9))
