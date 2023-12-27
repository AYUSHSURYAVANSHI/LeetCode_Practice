class Solution:
    def minCost(self, c: str,t: List[int]) -> int:
        return sum(t) - sum(max(g)[1] for _,g in groupby(zip(c,t), key=lambda x:x[0]))
        