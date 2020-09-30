class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        if not nums:
            return res
        nums = sorted(nums)
        if nums[0] > 0:
            return res
        for i in range(len(nums)-2):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            target = - nums[i]
            left, right = i + 1, len(nums)-1
            while left < right:
                if nums[left] + nums[right] == target:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left+1] == nums[left]:
                        left += 1
                    while left < right and nums[right-1] == nums[right]:
                        right -= 1
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] < target:
                    left += 1
                elif nums[left] + nums[right] > target:
                    right -= 1
        return res