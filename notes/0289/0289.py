class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                cur_lives = 0
                cur = board[i][j] & 1
                for x in range(max(0, i-1), min(m, i+2)):
                    for y in range(max(0, j-1), min(n, j+2)):
                        cur_lives += (board[x][y] & 1)
                if cur_lives == 3 or cur_lives - cur == 3:
                    board[i][j] += 0b10
        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1
