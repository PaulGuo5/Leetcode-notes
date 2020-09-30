class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        if not nums: return None
        n = len(nums)
        res = [-1]*n
        nums = nums+nums
        stack = []
        for i in range(len(nums)-1, -1, -1):
            while stack and stack[-1] <= nums[i%n]:
                stack.pop()
            if stack:
                res[i%n] = stack[-1]
            stack.append(nums[i%n])
        return res
