<<<<<<< HEAD
class Solution:
    def solve(self, root):
        if not root:
            return
        
        q = deque()
        cpy = deque()
        level_sum = []
        level = 0
        
        level_sum.append(root.val)
        q.append((level, (root, root.val)))
        cpy.append((level, (root, root.val)))

        while q:
            n = len(q)
            lvl_sum = 0

            for _ in range(n):
                node, _ = q.popleft()[1]
                sib_sum = 0

                if node.left:
                    sib_sum += node.left.val
                if node.right:
                    sib_sum += node.right.val

                if node.left:
                    q.append((level + 1, (node.left, sib_sum)))
                    cpy.append((level + 1, (node.left, sib_sum)))

                if node.right:
                    q.append((level + 1, (node.right, sib_sum)))
                    cpy.append((level + 1, (node.right, sib_sum)))

                lvl_sum += sib_sum
            
            level_sum.append(lvl_sum)
            level += 1

        while cpy:
            lvl, (node, sib_sum) = cpy.popleft()
            node.val = level_sum[lvl] - sib_sum

    def replaceValueInTree(self, root):
        self.solve(root)
=======
class Solution:
    def solve(self, root):
        if not root:
            return
        
        q = deque()
        cpy = deque()
        level_sum = []
        level = 0
        
        level_sum.append(root.val)
        q.append((level, (root, root.val)))
        cpy.append((level, (root, root.val)))

        while q:
            n = len(q)
            lvl_sum = 0

            for _ in range(n):
                node, _ = q.popleft()[1]
                sib_sum = 0

                if node.left:
                    sib_sum += node.left.val
                if node.right:
                    sib_sum += node.right.val

                if node.left:
                    q.append((level + 1, (node.left, sib_sum)))
                    cpy.append((level + 1, (node.left, sib_sum)))

                if node.right:
                    q.append((level + 1, (node.right, sib_sum)))
                    cpy.append((level + 1, (node.right, sib_sum)))

                lvl_sum += sib_sum
            
            level_sum.append(lvl_sum)
            level += 1

        while cpy:
            lvl, (node, sib_sum) = cpy.popleft()
            node.val = level_sum[lvl] - sib_sum

    def replaceValueInTree(self, root):
        self.solve(root)
>>>>>>> d6f8e7f5bf95ec30dd893de1512f2b076cbb6786
        return root