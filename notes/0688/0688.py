class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        dp0 = [[0]*N for _ in range(N)]
        dp0[r][c] = 1
        dist = ((-2, 1),(-1, 2),(1, 2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1))
        for k in range(K):
            dp1 = [[0]*N for _ in range(N)]
            for i in range(N):
                for j in range(N):
                    for x, y in dist:
                        ni, nj = i+x, j+y
                        if 0 <= ni < N and 0 <= nj < N:
                            dp1[ni][nj] += dp0[i][j]
            dp0 = dp1
        return sum([i for row in dp0 for i in row]) / 8**K
