class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        res = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == min(matrix[i]) and matrix[i][j] == max([matrix[x][j] for x in range(len(matrix))]):
                    res.append(matrix[i][j])
        return res
