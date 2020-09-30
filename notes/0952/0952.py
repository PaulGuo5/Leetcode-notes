class UnionFind:
    def __init__(self, p):
        self.parents = [i for i in range(p)]
    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x] 
    def union(self, x, y):
        xx = self.find(x)
        yy = self.find(y)
        self.parents[xx] = self.parents[yy]
class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        uf = UnionFind(max(A)+1)
        for a in A:
            for i in range(2, int(a**0.5)+1):
                if a % i == 0:
                    uf.union(a, i)
                    uf.union(a, a//i)
        return collections.Counter([uf.find(a) for a in A]).most_common(1)[0][1]
