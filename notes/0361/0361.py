class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        m, n = len(grid), len(grid[0])
        up = [[0]*n for _ in range(m)]
        down = [[0]*n for _ in range(m)]
        left = [[0]*n for _ in range(m)]
        right = [[0]*n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "W":
                    up[i][j] = 0
                else:
                    up[i][j] = 1 if grid[i][j] == "E" else 0
                    if i - 1 >= 0:
                        up[i][j] += up[i-1][j]
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "W":
                    left[i][j] = 0
                else:
                    left[i][j] = 1 if grid[i][j] == "E" else 0
                    if j - 1 >= 0:
                        left[i][j] += left[i][j-1]
                        
        for i in range(m-1, -1, -1):
            for j in range(n):
                if grid[i][j] == "W":
                    down[i][j] = 0
                else:
                    down[i][j] = 1 if grid[i][j] == "E" else 0
                    if i + 1 < m:
                        down[i][j] += down[i+1][j]
        
        for i in range(m):
            for j in range(n-1, -1, -1):
                if grid[i][j] == "W":
                    right[i][j] = 0
                else:
                    right[i][j] = 1 if grid[i][j] == "E" else 0
                    if j + 1 < n:
                        right[i][j] += right[i][j+1]
                        
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "0":
                    res = max(res, up[i][j]+down[i][j]+left[i][j]+right[i][j])
        return res
