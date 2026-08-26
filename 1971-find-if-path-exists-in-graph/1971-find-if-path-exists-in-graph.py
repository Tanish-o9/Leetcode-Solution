class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj = [[] for _ in range(n)]
        for u , v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = [False] * n
        def dfs(node):
            if node == destination:
                return True

            visited[node] = True

            for neighbor in adj[node]:
                if not visited[neighbor]:
                    if dfs(neighbor):
                        return True
            return False
        return dfs(source)