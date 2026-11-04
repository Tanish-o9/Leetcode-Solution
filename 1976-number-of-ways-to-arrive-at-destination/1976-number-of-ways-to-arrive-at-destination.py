class Solution:
    def countPaths(self, n: int, roads: list[list[int]]) -> int:
        MOD = 10**9 + 7
        adj = [[] for _ in range(n)]
        for u, v, time in roads:
            adj[u].append((v, time))
            adj[v].append((u, time))
        dist = [float('inf')] * n
        ways = [0] * n

        dist[0] = 0
        ways[0] = 1

        pq = [(0, 0)]

        while pq:
            d, node = heapq.heappop(pq)
            if d > dist[node]:
                continue

            for neighbor, time in adj[node]:
                new_dist = d + time

                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    ways[neighbor] = ways[node]
                    heapq.heappush(pq, (new_dist, neighbor))

                elif new_dist == dist[neighbor]:
                    ways[neighbor] = (
                        ways[neighbor] + ways[node]
                    ) % MOD

        return ways[n - 1]