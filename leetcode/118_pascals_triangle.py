class Solution:
    def generate(self, numRows):
        res = [[1], [1, 1]]
        if numRows <= 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return res

        for i in range(3, numRows + 1):
            temp = [None]*i
            insert_range = i - 2
            # for index in range(insert_range, )


s = Solution()
print(s.generate(5))

