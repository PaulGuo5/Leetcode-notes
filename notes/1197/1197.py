class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        if x == 0 and y == 0: return 0
        distances = [(2,1),(1,2),(-2,1),(2,-1),(-2,-1),(-1,2),(1,-2),(-1,-2)]
        q = collections.deque([(0,0,0)])
        visited = set((0,0))
        while q:
            bx, by, dis = q.popleft()
            for d in distances:
                xx, yy = bx+d[0], by+d[1]
                if xx == x and yy == y: return dis+1
                if (xx,yy) not in visited and abs(xx)+abs(yy)<=300:
                    q.append((xx,yy,dis+1))
                    visited.add((xx,yy))
        return None
