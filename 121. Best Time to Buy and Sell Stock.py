<<<<<<< HEAD
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minV = 1e9

        for i in range(len(prices)):
           minV = min(minV,prices[i])
           profit = max(profit,prices[i]- minV)
           
=======
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minV = 1e9

        for i in range(len(prices)):
           minV = min(minV,prices[i])
           profit = max(profit,prices[i]- minV)
           
>>>>>>> 1d9420b076e7346079e9d42c8776d2fbfb052808
        return profit