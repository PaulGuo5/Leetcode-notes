class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        clear_row = set()
        clear_col = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    clear_row.add(i)
                    clear_col.add(j)
        for i in range(m):
            if i in clear_row:
                for j in range(n):
                    matrix[i][j] = 0
        for j in range(n):
            if j in clear_col:
                for i in range(m):
                    matrix[i][j] = 0
