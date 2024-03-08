<<<<<<< HEAD
class Solution:
    def numSquares(self, n: int) -> int:
        dp=[0]*(n+1)
        for i in range(1,n+1):
            dp[i]=i
            for j in range(1,int(math.sqrt(i))+1):
                dp[i]=min(dp[i],dp[i-j*j]+1)
=======
class Solution:
    def numSquares(self, n: int) -> int:
        dp=[0]*(n+1)
        for i in range(1,n+1):
            dp[i]=i
            for j in range(1,int(math.sqrt(i))+1):
                dp[i]=min(dp[i],dp[i-j*j]+1)
>>>>>>> 973c2521232a2cdb9a3c2784c3886fa4feeff66d
        return dp[n]