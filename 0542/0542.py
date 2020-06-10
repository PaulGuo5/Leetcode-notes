class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        new = [[0]*n for _ in range(m)]
        
        def bfs(i,j):
            q = collections.deque([(i,j,0)])
            while q:
                ni, nj, dis = q.popleft()
                if 0 <= ni < m and 0 <= nj < n:
                    if matrix[ni][nj] == 0:
                        return dis
                    q.append((ni+1, nj, dis+1))
                    q.append((ni-1, nj, dis+1))
                    q.append((ni, nj+1, dis+1))
                    q.append((ni, nj-1, dis+1))
            
            return
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    new[i][j] = bfs(i, j)
        return new
