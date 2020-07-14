class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)
        for i in range(n-3):
            if 4*nums[i] > target:
                break
            if i-1 >= 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, n-2):
                if 3*nums[j] > target - nums[i]:
                    break
                if j-1 >= i+1 and nums[j] == nums[j-1]:
                    continue
                lo, hi = j+1, n-1
                while lo < hi:
                    tmp = nums[i] + nums[j] + nums[lo] + nums[hi]
                    if target == tmp:
                        res.append([nums[i], nums[j], nums[lo], nums[hi]])
                        while lo < hi and nums[lo] == nums[lo+1]:
                            lo += 1
                        while lo < hi and nums[hi] == nums[hi-1]:
                            hi -= 1
                        hi -= 1
                        lo += 1
                    elif target > tmp:
                        lo += 1
                    else:
                        hi -= 1
        return res
