<<<<<<< HEAD
class Solution:
    def passThePillow(self, n: int, time: int) -> int:
=======
class Solution:
    def passThePillow(self, n: int, time: int) -> int:
>>>>>>> b3467e64c7467582cda42326c1bb2f9cec23f9a3
        return n - abs(n - 1 - time % (n * 2 - 2)) 