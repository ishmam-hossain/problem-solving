# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
# class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        row, col = binaryMatrix.dimensions()
        res = col

        i = 0
        j = col - 1
        found = False

        while i < row and j >= 0:
            val = binaryMatrix.get(i, j)

            if val == 1:
                res = min(res, j)
                j -= 1
                found = True
            else:
                i += 1

        return res if found else -1