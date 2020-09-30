class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [[0]*10 for _ in range(9)]
        cols = [[0]*10 for _ in range(9)]
        boxs = [[0]*10 for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    n = int(board[i][j])
                    rows[j][n] = 1
                    cols[i][n] = 1
                    boxs[i//3*3+j//3][n] = 1
        
        def fill(board, i, j):
            if j == 9: return True
            nxt_i = (i+1) % 9
            nxt_j = j+1 if nxt_i == 0 else j
            if board[i][j] != ".": return fill(board, nxt_i, nxt_j)
            for n in range(1, 10):
                if not rows[j][n] and not cols[i][n] and not boxs[i//3*3+j//3][n]:
                    board[i][j] = str(n)
                    rows[j][n] = 1
                    cols[i][n] = 1
                    boxs[i//3*3+j//3][n] = 1
                    if fill(board, nxt_i, nxt_j): return True
                    board[i][j] = "."
                    rows[j][n] = 0
                    cols[i][n] = 0
                    boxs[i//3*3+j//3][n] = 0
            return False
        
        fill(board, 0, 0)
