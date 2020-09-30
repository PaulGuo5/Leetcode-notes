class UF:
    def __init__(self, p):
        self.nums = [i for i in range(p)]
        
    def find(self, x):
        if self.nums[x] != x: self.nums[x] = self.find(self.nums[x])
        return self.nums[x]
    
    def union(self, x, y):
        xx = self.find(x)
        yy = self.find(y)
        if xx != yy:
            self.nums[xx] = yy
    
class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        uf = UF(n*n*4)
        for i in range(n):
            for j in range(n):
                index = 4*(i*n + j)
                if grid[i][j] == "/":
                    uf.union(0+index, 3+index)
                    uf.union(1+index, 2+index)
                elif grid[i][j] == "\\":
                    uf.union(0+index, 1+index)
                    uf.union(2+index, 3+index)
                else:
                    uf.union(0+index, 3+index)
                    uf.union(1+index, 2+index)
                    uf.union(1+index, 3+index)
                if i < n-1: uf.union(2+index, 0+index+4*n)
                if j < n-1: uf.union(1+index, 3+index+4)
        
        res = 0
        for i in range(4*n*n):
            if uf.find(i) == i:
                res += 1
        return res
