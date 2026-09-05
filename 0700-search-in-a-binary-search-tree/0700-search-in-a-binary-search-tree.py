# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
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
