class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        
        def max_L_M(L, M):
            maxL, res = 0, 0
            for i in range(M+L, len(prefix_sum)):
                maxL = max(maxL, prefix_sum[i-M]-prefix_sum[i-M-L])
                res = max(res, maxL+prefix_sum[i]-prefix_sum[i-M])
            return res
        
        prefix_sum = [0]*(len(A)+1)
        for i in range(len(A)):
            prefix_sum[i+1] = prefix_sum[i] + A[i]
        return max(max_L_M(L, M), max_L_M(M, L))
