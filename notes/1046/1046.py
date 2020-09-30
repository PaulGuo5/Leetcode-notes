import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for i in stones:
            heapq.heappush(heap, -i)
        # heapq.heapify(stones)
        while len(heap) > 1:
            i = heapq.heappop(heap)
            j = heapq.heappop(heap)
            if -i > -j:
                heapq.heappush(heap, -(j-i))
        return -heap[-1] if heap else 0
