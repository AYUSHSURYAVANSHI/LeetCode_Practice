class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])
        dp = [0] * n

        # Initialize dp with the first row
        for j in range(n):
            dp[j] = points[0][j]

        # Traverse through each row
        for i in range(1, m):
            leftMax = [0] * n
            rightMax = [0] * n
            newDp = [0] * n

            # Calculate left max
            leftMax[0] = dp[0]
            for j in range(1, n):
                leftMax[j] = max(leftMax[j - 1], dp[j] + j)

            # Calculate right max
            rightMax[n - 1] = dp[n - 1] - (n - 1)
            for j in range(n - 2, -1, -1):
                rightMax[j] = max(rightMax[j + 1], dp[j] - j)

            # Calculate new DP for the current row
            for j in range(n):
                newDp[j] = max(leftMax[j] - j, rightMax[j] + j) + points[i][j]

            dp = newDp

        return max(dp)