class Solution:
    def findKthLargest1(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        res = []
        while nums:
            res.append(heapq.heappop(nums))
        return res[-k]
    
    def findKthLargest2(self, nums: List[int], k: int) -> int:
        cnt = 0
        res = []
        for n in nums:
            heapq.heappush(res, n)
            cnt += 1
            if cnt > k:
                heapq.heappop(res)
        return heapq.heappop(res)
    
    
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        def buildHeap(nums, length):
            i = length // 2
            while i > 0:
                heapify(nums, length, i)
                i -= 1
            return nums
        
        def heapify(nums, length, i):
            while True:
                max_pos = i
                if 2*i <= length and nums[2*i] > nums[i]:
                    max_pos = 2*i
                if 2*i+1 <= length and nums[2*i+1] > nums[max_pos]:
                    max_pos = 2*i+1
                if max_pos == i:
                    break
                nums[max_pos], nums[i] = nums[i], nums[max_pos]
                i = max_pos
        
        heap = [None] + nums
        length = len(nums)
        heap = buildHeap(heap, length)
        i = len(nums)
        while i > 0:
            heap[i], heap[1] = heap[1], heap[i]
            i -= 1
            heapify(heap, i, 1)
        return heap[-k]
