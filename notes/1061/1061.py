class UF:
    def __init__(self, p):
        self.par = [i for i in range(p)]
    def find(self, x):
        if self.par[x] != x: self.par[x] = self.find(self.par[x])
        return self.par[x]
    def union(self, x, y):
        xx = self.find(x)
        yy = self.find(y)
        if xx < yy:
            self.par[yy] = xx
        else:
            self.par[xx] = yy
            
class Solution:
    def smallestEquivalentString(self, A: str, B: str, S: str) -> str:
        words = set()
        for c in A:
            words.add(c)
        for c in B:
            words.add(c)
        table = {}
        ind2word = {}
        for i, c in enumerate(sorted(list(words))):
            table[c] = i
            ind2word[i] = c
        uf = UF(len(table))
        for c1, c2 in zip(A, B):
            uf.union(table[c1], table[c2])
        res = ""
        for c in S:
            if c not in table:
                res += c
            else:
                res += ind2word[uf.find(table[c])]
        return res
