class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        fresh_cnt = 0
        queue = deque()

        # sabhi fresh and rotten oranges ko find krna
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_cnt += 1
        # agar koi fresh orange n mile to
        if fresh_cnt == 0:
            return 0
        minutes = 0
        
        # BFS ka use krke rot spread
        while queue and fresh_cnt > 0:
            total_rotten = len(queue)

            for _ in range(total_rotten):
                i,j = queue.popleft()

                # check top, down, left, right
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    new_i = i + dx
                    new_j = j + dy

                    # now check boundries
                    if (new_i < 0 or new_i >= rows or new_j < 0 or new_j >= cols):
                        continue
                    # only fresh oranges can rotten so -
                    if grid[new_i][new_j] != 1:
                        continue

                    grid[new_i][new_j] = 2
                    fresh_cnt -= 1
                    queue.append((new_i, new_j))
            minutes += 1
        
        # if fresh orang remain left
        if fresh_cnt > 0:
            return -1
        return minutes