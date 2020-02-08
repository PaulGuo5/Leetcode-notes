class Solution:
    def sortArray_bubble_sort(self, nums: List[int]) -> List[int]:
        # bubble sort: TLE
        if not nums: return None
        for i in range(len(nums)-1):
            for j in range(len(nums)-1, i, -1):
                if nums[j] < nums[j-1]:
                    nums[j], nums[j-1] = nums[j-1], nums[j]
        return nums
    
    def sortArray_selection_sort(self, nums: List[int]) -> List[int]:
        # selection sort: TLE
        if not nums: return None
        for i in range(len(nums)-1):
            min_idx = i
            for j in range(i+1, len(nums)):
                if nums[j] < nums[min_idx]:
                    min_idx = j
            if min_idx != i:
                nums[min_idx], nums[i] = nums[i], nums[min_idx]
        return nums
    
    
    def sortArray_insertion_sort(self, nums: List[int]) -> List[int]:
        # Insertion sort: TLE
        if not nums: return None
        for i in range(1, len(nums)):
            j = i
            target = nums[j]
            while j-1>=0 and target < nums[j-1]:
                nums[j] = nums[j-1]
                j -= 1
            nums[j] = target
        return nums
    
    
    def sortArray_quick_sort(self, nums: List[int]) -> List[int]:
        # quick sort
        if not nums or len(nums) == 1: return nums
        return self.quickSort(nums, 0, len(nums)-1)
        
    def quickSort(self, nums, left, right):
        if left >= right: return
        pivot = self.partition(nums, left, right)
        self.quickSort(nums, left, pivot-1)
        self.quickSort(nums, pivot+1, right)
        return nums
    
    def partition(self, nums, left, right):
        pivot_idx = left
        pivot_val = nums[left]
        while left < right:
            while right > left and nums[right] >= pivot_val:
                right -= 1
            while left < right and nums[left] <= pivot_val:
                left += 1
            nums[left], nums[right] = nums[right], nums[left]
        nums[left], nums[pivot_idx] = nums[pivot_idx], nums[left]
        return left
    
    
    
    def sortArray_counting_sort(self, nums: List[int]) -> List[int]:
        # counting sort: O(n)
        positive = [n for n in nums if n>=0]
        negative = [-n for n in nums if n<0]
        pp = self.countSort(positive)
        nn = self.countSort(negative)
        pp = [] if not pp else pp
        nn_re = [-n for n in nn][::-1] if nn else []
        return nn_re + pp
    
    def countSort(self, nums):
        if not nums: return None
        b = [0 for i in range(len(nums))]
        c = [0 for i in range(max(nums)+1)]
        for n in nums:
            c[n] += 1
        for i in range(1, len(c)):
            c[i] += c[i-1]
        for n in nums:
            b[c[n]-1] = n
            c[n] -= 1
        return b
    
    
    
    def sortArray_bucket_sort(self, nums: List[int]) -> List[int]:
        # bucket sort: O(nlogn)
        if not nums: return None
        def bucketSort(nums):
            max_, min_ = max(nums), min(nums)
            buckets = [0 for _ in range(max_-min_+1)]
            for i in range(len(nums)):
                buckets[nums[i]-min_] += 1
            res = []
            for i in range(len(buckets)):
                res += buckets[i] * [i+min_]
            return res
        return bucketSort(nums)
    
    
    def sortArray(self, nums: List[int]) -> List[int]:
        # Radix sort O(n*m)
        def radixSort(nums, d):
            for i in range(d):
                s = [[] for _ in range(10)]
                for n in nums:
                    s[n//(10**i)%10].append(n)
                nums = [n for b in s for n in b]
            return nums
        
        positive = [n for n in nums if n >= 0]
        negative = [-n for n in nums if n < 0]
        if positive:
            p_res = radixSort(positive, len(str(max(positive))))
        else: return n_res
        if negative:
            n_res = [-n for n in radixSort(negative, len(str(max(negative))))][::-1]
        else: return p_res
        return n_res + p_res
    
