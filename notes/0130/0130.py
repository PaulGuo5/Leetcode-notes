class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board: return None
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if i in {0, m-1} or j in {0, n-1} and board[i][j] == "O":
                    self.dfs(board, i, j)
                    
        for i in range(m):
            for j in range(n):
                if board[i][j] == "D":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"
            
    def dfs(self, board, i, j):
        if not 0<=i<len(board) or not 0<=j<len(board[0]) or board[i][j]!="O":
            return 
        board[i][j] = 'D'
        self.dfs(board, i+1,j)
        self.dfs(board, i-1,j)
        self.dfs(board, i,j+1)
        self.dfs(board, i,j-1)
        
            
