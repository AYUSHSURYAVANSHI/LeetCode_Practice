class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        p, n = [x for x in nums if x > 0], [x for x in nums if x < 0]
        a = []
        for i in range(len(p)):
            a.append(p[i])
            a.append(n[i])
        return a 