class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if not n: return []
        l, r, t, b = 0, n-1, 0, n-1
        num = 1
        matrix = [[0]*n for _ in range(n)]
        while l <= r and t <= b:
            for i in range(l, r+1):
                matrix[t][i] = num
                num += 1
            t += 1
            for i in range(t, b+1):
                matrix[i][r] = num
                num += 1
            r -= 1
            for i in range(r, l-1, -1):
                matrix[b][i] = num
                num += 1
            b -= 1
            for i in range(b, t-1, -1):
                matrix[i][l] = num
                num += 1
            l += 1
        return matrix
