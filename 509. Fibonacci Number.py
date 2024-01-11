class Solution:
    def fib(self, n: int) -> int:
        curr = 0
        next = 1
        if n == 0:
            return curr
        elif n == 1:
            return next
        else:
            for i in range(2,n+1):
                sum = next + curr
                curr = next
                next = sum 
            return next