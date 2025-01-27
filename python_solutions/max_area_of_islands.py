class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        big_island = 0


        def dfs(r, c):
            if r < 0 or c < 0 or r >= row or c >= col or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            res = 1
            res += dfs(r +1, c)
            res += dfs(r-1, c)
            res += dfs(r, c + 1)
            res += dfs(r, c- 1)
            return res

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    size = dfs(r,c)
                    big_island = max(big_island, size)
        return big_island

