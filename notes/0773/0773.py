class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        m, n = len(board), len(board[0])
        target = tuple([i for i in range(1, m*n)]+[0])
        start = tuple([i for j, row in enumerate(board) for i in row])
        pos = list(start).index(0)
        q = collections.deque([(start, pos, 0)])
        visited = {start}
        while q:
            state, pos, steps = q.popleft()
            if state == target:
                return steps
            for dist in ((0,1),(0,-1),(-1,0),(1,0)):
                x, y = pos//n, pos%n
                nx, ny = dist[0]+x, dist[1]+y
                if 0 <= nx < m and 0 <= ny < n:
                    nboard = list(state)
                    s_idx = nx*n+ny
                    nboard[s_idx], nboard[pos] = nboard[pos], nboard[s_idx]
                    ntuple = tuple(nboard)
                    if ntuple not in visited:
                        visited.add(ntuple)
                        q.append((ntuple, s_idx, steps+1))
        return -1
