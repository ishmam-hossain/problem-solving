class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        mat = []
        for _ in range(numRows):
            mat.append(['' for _ in range(len(s))])

        row_counter = 0
        col_counter = 0
        going_down = True

        for c in s:
            mat[row_counter][col_counter] = c
            if row_counter == numRows - 1:
                going_down = False
            if row_counter == 0:
                going_down = True

            if going_down:
                # go down, incr row
                if row_counter < numRows:
                    row_counter += 1
            else:
                # go diagonally, incr col, decr row
                row_counter -= 1
                col_counter += 1

        return ''.join([''.join(row) for row in mat])
