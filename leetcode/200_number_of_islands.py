class Solution:
    def numIslands(self, grid) -> int:
        count = 0
        right, bottom = len(grid[0]), len(grid)

        for i in range(bottom):
            for j in range(right):
                if grid[i][j] == "1":
                    self.dfs(grid, i, j)
                    count += 1
        return count

    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
            return

        grid[i][j] = "#"
        self.dfs(grid, i+1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j-1)


s = Solution()
grd = [
    list("11110"),
    list("11010"),
    list("11000"),
    list("00000")
]

print(s.numIslands(grd))
