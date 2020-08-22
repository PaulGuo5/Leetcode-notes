class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        # bfs
        m, n = len(maze), len(maze[0])
        q = [(0, start[0], start[1])]
        heapq.heapify(q)
        vis = set()
        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
        
        while q:
            steps, x, y = heapq.heappop(q)
            if x == destination[0] and y == destination[1]:
                return steps
            if (x, y) not in vis:
                vis.add((x, y))
                for d in dirs:
                    nx, ny, tmp_steps = x, y, steps
                    while 0 <= nx+d[0] < m and 0 <= ny+d[1] < n and maze[nx+d[0]][ny+d[1]] == 0:
                        nx += d[0]
                        ny += d[1]
                        tmp_steps += 1
                    heapq.heappush(q, (tmp_steps, nx, ny))
        return -1
    
    
    def shortestDistance1(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        # dfs LTE
        m, n = len(maze), len(maze[0])
        vis = set()
        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
        res = []
        
        def dfs(x, y, steps):
            if x == destination[0] and y == destination[1]:
                res.append(steps)
                return 
            if (x, y) not in vis:
                vis.add((x, y))
                for d in dirs:
                    nx, ny, tmp_steps = x, y, steps
                    while 0 <= nx+d[0] < m and 0 <= ny+d[1] < n and maze[nx+d[0]][ny+d[1]] == 0:
                        nx += d[0]
                        ny += d[1]
                        tmp_steps += 1
                    dfs(nx, ny, tmp_steps)
                vis.remove((x, y))
        
        dfs(start[0], start[1], 0)
        return min(res) if res else -1
