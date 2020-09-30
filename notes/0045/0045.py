class Solution:
    def jump(self, nums: List[int]) -> int:
        if not nums: return 0
        far = nums[0]
        near = 0
        res = 0
        for i, n in enumerate(nums):
            if i > near:
                res += 1
                near = far
            far = max(far, n + i)
        return res
