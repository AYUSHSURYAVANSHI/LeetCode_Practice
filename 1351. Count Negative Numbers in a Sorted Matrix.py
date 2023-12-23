<<<<<<< HEAD
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
=======
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
>>>>>>> 1d9420b076e7346079e9d42c8776d2fbfb052808
        return  sum(a<0 for i in grid for a in i)