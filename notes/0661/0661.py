class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        r, c = len(M), len(M[0])
        res = [[None]*c for i in range(r)]
        for i in range(r):
            for j in range(c):
                tmp = [M[i+x][j+y] for x, y in ((0,0),(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,1),(1,-1))
                      if 0 <= i+x < r and 0 <= j+y < c]
                res[i][j] = sum(tmp)//len(tmp)
        return res
