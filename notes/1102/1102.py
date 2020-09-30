class Solution:
    def maximumMinimumPath(self, A: List[List[int]]) -> int:
        m, n = len(A), len(A[0])
        heap = []
        heapq.heappush(heap, (-A[0][0],0,0))
        visited = set((0,0))
        res = -float('inf')
        while heap:
            value, i, j = heapq.heappop(heap)
            res = max(res, value)
            for x, y in ((0,1),(1,0),(0,-1),(-1,0)):
                if 0 <= x+i < m and 0 <= y+j < n and (x+i, y+j) not in visited:
                    visited.add((x+i, y+j))
                    if x+i == m-1 and y+j == n-1:
                        return -max(res, -A[x+i][y+j])
                    heapq.heappush(heap, (-A[x+i][y+j], x+i, y+j))
