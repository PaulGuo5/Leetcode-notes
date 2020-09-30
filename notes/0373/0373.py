class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2: return []
        heap = []
        for i in nums1:
            for j in nums2:
                heapq.heappush(heap, (i+j, [i, j]))
        res = []
        while k > 0:
            if heap:
                res.append(heapq.heappop(heap))
                k -= 1
            else:
                break
        return [i[1] for i in res]
