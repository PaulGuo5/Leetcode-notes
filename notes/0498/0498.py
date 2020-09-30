class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return None
        direct = 1
        i, j = 0, 0
        res = []
        for x in range(len(matrix)*len(matrix[0])):
            res.append(matrix[i][j])
            if direct > 0:
                di, dj = i - 1, j + 1
            else:
                di, dj = i + 1, j - 1
            if 0 <= di < len(matrix) and 0 <= dj < len(matrix[0]):
                i, j = di, dj
            else:
                if direct > 0:
                    if j + 1 < len(matrix[0]):
                        j += 1
                    else:
                        i += 1
                else:
                    if i + 1 < len(matrix):
                        i += 1
                    else:
                        j += 1
                direct *= -1
        return res
            
