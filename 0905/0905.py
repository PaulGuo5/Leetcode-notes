class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        left=[]
        right=[]
        for i in range(len(A)):
            t = A[i] % 2
            if t == 0:
                left.append(A[i])
            else:
                right.append(A[i])
        return left+right