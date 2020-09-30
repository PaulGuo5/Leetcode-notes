class Solution:
    def numIslands1(self, grid: List[List[str]]) -> int:
        visited = [[0]*len(grid[0]) for i in range(len(grid))]
        def helper(grid, i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == "0" or visited[i][j] == 1:
                return
            visited[i][j] = 1
            helper(grid, i-1, j)
            helper(grid, i+1, j)
            helper(grid, i, j-1)
            helper(grid, i, j+1)
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and visited[i][j] == 0:
                    helper(grid, i, j)
                    count += 1
        return count
    
    
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        
        def dfs(grid, i, j, m, n):
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == "0":
                return
            grid[i][j] = "0"
            dfs(grid, i-1, j, m, n)
            dfs(grid, i+1, j, m, n)
            dfs(grid, i, j-1, m, n)
            dfs(grid, i, j+1, m, n)
            
        
        m, n = len(grid), len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    res += 1
                    dfs(grid, i, j, m, n)
        return res
