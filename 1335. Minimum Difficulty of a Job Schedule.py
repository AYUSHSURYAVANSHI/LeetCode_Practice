class Solution:
    def minDifficulty(self,diff: List[int], d: int) -> int:
        n = len(diff)
        dp = [[float('inf')] * n for _ in range(d)]

        for i in range(n):
            dp[0][i] = max(diff[:i+1])

        for k in range(1, d):
            for i in range(k, n):
                curr_diff = -float('inf')
                for j in range(i, k-1, -1):
                    curr_diff = max(curr_diff, diff[j])
                    dp[k][i] = min(dp[k][i], curr_diff + dp[k-1][j-1])

        return dp[d-1][n-1] if dp[d-1][n-1] != float('inf') else -1