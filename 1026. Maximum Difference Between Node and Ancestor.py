# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ret = [0]
        def rec(node, minv, maxv):
            if not node:
                return
            ret[0] = max(abs(node.val - minv), abs(node.val -maxv), ret[0])
            rec(node.left, min(minv, node.val), max(node.val, maxv))
            rec(node.right, min(minv, node.val), max(node.val, maxv))
        
        rec(root.left, root.val, root.val)
        rec(root.right, root.val, root.val)

        return ret[0] 