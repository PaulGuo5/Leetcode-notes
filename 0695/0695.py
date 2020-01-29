class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.area = 0
                    self.helper(grid, i, j)
                    res = max(res, self.area)
        return res
    
    def helper(self, grid, i, j):
        m, n = len(grid), len(grid[0])
        if grid[i][j] == 1:
            grid[i][j] = 0
            self.area += 1
            if i-1 >= 0: self.helper(grid,i-1,j)
            if i+1 < m: self.helper(grid,i+1,j)
            if j-1 >= 0: self.helper(grid,i,j-1)
            if j+1 < n: self.helper(grid,i,j+1)
        else:
            return 0
