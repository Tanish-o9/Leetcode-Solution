class Solution:
    def searchBST(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if root == None:
            return 0
        curr = root
        while (curr != None):
            if(curr.val == target):
                return curr
            if(target < curr.val):
                curr = curr.left
            else:
                curr = curr.right
        return None
