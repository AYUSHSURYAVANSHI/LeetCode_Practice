<<<<<<< HEAD

class Solution:
    # Helper function to perform Depth-First Search (DFS) to explore the island
    def dfs(self, grid: List[List[int]], visited: List[List[bool]], i: int, j: int):
        m, n = len(grid), len(grid[0])
        # Check boundaries and whether the cell is already visited or is water
        if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == 0 or visited[i][j]:
            return
        visited[i][j] = True # Mark the cell as visited
        # Recursively visit all 4 directions
        self.dfs(grid, visited, i+1, j)
        self.dfs(grid, visited, i-1, j)
        self.dfs(grid, visited, i, j+1)
        self.dfs(grid, visited, i, j-1)

    # Function to count the number of islands (connected groups of 1's)
    def countIslands(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        count = 0

        # Iterate through the grid to find and count each island
        for i in range(m):
            for j in range(n):
                # If we find a land cell that is not visited, start a new DFS
                if grid[i][j] == 1 and not visited[i][j]:
                    count += 1
                    self.dfs(grid, visited, i, j) # Explore the island
        return count
    
    # Function to determine the minimum number of days to disconnect the island
    def minDays(self, grid: List[List[int]]) -> int:
        # Step 1: Check if the grid is already disconnected
        if self.countIslands(grid) != 1:
            return 0
        
        m, n = len(grid), len(grid[0])

        # Step 2: Try removing one land cell
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 0 # Remove the land cell
                    # Check if removing this cell disconnects the grid
                    if self.countIslands(grid) != 1:
                        return 1
                    grid[i][j] = 1 # Restore the land cell

        # Step 3: If removing one cell isn't enough, return 2 (as it is guaranteed to be sufficient)
=======

class Solution:
    # Helper function to perform Depth-First Search (DFS) to explore the island
    def dfs(self, grid: List[List[int]], visited: List[List[bool]], i: int, j: int):
        m, n = len(grid), len(grid[0])
        # Check boundaries and whether the cell is already visited or is water
        if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == 0 or visited[i][j]:
            return
        visited[i][j] = True # Mark the cell as visited
        # Recursively visit all 4 directions
        self.dfs(grid, visited, i+1, j)
        self.dfs(grid, visited, i-1, j)
        self.dfs(grid, visited, i, j+1)
        self.dfs(grid, visited, i, j-1)

    # Function to count the number of islands (connected groups of 1's)
    def countIslands(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        count = 0

        # Iterate through the grid to find and count each island
        for i in range(m):
            for j in range(n):
                # If we find a land cell that is not visited, start a new DFS
                if grid[i][j] == 1 and not visited[i][j]:
                    count += 1
                    self.dfs(grid, visited, i, j) # Explore the island
        return count
    
    # Function to determine the minimum number of days to disconnect the island
    def minDays(self, grid: List[List[int]]) -> int:
        # Step 1: Check if the grid is already disconnected
        if self.countIslands(grid) != 1:
            return 0
        
        m, n = len(grid), len(grid[0])

        # Step 2: Try removing one land cell
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 0 # Remove the land cell
                    # Check if removing this cell disconnects the grid
                    if self.countIslands(grid) != 1:
                        return 1
                    grid[i][j] = 1 # Restore the land cell

        # Step 3: If removing one cell isn't enough, return 2 (as it is guaranteed to be sufficient)
>>>>>>> 53cbd46aa08ed51a116a277d334efcc0225e7e90
        return 2