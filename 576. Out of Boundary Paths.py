class Solution:
    def findPaths(self, m: int, n: int, N: int, row: int, col: int) -> int:
        @cache
        def helper(i,j,N):
            if i == m or j == n or i < 0 or j < 0 :
                return 1
            if N == 0: return 0
            return helper(i+1,j,N-1) + helper(i,j+1,N-1)+helper(i-1,j,N-1)+helper(i,j-1,N-1)
        
        return helper(row,col,N)%(10**9 + 7)