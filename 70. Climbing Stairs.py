class Solution:
    def climbStairs(self, n: int) -> int:
        n1 , n2 = 1, 2
        if n == 1 or n == 2:
            return n 
        for i in range(2,n):
            n3 = n1+n2
            n1 , n2 = n2, n3
        return n3
        