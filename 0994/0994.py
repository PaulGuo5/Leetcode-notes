class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        bfs = [(x,y) for x, row in enumerate(grid) for y, val in enumerate(row) if val == 2]
        m, n = len(grid), len(grid[0])
        step = 0
        while bfs:
            tmp = []
            for x, y in bfs:
                for i, j in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                    if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
                        grid[i][j] = 2
                        tmp.append((i, j))
            bfs = tmp
            step += bool(bfs)
        return step if all(val != 1 for row in grid for val in row) else -1
