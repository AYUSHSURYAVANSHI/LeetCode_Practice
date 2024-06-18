class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        infos = sorted(zip(difficulty, profit))
        max_profit_for_difficulty = []
        max_profit = 0
        for d, p in infos:
            max_profit = max(max_profit, p)
            max_profit_for_difficulty.append((d, max_profit))
        
        total_profit = 0
        for w in worker:
            index = self.binary_search(max_profit_for_difficulty, w)
            if index >= 0 and w >= max_profit_for_difficulty[index][0]:
                total_profit += max_profit_for_difficulty[index][1]
        return total_profit
    
    def binary_search(self, max_profit_for_difficulty: List[Tuple[int, int]], target: int) -> int:
        left, right = 0, len(max_profit_for_difficulty) - 1
        while left <= right:
            mid = (left + right) // 2
            if max_profit_for_difficulty[mid][0] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return right