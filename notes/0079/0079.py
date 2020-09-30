class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False
        def dfs(board, word, d, i, j):
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[d]:
                return False
            if d == len(word) - 1:
                return True
            # Let the current node out
            cur = board[i][j]
            board[i][j] = 0
            found = dfs(board, word, d+1, i+1, j) or dfs(board, word, d+1, i-1, j) or dfs(board, word, d+1, i, j+1) or dfs(board, word, d+1, i, j-1)
            # retore the current value
            board[i][j] = cur
            return found
            
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if dfs(board, word, 0, i, j):
                    return True
        return False
        
