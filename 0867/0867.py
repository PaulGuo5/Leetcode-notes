class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        
        res = [[0]*len(A) for j in range(len(A[0]))]
        for i in range(len(A)):
            for j in range(len(A[i])):
                res[j][i] = A[i][j]
        return res
    
    def transpose2(self, A: List[List[int]]) -> List[List[int]]:
        return list(zip(*A))