class Solution:
    def solve(self, board: list[list[str]]) -> None:
        if not board:
            return

        rows = len(board)
        cols = len(board[0])

        visited = [[0] * cols for _ in range(rows)]
        
        def dfs(r,c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return

            if board[r][c] != "O" or visited[r][c] == 1:
                return

            visited[r][c] = 1

            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c+1)
        for r in range(rows):
            if board[r][0] == "O":
                dfs(r, 0)

            if board[r][cols - 1] == "O":
                dfs(r, cols - 1)

        for c in range(cols):
            if board[0][c] == "O":
                dfs(0, c)
            if board[rows - 1][c] == "O":
                dfs(rows-1, c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and visited[r][c] == 0:
                    board[r][c] = "X"
        