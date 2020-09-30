class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        top = [a[:] for a in grid]
        left = [a[:] for a in grid]
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    if i:
                        top[i][j] = top[i-1][j] + 1
                    if j:
                        left[i][j] = left[i][j-1] + 1
        for s in range(min(m,n), 0, -1):
            for i in range(m-s+1):
                for j in range(n-s+1):
                    if min(top[i+s-1][j], top[i+s-1][j+s-1], left[i][j+s-1], left[i+s-1][j+s-1]) >= s:
                        return s*s
        return 0
