from heapq import heappush, heappop
class Solution:
    def kthSmallest1(self, matrix: List[List[int]], k: int) -> int:
        res = []
        for l in matrix:
            res += l
        res = sorted(res)
        return res[k-1]
    
    def kthSmallest2(self, matrix: List[List[int]], k: int):
        return sorted(sum(matrix,[]))[k-1]
    
    def kthSmallest3(self, matrix: List[List[int]], k: int):
        return list(heapq.merge(*matrix))[k-1]
    
    def kthSmallest(self, matrix: List[List[int]], k: int):
        heap = []
        heappush(heap, (matrix[0][0], (0, 0)))
        for i in range(k):
            val, loc = heappop(heap)
            if loc[0] + 1 < len(matrix) and loc[1] == 0:
                heappush(heap, (matrix[loc[0] + 1][0], (loc[0] + 1, 0)))
            if loc[1] + 1 < len(matrix):
                heappush(heap, (matrix[loc[0]][loc[1] + 1], (loc[0], loc[1] + 1)))
        return val
