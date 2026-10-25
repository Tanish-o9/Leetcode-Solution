
class Solution:
    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:
        sizes = []

        def solve(node):
            if node is None:
                return 0
            
            left = solve(node.left)
            right = solve(node.right)

            if left == -1 or right == -1 or left != right:
                return -1

            size = 1 + left + right

            sizes.append(size)

            return size
        solve(root)
        sizes.sort(reverse = True)

        if len(sizes) < k:
            return -1

        return sizes[k - 1]