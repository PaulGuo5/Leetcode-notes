class Solution:
    def kthSmallestPrimeFraction1(self, A: List[int], K: int) -> List[int]:
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
    
    
    def kthSmallestPrimeFraction(self, A: List[int], K: int) -> List[int]:
        n = len(A)
        low = 0.0
        high = 1.0
        while low < high:
            mid = (low+high) / 2
            j = 1
            total = 0
            tmp_max = 0
            for i in range(n-1):
                while j < n and A[i] > mid * A[j]:
                    j += 1
                if j == n: break
                total += n-j
                tmp = A[i] / A[j]
                if tmp > tmp_max:
                    tmp_max, x, y = tmp, i, j
            if total == K:
                return [A[x], A[y]]
            elif total < K:
                low = mid
            else:
                high = mid
        return []
    
           
