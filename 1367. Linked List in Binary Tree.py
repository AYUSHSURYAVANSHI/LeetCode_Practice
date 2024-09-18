<<<<<<< HEAD
class Solution:
    def isSubPath(self, head, root):
        def checkPath(head, root):
            if not head: return True
            if not root or head.val != root.val: return False
            return checkPath(head.next, root.left) or checkPath(head.next, root.right)

        if not root: return False
        if checkPath(head, root): return True
=======
class Solution:
    def isSubPath(self, head, root):
        def checkPath(head, root):
            if not head: return True
            if not root or head.val != root.val: return False
            return checkPath(head.next, root.left) or checkPath(head.next, root.right)

        if not root: return False
        if checkPath(head, root): return True
>>>>>>> 53cbd46aa08ed51a116a277d334efcc0225e7e90
        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)