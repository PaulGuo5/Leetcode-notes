class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        keep = [float('inf')]*len(A)
        swap = [float('inf')]*len(A)
        keep[0],swap[0] = 0, 1
        for i in range(1, len(A)):
            if A[i-1] < A[i] and B[i-1] < B[i]:
                keep[i] = keep[i-1]
                swap[i] = swap[i-1]+1
            if A[i-1] < B[i] and B[i-1] < A[i]:
                keep[i] = min(keep[i], swap[i-1])
                swap[i] = min(swap[i], keep[i-1]+1)
        return min(swap[-1],keep[-1])
