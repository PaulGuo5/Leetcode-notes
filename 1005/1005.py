from heapq import heappush, heappop
class Solution:
    def largestSumAfterKNegations1(self, A: List[int], K: int) -> int:
        heap = []
        for i in A:
            heappush(heap,i)
        for i in range(K):
            t = heappop(heap)
            heappush(heap, -t)
        return sum(heap)
    
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        def eachNegations(A):
            A = sorted(A)
            A[0] = -A[0]
            return A
        while K > 0:
            A = eachNegations(A)
            K -= 1
        return sum(A)
