class Solution:
    def beautifulArray(self, N: int) -> List[int]:
        nums = [i for i in range(1, N+1)]
        
        def helper(nums):
            if len(nums) <= 2:
                return nums
            even = nums[::2]
            odd = nums[1::2]
            return helper(even) + helper(odd)
        
        return helper(nums)
