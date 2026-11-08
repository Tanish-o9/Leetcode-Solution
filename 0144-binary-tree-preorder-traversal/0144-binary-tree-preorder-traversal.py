class Solution:
    def __init__(self):
        self.ans = []

    def preorder(self, root):
        if root is None:
            return
        self.ans.append(root.val)
        self.preorder(root.left)
        self.preorder(root.right)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.ans = []
        self.preorder(root)
        return self.ans    