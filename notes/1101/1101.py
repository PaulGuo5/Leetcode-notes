class UnionFind:
    def __init__(self, p):
        self.parents = [i for i in range(p)]
        self.groups = p
    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    def union(self, x, y):
        xx = self.find(x)
        yy = self.find(y)
        if xx != yy:
            self.parents[yy] = xx
            self.groups -= 1
class Solution:
    def earliestAcq(self, logs: List[List[int]], N: int) -> int:
        uf = UnionFind(N)
        for time, n1, n2 in sorted(logs, key=lambda x:x[0]):
            uf.union(n1, n2)
            if uf.groups == 1:
                return time
        return -1
