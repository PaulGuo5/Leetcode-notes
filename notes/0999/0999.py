class Solution:
    def numRookCaptures1(self, board: List[List[str]]) -> int:
        m, n = len(board), len(board[0])
        for x, row in enumerate(board):
            for y, val in enumerate(row):
                if val == "R":
                    rock = (x, y) 
        white = {(x, y) for x, row in enumerate(board) for y, val in enumerate(row)
                if "A" <= val <= "Z" and val != "R"}
        black = {(x, y) for x, row in enumerate(board) for y, val in enumerate(row)
                if "a" <= val <= "z"}
        res = 0
        x, y = rock
        while x < m:
            x += 1
            if (x, y) in white:
                break
            if (x, y) in black:
                res += 1
                break
        x, y = rock
        while y < n:
            y += 1
            if (x, y) in white:
                break
            if (x, y) in black:
                res += 1
                break
        x, y = rock
        while x >= 0:
            x -= 1
            if (x, y) in white:
                break
            if (x, y) in black:
                res += 1
                break
        x, y = rock
        while y >= 0:
            y -= 1
            if (x, y) in white:
                break
            if (x, y) in black:
                res += 1
                break
        return res
    
    
    def numRookCaptures(self, board: List[List[str]]) -> int:
        res = 0
        m, n = len(board), len(board[0])
        for x, row in enumerate(board):
            for y, val in enumerate(row):
                if val == "R":
                    rock = (x, y) 
        xr, yr = rock
        for i ,j in {(0,1), (0,-1), (1,0), (-1,0)}:
            x, y = xr + i, yr + j
            while 0 <= x < m and 0 <= y < n:
                if board[x][y] == "p": 
                    res += 1
                    break
                if board[x][y] != ".":
                    break
                x ,y = x + i, y + j
        return res
