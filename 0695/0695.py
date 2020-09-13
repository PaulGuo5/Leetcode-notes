class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        vis = set()
        
        def dfs(i, j):
            nonlocal area
            area += 1
            for xx, yy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                ni, nj = i+xx, j+yy
                if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in vis and grid[ni][nj] == 1:
                    vis.add((ni, nj))
                    dfs(ni, nj)
                    
        def bfs(i, j):
            nonlocal area
            q = collections.deque([(i, j)])
            while q:
                x, y = q.popleft()
                area += 1
                for xx, yy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    nx, ny = x+xx, y+yy
                    if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in vis and grid[nx][ny] == 1:
                        vis.add((nx, ny))
                        q.append((nx, ny))
        res = 0
        for i in range(m):
            for j in range(n):
                if (i, j) not in vis and grid[i][j] == 1:
                    vis.add((i, j))
                    area = 0
                    # dfs(i, j)
                    bfs(i, j)
                    res = max(res, area)
        return res
