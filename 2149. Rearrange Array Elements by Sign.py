<<<<<<< HEAD
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        p, n = [x for x in nums if x > 0], [x for x in nums if x < 0]
        a = []
        for i in range(len(p)):
            a.append(p[i])
            a.append(n[i])
=======
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        p, n = [x for x in nums if x > 0], [x for x in nums if x < 0]
        a = []
        for i in range(len(p)):
            a.append(p[i])
            a.append(n[i])
>>>>>>> 973c2521232a2cdb9a3c2784c3886fa4feeff66d
        return a 