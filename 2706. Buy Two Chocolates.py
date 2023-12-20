class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        return money if money<(x:=sum(heapq.nsmallest(2,prices))) else money-x