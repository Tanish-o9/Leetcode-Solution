class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        V = len(graph)

        adj_list = [[] for _ in range(V)]
        for node in range(V):
            for adjNode in graph[node]:
                adj_list[adjNode].append(node)

        indegrees = [0] * V
        for node in range(V):
            for adjNode in adj_list[node]:
                indegrees[adjNode] += 1
        queue = deque()

        for i in range(V):
            if indegrees[i] == 0:
                queue.append(i)

        result = []
        while queue:
            node = queue.popleft()
            result.append(node)
            for adjNode in adj_list[node]:
                indegrees[adjNode] -= 1
                if indegrees[adjNode] == 0:
                    queue.append(adjNode)
                    
        result.sort()
        return result