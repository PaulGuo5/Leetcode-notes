class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        
        def num2pos(num):
            r, c = divmod(num-1, n)
            if r%2 != 0:
                c = n - c - 1
            return n - r - 1, c
        
        q = collections.deque([(1, 0)])
        visited = set()
        while q:
            num, step = q.popleft()
            r, c = num2pos(num)
            if board[r][c] != -1:
                num = board[r][c]
            if num == n*n: return step
            for dis in range(1, 7):
                new = dis+num
                if new <= n*n and new not in visited:
                    visited.add(new)
                    q.append((new, step+1))
        return -1
