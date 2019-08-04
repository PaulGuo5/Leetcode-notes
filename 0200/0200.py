class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
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
