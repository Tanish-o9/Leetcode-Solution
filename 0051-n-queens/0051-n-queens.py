class Solution:
    def solve(self, col, board, ans, leftrow, lowerdiagonal, upperdiagonal, n):
        if col == n:
            ans.append(board[:])
            return
        for row in range(n):
            if (leftrow[row] == 0 and lowerdiagonal[row+col] == 0 and upperdiagonal[n-1+col-row] == 0):
                board[row] = board[row][:col] + "Q" + board[row][col + 1:]
                leftrow[row] = 1
                lowerdiagonal[col+row] = 1
                upperdiagonal[n-1+col-row] = 1
                self.solve(col+1, board, ans, leftrow, lowerdiagonal, upperdiagonal, n)
                board[row] = board[row][:col] + "." + board[row][col + 1:]
                leftrow[row] = 0
                lowerdiagonal[row+col] = 0
                upperdiagonal[n-1+col-row] = 0

    def solveNQueens(self, n: int) -> list[list[str]]:
        ans = []
        board = ["." * n for _ in range(n)]
        leftrow = [0] * n
        upperdiagonal = [0] * (2 * n - 1)
        lowerdiagonal = [0] * (2 * n - 1)
        self.solve(0, board, ans, leftrow, lowerdiagonal, upperdiagonal, n)
        return ans