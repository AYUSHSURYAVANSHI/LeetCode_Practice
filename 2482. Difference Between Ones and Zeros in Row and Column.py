class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m , n = len(grid) , len(grid[0])

        row = [0]*m
        col = [0]*n

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    row[i] += 1
                    col[j] += 1
                elif grid[i][j] == 0:
                    row[i] -= 1
                    col[j] -= 1
        
        for i in range(m):
            for j in range(n):
                grid[i][j] = row[i] + col[j]
            
        return grid 