class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        N = len(grid)

        def move(x, y):
            res = []
            for i, j in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                if 0 <= x + i < N and 0 <= y + j < N:
                    res.append((x + i, y + j))
            return res

        def dfs(x, y, index):
            nonlocal area
            grid[x][y] = index
            area += 1
            for i, j in move(x, y):
                if grid[i][j] == 1:
                    dfs(i, j, index)

        # DFS every island and give it an index of island
        index = 2
        areas = {0: 0}
        for x in range(N):
            for y in range(N):
                if grid[x][y] == 1:
                    area = 0
                    dfs(x, y, index)
                    areas[index] = area
                    index += 1

        # traverse every 0 cell and count biggest island it can conntect
        res = max(areas.values())
        for x in range(N):
            for y in range(N):
                if grid[x][y] == 0:
                    possible = set(grid[i][j] for i, j in move(x, y))
                    res = max(res, sum(areas[index] for index in possible) + 1)
        return res
