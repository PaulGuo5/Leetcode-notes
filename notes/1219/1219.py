class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        self.res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]>0:
                    self.dfs(grid, i, j, 0)
        return self.res
    
    def dfs(self, grid, i, j, cur):
        if 0<=i<len(grid) and 0<=j<len(grid[0]) and grid[i][j]>0:
            tmp = grid[i][j]
            grid[i][j] = 0
            self.dfs(grid, i+1, j, cur+tmp)
            self.dfs(grid, i-1, j, cur+tmp)
            self.dfs(grid, i, j+1, cur+tmp)
            self.dfs(grid, i, j-1, cur+tmp)
            grid[i][j] = tmp
            self.res = max(self.res, cur+tmp)
