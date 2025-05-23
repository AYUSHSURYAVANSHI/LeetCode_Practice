class Solution:
    def myPow(self, x: float, n: int) -> float:
        def fastpower(x,n):
            if n == 0:
                return 1
            half = fastpower(x, n // 2)
            if n % 2 == 0:
                return half * half
            else:
                return half * half * x
            
        if n < 0:
            x = 1/x
            n = -n
        return fastpower(x,n)

