class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        rows = len(board)
        cols = len(board[0])

        ships = 0

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == ".":
                    continue
                if c > 0 and board[r][c-1] == "X":
                    continue
                if r > 0 and board[r-1][c] == "X":
                    continue
                ships += 1
        return ships
                
