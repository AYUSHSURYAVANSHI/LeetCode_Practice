class Solution:
    def sortPeople(self, n: List[str], h: List[int]) -> List[str]:
        d = dict(zip(h,n))
        c = []
        h.sort(reverse=True)
        for i in h:
            c.append(d[i])
        return c