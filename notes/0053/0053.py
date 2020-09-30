class Solution:
    def maxSubArray1(self, nums: List[int]) -> int:
        #Dynamic method
        tmp = 0
        dynamic_arr = []
        for num in nums:
            tmp = max(tmp+num, num)
            dynamic_arr.append(tmp)
        return max(dynamic_arr)
    
    def maxSubArray(self, nums: List[int]) -> int:
        res, pre = nums[0], nums[0]
        for num in nums[1:]:
            pre = max(pre+num, num)
            res = max(pre, res)
        return res
