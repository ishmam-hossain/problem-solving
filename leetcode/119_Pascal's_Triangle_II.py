class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        zero = [1]
        one = [1, 1]

        if rowIndex == 0:
            return zero
        if rowIndex == 1:
            return one
        
        cur = one
        for row in range(2, rowIndex + 1):
            res = [1] * (row + 1)
            for i in range(1, row):
                res[i] = cur[i-1]+cur[i]
            cur = res
        
        return cur
