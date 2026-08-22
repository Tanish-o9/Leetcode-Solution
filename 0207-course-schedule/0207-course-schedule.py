class Queue:
        def __init__(self):
            self.q = []
            self.front = -1
        def push(self, x):
            if self.front == -1:
                self.front = 0
            self.q.append(x)
        def pop(self):
            if len(self.q) == 0:
                return -1
            x = self.q[self.front]
            self.front += 1
            if self.front == len(self.q):
                self.front = -1
                self.q = []
            return x

        def getfront(self):
            if len(self.q) == 0:
                return -1
            return self.q[self.front]

        def size(self):
            if self.front == -1:
                return 0
            return len(self.q) - self.front

class Solution:
    def canFinish(self, n: int, prerequisites: List[List[int]]) -> bool:
        q = Queue()
        ans = []
        indegree = [0] * n
        adjlist = []

        for i in range(n):
            adjlist.append([])

        for a,b in prerequisites:
            indegree[a]+=1
            adjlist[b].append(a)

        for i in range(n):
            if indegree[i] == 0:
                ans.append(i)
                q.push(i)

        while q.size()>0:
            front = q.pop()
            for x in adjlist[front]:
                indegree[x] -= 1
                if indegree[x] == 0:
                    ans.append(x)
                    q.push(x)

        if len(ans) == n:
            return True
        else:
            return False