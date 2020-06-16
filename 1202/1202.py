class UnionFind:
    def __init__(self, p):
        self.nums = [i for i in range(p)]
    
    def find(self, x):
        if self.nums[x] != x:
            self.nums[x] = self.find(self.nums[x])
        return self.nums[x]
    
    def union(self, x, y):
        xx = self.find(x)
        yy = self.find(y)
        if xx > yy:
            xx, yy = yy, xx
        self.nums[xx] = yy
        
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        uf = UnionFind(len(s))
        res = []
        table = collections.defaultdict(list)
        for p1, p2 in pairs:
            uf.union(p1, p2)
        for i in range(len(s)):
            table[uf.find(i)].append(s[i])
        for k in table.keys():
            table[k].sort(reverse = True)
        for i in range(len(s)):
            res.append(table[uf.find(i)].pop())
        return "".join(res)
