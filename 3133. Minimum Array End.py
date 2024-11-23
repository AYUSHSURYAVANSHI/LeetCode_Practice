<<<<<<< HEAD
class Solution:
    def minEnd(self, n: int, x: int) -> int:
        res = 0
        q = n-1<<1
        for i in range(50):
            if 1<<i&x:
                res += 1<<i
            else:
                q >>= 1
                res += q%2<<i
        
=======
class Solution:
    def minEnd(self, n: int, x: int) -> int:
        res = 0
        q = n-1<<1
        for i in range(50):
            if 1<<i&x:
                res += 1<<i
            else:
                q >>= 1
                res += q%2<<i
        
>>>>>>> d6f8e7f5bf95ec30dd893de1512f2b076cbb6786
        return res