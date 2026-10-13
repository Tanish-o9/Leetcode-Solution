class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        n = len(grid)

        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        queue = deque([(0, 0, 1)])
        visited = {(0, 0)}
        directions = [
            (-1, 0), (1, 0),
            (0, -1), (0, 1),
            (-1, -1), (-1, 1),
            (1, -1), (1, 1)
        ]
        while queue:
            r, c, dist = queue.popleft()

            if r == n-1 and c == n-1:
                return dist

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if (0 <= nr < n and 0 <= nc < n
                and grid[nr][nc] == 0
                and (nr, nc) not in visited):
                
                    visited.add((nr, nc))
                    queue.append((nr, nc, dist+1))

        return -1