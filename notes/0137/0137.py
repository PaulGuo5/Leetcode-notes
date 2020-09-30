class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        i = 0
        while i < len(nums)-2:
            if nums[i] == nums[i+1] and nums[i+1] == nums[i+2]:
                i += 3
            else:
                ans = nums[i]
                break
        if ans == 0:
            ans = nums[i]
        return ans
