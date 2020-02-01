class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        n = len(points)
        nx = set([x for x,y in points])
        ny = set([y for x,y in points])
        if nx == n or ny == n: return 0
        p = collections.defaultdict(list)
        for x, y in points:
            if nx > ny:
                p[x].append(y)
            else:
                p[y].append(x)
        
        lastx = {}
        res = float('inf')
        for x in sorted(p):
            p[x].sort()
            for i in range(len(p[x])):
                for j in range(i):
                    y1, y2 = p[x][i], p[x][j]
                    if (y1, y2) in lastx:
                        res = min(res, (x-lastx[y1,y2])*(y1-y2))
                    lastx[y1,y2] = x
        return res if res != float('inf') else 0
