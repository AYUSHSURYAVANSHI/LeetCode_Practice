class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        n = len(mat)
        m = len(mat[0])
        ans = 0
        num = list(zip(*mat))
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1 and sum(mat[i]) == 1 and sum(num[j]) == 1:
                    ans += 1
        return ans 