class Solution:
    @cache
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        if target <= 0:
            return 0
        if n == 1:
            return 1 if target <= k else 0
        return sum(self.numRollsToTarget(n - 1, k, target - d) for d in range(1, k + 1)) % (10 ** 9 + 7)