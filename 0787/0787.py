class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = collections.defaultdict(dict)
        heap = [(0, src, K+1)]
        for s, d, v in flights: graph[s][d] = v
        print(graph)
        while heap:
            cost, s, k = heapq.heappop(heap)
            if s == dst: return cost
            if k:
                for d in graph[s]:
                    heapq.heappush(heap, (cost+graph[s][d], d, k-1) )
        return -1
