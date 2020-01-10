class Solution:
    def minSubArrayLen1(self, s: int, nums: List[int]) -> int:
        if sum(nums) < s:
            return 0
        fst = 0
        lst = 0
        temp_sum = 0
        res = len(nums)
        while lst < len(nums):
            while lst < len(nums) and temp_sum < s:
                temp_sum += nums[lst]
                lst += 1
            while temp_sum >= s:
                temp_sum -= nums[fst]
                fst += 1
            res = min(res,lst-fst+1)            
        return res
            
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if sum(nums) < s:
            return 0
        slow = 0
        tmp = 0
        res = len(nums)
        for fast in range(len(nums)):
            tmp += nums[fast]
            while tmp >= s:
                if res > fast - slow + 1:
                    res = fast - slow + 1
                tmp -= nums[slow]
                slow += 1
        return res