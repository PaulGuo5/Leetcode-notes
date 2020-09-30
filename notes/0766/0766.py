class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        # m = len(matrix)
        # n = len(matrix[0])
        # for i in range(m-1):
        #     for j in range(n-1):
        #         if matrix[i+1][j+1] != matrix[i][j]:
        #             return False
        # return True
        return all(matrix[i+1][j+1] == matrix[i][j] for i in range(len(matrix)-1) for j in range(len(matrix[0])-1))
    
    def isToeplitzMatrix1(self, matrix: List[List[int]]) -> bool:
        return all(r1[:-1] == r2[1:] for r1, r2 in zip(matrix[:-1], matrix[1:]))
