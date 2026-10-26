
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def solve(node):
            nonlocal diameter

            if node is None:
                return 0
            leftheight = solve(node.left)
            rightheight = solve(node.right)

            diameter = max(diameter, leftheight+rightheight)

            return 1 + max(leftheight, rightheight)

        solve(root)
        return diameter
