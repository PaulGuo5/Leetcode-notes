class Solution:
    def maxProduct1(self, A) -> int:
        B = A[::-1]
        for i in range(1, len(A)):
            A[i] *= A[i - 1] or 1
            B[i] *= B[i - 1] or 1
        return max(A + B)
    
    
    def maxProduct2(self, nums) -> int:
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        max_cur, min_cur, max_res = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            max_cur, min_cur = max(nums[i], max_cur*nums[i], min_cur*nums[i]),min(nums[i], max_cur*nums[i], min_cur*nums[i])
            max_res = max(max_cur, max_res)
        return max_res
    
    
    def maxProduct(self, nums) -> int:
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        max_cur, min_cur = [0]*len(nums), [0]*len(nums)
        max_cur[0], min_cur[0], max_res = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            max_cur[i] = max(nums[i], max_cur[i-1]*nums[i], min_cur[i-1]*nums[i])
            min_cur[i] = min(nums[i], max_cur[i-1]*nums[i], min_cur[i-1]*nums[i])
            max_res = max(max_cur[i], max_res)
        return max_res
