<<<<<<< HEAD
class Solution:
    def pivotInteger(self, n: int) -> int:
        x = sqrt(n * (n + 1) / 2)
        
        if x % 1 != 0:
            return -1
        else:
=======
class Solution:
    def pivotInteger(self, n: int) -> int:
        x = sqrt(n * (n + 1) / 2)
        
        if x % 1 != 0:
            return -1
        else:
>>>>>>> 6565d284220dea1aa3de84faf61b1150f2d66938
            return int(x)