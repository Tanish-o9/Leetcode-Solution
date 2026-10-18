class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        for course, pre in prerequisites:
            adj[pre].append(course)
        visited = [0] * numCourses
        path_visited = [0] * numCourses
        def dfs(node):
            visited[node] = 1
            path_visited[node] = 1
            for adjNode in adj[node]:
                if visited[adjNode] == 0:
                    if dfs(adjNode):
                        return True
                elif path_visited[adjNode] == 1:
                    return True
            path_visited[node] = 0
            return False
        for i in range(numCourses):
            if visited[i] == 0:
                if dfs(i):
                    return False
        return True