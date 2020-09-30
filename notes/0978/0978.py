class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        up = [1]*len(A)
        do = [1]*len(A)
        res = 1
        for i in range(1, len(A)):
            if A[i] > A[i-1]:
                up[i] = do[i-1]+1
            elif A[i] < A[i-1]:
                do[i] = up[i-1]+1
            res = max(res, up[i], do[i])
        return res
