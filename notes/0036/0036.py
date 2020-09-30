class Solution:
    def isValid(self, row):
        map = {}
        for c in row:
            if c != '.':
                if c in map:
                    return False
                else:
                    map[c] = True
        return True
    
    def isValidSudoku1(self, board: List[List[str]]) -> bool:
        for i in range(9):
            if not self.isValid(board[i]): return False
            col = [c[i] for c in board]
            if not self.isValid(col): return False
        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                if not self.isValid([board[s][t] for s in [i, i+1, i+2] for t in [j, j+1, j+2]]):
                    return False
        return True
    
    
    def isValidSudoku(self, board: List[List[str]]) -> bool: 
        seen = []
        for i, row in enumerate(board):
            for j, c in enumerate(row):
                if c != '.':
                    seen += [(c,j),(i,c),(i//3,j//3,c)]
        return len(seen) == len(set(seen))
