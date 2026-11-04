class Solution:
    def canReach(self, arr: list[int], start: int) -> bool:
        visited = set()
        def dfs(index):
            if index < 0 or index >= len(arr):
                return False
            if index in visited:
                return False
            if arr[index] == 0:
                return True

            visited.add(index)
            left = dfs(index - arr[index])
            rit = dfs(index + arr[index])
            return left or rit

        return dfs(start)