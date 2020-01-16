class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        seen = set()
        def helper(i, j, di=0):
            if 0<=i<len(grid) and 0<=j<len(grid[0]) and grid[i][j] and (i,j) not in seen:
                seen.add((i,j))
                shape.append(di)
                
                helper(i+1, j, di+1)
                helper(i-1, j, di+2)
                helper(i, j+1, di+3)
                helper(i, j-1, di+4)
                shape.append(0)
        
        shapes = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                shape = []
                helper(i, j)
                if shape:
                    shapes.add(tuple(shape))
        return len(shapes)
