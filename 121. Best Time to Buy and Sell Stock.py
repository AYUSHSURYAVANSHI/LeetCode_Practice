class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minV = 1e9

        for i in range(len(prices)):
           minV = min(minV,prices[i])
           profit = max(profit,prices[i]- minV)
           
        return profit