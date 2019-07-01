from heapq import heappush, heappop, heapify
class Solution:
    def findKthLargest1(self, nums: List[int], k: int) -> int:
        return sorted(nums)[-k]
    
    def findKthLargest2(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heappush(heap, num)
        for i in range(len(nums) - k):
            heappop(heap)
        return heap[0]
    
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapify(nums)
        for i in range(len(nums) - k):
            heappop(nums)
        return nums[0]
