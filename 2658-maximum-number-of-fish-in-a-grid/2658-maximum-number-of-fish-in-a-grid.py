class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        max_fish = 0

        def dfs(r,c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return 0
            if grid[r][c] == 0:
                return 0

            fish = grid[r][c]

            grid[r][c] = 0

            fish += dfs(r-1,c)
            fish += dfs(r+1,c)
            fish += dfs(r,c-1)
            fish += dfs(r,c+1)

            return fish
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] > 0:
                    fish = dfs(r,c)
                    max_fish = max(max_fish, fish)
        return max_fish

            