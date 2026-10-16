class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        dead = set(deadends)
        if '0000' in dead:
            return -1

        queue = deque([('0000' , 0)])
        visited = {'0000'}

        while queue:
            lock, step = queue.popleft()
            if lock == target:
                return step
            for i in range(4):
                digit = int(lock[i])
                for move in [-1, 1]:
                    new_digit = (move + digit) % 10
                    new_lock = lock[:i] + str(new_digit) + lock[1 + i:]

                    if new_lock not in visited and new_lock not in dead:
                        visited.add(new_lock)
                        queue.append((new_lock, step+1))
        return -1