<<<<<<< HEAD
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.result = 0
        def dfs(node):
            if not node:
                return []
            if not node.left and not node.right:
                return [1]
            left = dfs(node.left)
            right = dfs(node.right)
            for l in left:
                for r in right:
                    if l + r <= distance:
                        self.result += 1

            merged = [i+1 for i in left+right if i+1 < distance]
            return merged
        
        dfs(root)
=======
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.result = 0
        def dfs(node):
            if not node:
                return []
            if not node.left and not node.right:
                return [1]
            left = dfs(node.left)
            right = dfs(node.right)
            for l in left:
                for r in right:
                    if l + r <= distance:
                        self.result += 1

            merged = [i+1 for i in left+right if i+1 < distance]
            return merged
        
        dfs(root)
>>>>>>> b3467e64c7467582cda42326c1bb2f9cec23f9a3
        return self.result