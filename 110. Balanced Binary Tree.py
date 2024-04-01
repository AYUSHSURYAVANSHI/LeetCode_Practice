# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self, node: Optional[TreeNode]) -> bool:
        if not node:
            return 0
        
        lh = self.height(node.left)
        if lh == -1:
            return -1
        
        rh = self.height(node.right)
        if rh == -1:
            return -1
        
        if abs(lh - rh) > 1:
            return -1
        
        return max(lh, rh) + 1
    
    def isBalanced(self, root):
        return self.height(root) != -1