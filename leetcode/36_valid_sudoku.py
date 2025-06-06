class Solution:
    @staticmethod
    def getSquaresAsItr(board):
        for i in range(0, len(board), 3):
            for j in range(0, len(board), 3):
                box = []
                for row in range(i, i+3):
                    for col in range(j, j+3):
                        box.append(board[row][col])
                yield box

    @staticmethod
    def containDuplicate(itr):
        seen = set()
        for elem in itr:
            if elem == ".":
                continue
            if elem in seen:
                return True
            seen.add(elem)

        return False

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 1. Check each row
        for row in range(len(board)):
            # print(board[row])
            if self.containDuplicate(board[row]):
                return False
        # 2. Check each columns
        for col in range(len(board)):
            cols = []
            for r in range(len(board)):
                cols.append(board[r][col])

            if self.containDuplicate(cols):
                return False
        # 3. Check each box
        for square in self.getSquaresAsItr(board):
            if self.containDuplicate(square):
                return False

        return True

    def isValidOptimized(board):
        seen = {'rows': defaultdict(set), 'cols': defaultdict(set), 'squares': defaultdict(set)}

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue

                if (board[r][c] in seen['rows'][r] or
                    board[r][c] in seen['cols'][c] or
                    board[r][c] in seen['squares'][(r//3,c//3)]):
                    return False

                seen['rows'][r].add(board[r][c])
                seen['cols'][c].add(board[r][c])
                seen['squares'][(r//3,c//3)].add(board[r][c])

        return True
