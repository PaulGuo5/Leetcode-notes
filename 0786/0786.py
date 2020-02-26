class Solution:
    def kthSmallestPrimeFraction(self, A: List[int], K: int) -> List[int]:
        # heap: may TLE
        heap = []
        for i in range(len(A)-1):
            for j in range(i+1, len(A)):
                if K > 0:
                    heapq.heappush(heap, (-A[i]/A[j], A[i], A[j]))
                    K -= 1
                else:
                    heapq.heappushpop(heap, (-A[i]/A[j], A[i], A[j]))
        
        return [heap[0][1], heap[0][2]]
        
