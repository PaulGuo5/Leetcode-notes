class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def check(depth, col):
            for row in range(depth):
                if board[row] == col or abs(board[row]-col) == abs(row-depth):
                    return False
            return True
        
        def dfs(depth, tmp):
            if depth == n:
                res.append(tmp)
                return 
            else:
                for col in range(n):
                    if check(depth, col):
                        board[depth] = col
                        s = "."*n
                        dfs(depth+1, tmp+[s[:col]+"Q"+s[col+1:]])
        res = []
        board = [-1 for _ in range(n)]
        dfs(0, [])
        return res
