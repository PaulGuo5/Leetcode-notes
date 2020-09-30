class Solution:
    def hasPath11(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        #dfs
        m, n = len(maze), len(maze[0])
        visited = set()
        def dfs(i, j):
            if (i,j) in visited: return False
            visited.add((i, j))
            if i == destination[0] and j == destination[1]: return True
            for x, y in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                nx, ny = i, j
                while 0<=nx+x<m and 0<=ny+y<n and maze[nx+x][ny+y] != 1:
                    nx += x
                    ny += y
                if dfs(nx, ny): return True
            return False
        return dfs(*start)
    
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        #bfs
        m, n = len(maze), len(maze[0])
        visited = set()
        q = collections.deque([(start[0], start[1])])
        
        while q:
            i, j = q.popleft()
            if i == destination[0] and j == destination[1]: return True
            if (i, j) in visited: continue
            visited.add((i, j))
            for x, y in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                nx, ny = i, j
                while 0<=nx+x<m and 0<=ny+y<n and maze[nx+x][ny+y] != 1:
                    nx += x
                    ny += y
                q.append((nx, ny))
        return False
