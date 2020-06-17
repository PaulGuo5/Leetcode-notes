class UnionFind:
    def __init__(self, p):
        self.parents = [i for i in range(p)]
    def find(self, x):
        if self.parents[x] != x: self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    def union(self, x, y):
        xx = self.find(x)
        yy = self.find(y)
        if xx != yy: self.parents[xx] = yy
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        var = {}
        i = 0
        for e in equations:
            if e[0] not in var:
                var[e[0]] = i
                i += 1
            if e[3] not in var:
                var[e[3]] = i
                i += 1
        uf = UnionFind(len(var))
        notequals = []
        for e in equations:
            if e[1] == "!":
                notequals.append(e)
            else:
                if uf.find(var[e[0]]) != uf.find(var[e[3]]):
                    uf.union(var[e[0]], var[e[3]])
        for e in notequals:
            if uf.find(var[e[0]]) == uf.find(var[e[3]]):
                return False
        return True
