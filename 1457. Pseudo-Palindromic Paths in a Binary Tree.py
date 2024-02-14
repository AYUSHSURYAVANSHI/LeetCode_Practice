# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        def dfs(node, s):
            if not node:
                return

            nonlocal count
            if node.val in s:
                s.remove(node.val)
            else:
                s.add(node.val)

            if not node.left and not node.right:
                if len(s) < 2:
                    count += 1
            else :
                dfs(node.left, s)
                dfs(node.right, s)
            
            if node.val in s:
                s.remove(node.val)
            else:
                s.add(node.val)

        count = 0
        dfs(root, set())
        return count
