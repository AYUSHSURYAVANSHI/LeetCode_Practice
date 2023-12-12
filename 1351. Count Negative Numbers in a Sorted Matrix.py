class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        return  sum(a<0 for i in grid for a in i)