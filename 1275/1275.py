class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        grid = [[0]*3 for _ in range(3)]
        step = 0
        for move in moves:
            grid[move[0]][move[1]] = 1 if not step%2 else -1
            step += 1
        for j in range(3):
            if sum([grid[j][i] for i in range(3)]) == 3: return "A"
            if sum([grid[j][i] for i in range(3)]) == -3: return "B"
            if sum([grid[i][j] for i in range(3)]) == 3: return "A"
            if sum([grid[i][j] for i in range(3)]) == -3: return "B"
        if sum([grid[i][i] for i in range(3)]) == 3: return "A"
        if sum([grid[i][i] for i in range(3)]) == -3: return "B"
        if sum([grid[i][2-i] for i in range(3)]) == 3: return "A"
        if sum([grid[i][2-i] for i in range(3)]) == -3: return "B"
        if len(moves) == 9: return "Draw"
        if len(moves) < 9: return "Pending"
