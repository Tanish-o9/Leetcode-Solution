
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        maxi = float('-inf')

        def solve(node):
            nonlocal maxi

            if node is None:
                return 0
            leftSum = solve(node.left)
            rightSum = solve(node.right)

            if leftSum < 0:
                leftSum = 0
            if rightSum < 0:
                rightSum = 0
            
            maxi = max(maxi, leftSum + node.val + rightSum)

            return node.val + max(leftSum, rightSum)

        solve(root)
        return maxi