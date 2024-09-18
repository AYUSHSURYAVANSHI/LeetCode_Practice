<<<<<<< HEAD

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def pot(root):
            if root:
                pot(root.left)
                pot(root.right)
                res.append(root.val)
        pot(root)
=======

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def pot(root):
            if root:
                pot(root.left)
                pot(root.right)
                res.append(root.val)
        pot(root)
>>>>>>> 53cbd46aa08ed51a116a277d334efcc0225e7e90
        return res