class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid or grid[0][0] == 1 or grid[-1][-1] == 1: return -1
        m, n = len(grid), len(grid[0])
        q = collections.deque()
        q.append((0,0,1))
        dist = ((0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1))
        while q:
            i, j, path = q.popleft()
            if (i,j) == (m-1, n-1):
                return path
            for d in dist:
                ni, nj = i+d[0], j+d[1]
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 0:
                    grid[ni][nj] = 1
                    q.append((ni, nj, path+1))
        return -1
