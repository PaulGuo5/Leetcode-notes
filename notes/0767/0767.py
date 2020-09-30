class Solution:
    def reorganizeString(self, S: str) -> str:
        if not S: return ""
        cnt = collections.Counter(S)
        heap = []
        for key, value in cnt.items():
            heapq.heappush(heap, [-value, key])
        
        res = ""
        pre = heapq.heappop(heap)
        res += pre[1]
        
        while heap:
            cur = heapq.heappop(heap)
            res += cur[1]
            
            pre[0] += 1
            if pre[0] < 0:
                heapq.heappush(heap, pre)
            pre = cur
            
        return res if len(res) == len(S) else ""
