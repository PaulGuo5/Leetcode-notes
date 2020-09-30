class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        def win(flag):
            for i in board:
                if i[0] == i[1] == i[2] == flag: return True
            for i in range(3):
                if board[0][i] == board[1][i] == board[2][i] == flag: return True
            if board[0][0] == board[1][1] == board[2][2] == flag: return True
            if board[0][2] == board[1][1] == board[2][0] == flag: return True
            return False
        
        c = collections.Counter(''.join(board))
        xc, oc = c['X'], c['O']
        if xc < oc or xc > oc + 1: return False
        if win('X') and xc-1 != oc: return False
        if win('O') and xc != oc: return False
        return True
