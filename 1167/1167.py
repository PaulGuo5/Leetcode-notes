class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        stack = []
        for s in sticks:
            heapq.heappush(stack, s)
        res = 0
        while len(stack) > 1:
            tmp = heapq.heappop(stack) + heapq.heappop(stack)
            res += tmp
            heapq.heappush(stack, tmp)
        return res
