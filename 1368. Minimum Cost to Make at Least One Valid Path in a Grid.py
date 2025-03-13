class Solution(object):
    def minCost(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        # Initialize the minCost matrix with a large value
        minCost = [[float('inf')] * n for _ in range(m)]
        minCost[0][0] = 0
        
        # Deque for 0-1 BFS
        dque = deque([(0, 0)])
        
        # Directions: right, left, down, up
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while dque:
            r, c = dque.popleft()
            
            # Visit adjacent cells
            for i, (dr, dc) in enumerate(directions):
                nr, nc = r + dr, c + dc
                cost = 1 if grid[r][c] != i + 1 else 0
                
                if 0 <= nr < m and 0 <= nc < n and minCost[r][c] + cost < minCost[nr][nc]:
                    minCost[nr][nc] = minCost[r][c] + cost
                    
                    # Add to deque based on cost
                    if cost == 1:
                        dque.append((nr, nc))
                    else:
                        dque.appendleft((nr, nc))
        
        # Return the minimum cost to reach the bottom-right corner
        return minCost[m - 1][n - 1]
        