class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        row = [0] * n
        col = [0] * m
        for i, j in indices:
            row[i] += 1
            col[j] += 1
        res = 0
        for i in range(n):
            for j in range(m):
                if (row[i] + col[j]) % 2:
                    res += 1
        return res
