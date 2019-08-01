class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        res = []
        left, right = [1]*N, [1]*N
        for i in range(1, N):
            left[i] = left[i-1] * nums[i-1]
        for i in range(N-2, -1, -1):
            right[i] = right[i+1] * nums[i+1]
        for i in range(N):
            res.append(left[i]*right[i])
        return res
