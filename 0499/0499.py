class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        m, n = len(maze), len(maze[0])
        q = [(0, ball[0], ball[1], "")]
        heapq.heapify(q)
        vis = set()
        res = []
        dirs = ((1, 0, "d"), (0, -1, "l"), (0, 1, "r"), (-1, 0, "u"))
        
        while q:
            steps, x, y, path = heapq.heappop(q)
            if x == hole[0] and y == hole[1]:
                res.append((steps, path))
            if (x, y) not in vis:
                vis.add((x, y))
                for d1, d2, d in dirs:
                    tmp_steps = steps
                    nx, ny = x, y
                    while 0 <= nx+d1 < m and 0 <= ny+d2 < n and maze[nx+d1][ny+d2] == 0:
                        nx += d1
                        ny += d2
                        tmp_steps += 1
                        if nx == hole[0] and ny == hole[1]:
                            break
                    heapq.heappush(q, (tmp_steps, nx, ny, path+d))
        
        return min(res, key = lambda x:(x[0], x[1]))[1] if res else "impossible"
