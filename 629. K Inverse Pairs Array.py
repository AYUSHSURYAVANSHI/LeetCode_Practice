<<<<<<< HEAD
class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        dp = [[0] * (k + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(k + 1):
                if j == 0:
                    dp[i][j] = 1
                else:
                    val = (dp[i - 1][j] + MOD - (dp[i - 1][j - i] if j - i >= 0 else 0)) % MOD
                    dp[i][j] = (dp[i][j - 1] + val) % MOD

=======
class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        dp = [[0] * (k + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(k + 1):
                if j == 0:
                    dp[i][j] = 1
                else:
                    val = (dp[i - 1][j] + MOD - (dp[i - 1][j - i] if j - i >= 0 else 0)) % MOD
                    dp[i][j] = (dp[i][j - 1] + val) % MOD

>>>>>>> 973c2521232a2cdb9a3c2784c3886fa4feeff66d
        return (dp[n][k] + MOD - (dp[n][k - 1] if k > 0 else 0)) % MOD