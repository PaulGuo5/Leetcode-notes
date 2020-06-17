class UF:
    def __init__(self, p, connections):
        self.parents = [i for i in range(p)]
        self.length = {}
    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    def union(self, x, y):
        xx = self.find(x)
        yy = self.find(y)
        if xx < yy:
            self.parents[yy] = xx
        else:
            self.parents[xx] = yy
            
class Solution:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        uf = UF(N, connections)
        res = 0
        for x, y, cost in sorted(connections, key=lambda x: x[2]):
            if uf.find(x-1) != uf.find(y-1):
                uf.union(x-1, y-1)
                res += cost
        return res if len(set(uf.find(i) for i in uf.parents)) <= 1 else -1
