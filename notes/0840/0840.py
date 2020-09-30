class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        res = 0
        for i in range(len(grid)-2):
            for j in range(len(grid[i])-2):
                strs = grid[i][j:j+3] +  grid[i+1][j:j+3] + grid[i+2][j:j+3]
                t = set(strs)
                mx = max(t)
                mn = min(t)
                if (len(t) == 9 and mx == 9 and mn == 1):
                    diag1 = grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2]
                    diag2 = grid[i][j+2] + grid[i+1][j+1] + grid[i+2][j]
                    row1 = grid[i][j] + grid[i][j+1] + grid[i][j+2]
                    row2 = grid[i+1][j] + grid[i+1][j+1] + grid[i+1][j+2]
                    row3 = grid[i+2][j] + grid[i+2][j+1] + grid[i+2][j+2]
                    col1 = grid[i][j] + grid[i+1][j] + grid[i+2][j]
                    col2 = grid[i][j+1] + grid[i+1][j+1] + grid[i+2][j+1]
                    col3 = grid[i][j+2] + grid[i+1][j+2] + grid[i+2][j+2]
                    if (diag1 == diag2 and diag2 == row1 and row1 == row2 and row2 == row3 and row3 == col1 and col1 == col2 and col2 == col3):
                        res += 1
        return res