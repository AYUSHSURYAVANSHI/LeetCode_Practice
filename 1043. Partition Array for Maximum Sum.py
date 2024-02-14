class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            maximum = 0
            max_sum = 0
            for j in range(1, k + 1):
                if i - j >= 0:
                    maximum = max(maximum, arr[i - j])
                    max_sum = max(max_sum, dp[i - j] + maximum * j)
            dp[i] = max_sum

        return dp[n]