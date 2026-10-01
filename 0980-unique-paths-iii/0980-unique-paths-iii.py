class Solution:
    def uniquePathsIII(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        empty = 0
        x = y = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != -1:
                    empty += 1

                if grid[i][j] == 1:
                    x, y = i, j

        def dfs(i, j, count):
            if grid[i][j] == 2:
                return 1 if count == empty else 0

            grid[i][j] = -1
            paths = 0

            if i + 1 < m and grid[i + 1][j] != -1:
                paths += dfs(i + 1, j, count + 1)
            
            if i - 1 >= 0 and grid[i - 1][j] != -1:
                paths += dfs(i - 1, j, count + 1)
            
            if j + 1 < n and grid[i][j + 1] != -1:
                paths += dfs(i, j + 1, count + 1)

            if j - 1 >= 0 and grid[i][j - 1] != -1:
                paths += dfs(i, j - 1, count + 1)

            grid[i][j] = 0
            return paths
        return dfs(x, y, 1)
