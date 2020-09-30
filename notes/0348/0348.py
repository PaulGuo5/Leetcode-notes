class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.n = n
        self.grid = [[None]*n for _ in range(n)]
        
    def check(self, flag, row, col):
        sum_row = sum([self.grid[row][i] == flag for i in range(self.n)])
        sum_col = sum([self.grid[i][col] == flag for i in range(self.n)])
        sum_r_l = sum([self.grid[i][self.n-1-i] == flag for i in range(self.n)])
        sum_l_r = sum([self.grid[i][i] == flag for i in range(self.n)])
        if sum_row == self.n or sum_col == self.n or sum_r_l == self.n or sum_l_r == self.n:
            return 1 if flag == 'X' else 2
        return 0
    
    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        flag = "X" if player == 1 else "O"
        self.grid[row][col] = flag
        return self.check(flag, row, col) 

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
