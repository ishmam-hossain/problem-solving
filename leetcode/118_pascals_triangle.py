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
            temp[0] = temp[-1] = 1

            for j in range(1, i-1):
                temp[j] = res[-1][j-1] + res[-1][j]

            res.append(temp)

        return res


s = Solution()
print(s.generate(5))

