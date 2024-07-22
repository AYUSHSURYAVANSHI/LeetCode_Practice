<<<<<<< HEAD
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
=======
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
>>>>>>> b3467e64c7467582cda42326c1bb2f9cec23f9a3
        return numBottles + (numBottles-1)//(numExchange-1)