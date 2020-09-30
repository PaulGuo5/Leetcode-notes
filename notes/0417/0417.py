class Solution:
    def pacificAtlantic1(self, matrix: List[List[int]]) -> List[List[int]]:
        #dfs
        if not matrix: return None
        
        def helper(matrix, x, y, visited, prev):
            m, n = len(matrix), len(matrix[0])
            if x < 0 or x >= m or y < 0 or y >= n or (x, y) in visited or prev > matrix[x][y]: return
            dists = ((1,0),(-1,0),(0,1),(0,-1))
            visited.add((x,y))
            for d in dists:
                helper(matrix, x+d[0], y+d[1], visited, matrix[x][y])
                
        m, n = len(matrix), len(matrix[0])
        p, a = set(), set()
        for i in range(m):
            helper(matrix, i, 0, p, -1)
            helper(matrix, i, n-1, a, -1)
        for j in range(n):
            helper(matrix, 0, j, p, -1)
            helper(matrix, m-1, j, a, -1)
        return p&a
    
    
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        # bfs
        if not matrix: return None
        m, n = len(matrix), len(matrix[0])
        p = set([(i, 0) for i in range(m)]+[(0, i) for i in range(n)])
        a = set([(i, n-1) for i in range(m)]+[(m-1,i) for i in range(n)])
        
        def helper(ocean):
            q = collections.deque(ocean)
            while q:
                x, y = q.popleft()
                dists = ((1,0),(-1,0),(0,1),(0,-1))
                for d in dists:
                    xx, yy = d[0]+x, d[1]+y
                    if 0<=xx<m and 0<=yy<n and (xx,yy) not in ocean and matrix[xx][yy] >= matrix[x][y]:
                        q.append((xx,yy))
                        ocean.add((xx,yy))
            return ocean
        
        return helper(p)&helper(a)
