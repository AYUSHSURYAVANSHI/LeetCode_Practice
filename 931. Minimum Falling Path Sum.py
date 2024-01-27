class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        for row in range(1,len(matrix)):
            for col in range(len(matrix)):
                matrix[row][col] = matrix[row][col]+min([matrix[row-1][c+col] if (0<=c+col<len(matrix)) else 10001 for c in range(-1,2)])
        return min(matrix[-1])