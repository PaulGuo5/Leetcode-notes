class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]: return 0
        m, n = len(grid), len(grid[0])
        memo = {}
        return max(0, self.helper(m-1, n-1, m-1, grid, m, n, memo))
    
    def helper(self, i1, j1, i2, grid, m, n, memo):
        if (i1,j1,i2) in memo: return memo[(i1,j1,i2)]
        j2 = i1+j1-i2
        if not 0<=i1<m or not 0<=i2<m or not 0<=j1<n or not 0<=j2<n or grid[i1][j1]==-1 or grid[i2][j2]==-1:
            memo[(i1,j1,i2)] = -1
            return -1
        if i1==j1==i2==0:
            cherries = 0
        else:
            cherries = max(self.helper(i1-1, j1, i2-1, grid, m, n, memo), self.helper(i1-1, j1, i2, grid, m, n, memo), self.helper(i1, j1-1, i2-1, grid, m, n, memo), self.helper(i1, j1-1, i2, grid, m, n, memo))
        if cherries == -1:
            memo[(i1,j1,i2)] = -1
            return -1
        cherries += grid[i1][j1] + grid[i2][j2]
        if i1 == i2 and j1 == j2 and grid[i1][j1] == 1:
            cherries -= 1
        memo[(i1,j1,i2)] = cherries
        return cherries
        
