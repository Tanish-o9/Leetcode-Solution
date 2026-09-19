class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return []
        queue = deque([root])
        ans = root.val

        while queue:
            level_size = len(queue)
            

            for i in range(level_size):
                node = queue.popleft()
                if i == 0:
                    ans = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
        return ans