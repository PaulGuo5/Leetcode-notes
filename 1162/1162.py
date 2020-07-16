class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        res = -float('inf')
        m, n = len(grid), len(grid[0])
        dist = ((0,1),(0,-1),(1,0),(-1,0))
        q = collections.deque()
        vis = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((i,j,i,j))
        while q:
            ii, jj, ori_i, ori_j = q.popleft()
            if (ii, jj) not in vis:
                vis.add((ii,jj))
                if (ii,jj) != (ori_i, ori_j):
                    res = max(res, abs(ii-ori_i)+abs(jj-ori_j))
                for x, y in dist:
                    newR, newC = ii+x, jj+y
                    if 0 <= newR < m and 0 <= newC < n:
                        q.append((newR, newC, ori_i, ori_j))
            
        return res if res > -float('inf') else -1
    
    
