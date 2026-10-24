from collections import deque

class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        rows = len(mat)
        cols = len(mat[0])

        visited = [[0] * cols for _ in range(rows)]
        distance = [[0] * cols for _ in range(rows)]

        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    queue.append((r, c, 0))
                    visited[r][c] = 1

        while queue:
            i, j, d = queue.popleft()
            distance[i][j] = d

            for x, y in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                new_i = i + x
                new_j = j + y

                if new_i < 0 or new_i >= rows or new_j < 0 or new_j >= cols:
                    continue

                if visited[new_i][new_j] == 1:
                    continue

                visited[new_i][new_j] = 1
                queue.append((new_i, new_j, d + 1))

        return distance