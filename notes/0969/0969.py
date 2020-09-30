class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        res = []
        n = len(A)
        for _ in range(n):
            max_val = max(A)
            max_idx = A.index(max_val)
            res.append(max_idx+1)
            A = A[:max_idx+1][::-1] + A[max_idx+1:]
            res.append(len(A))
            A = A[::-1][:-1]
        return res
