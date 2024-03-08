<<<<<<< HEAD
class Solution:
    def sortPeople(self, n: List[str], h: List[int]) -> List[str]:
        d = dict(zip(h,n))
        c = []
        h.sort(reverse=True)
        for i in h:
            c.append(d[i])
=======
class Solution:
    def sortPeople(self, n: List[str], h: List[int]) -> List[str]:
        d = dict(zip(h,n))
        c = []
        h.sort(reverse=True)
        for i in h:
            c.append(d[i])
>>>>>>> 973c2521232a2cdb9a3c2784c3886fa4feeff66d
        return c