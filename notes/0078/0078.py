class Solution:
    def subsets1(self, nums: List[int]) -> List[List[int]]:
        # iterative
        res = [[]]
        for n in nums:
            for i in range(len(res)):
                res.append(res[i]+[n])
        return res
    
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # dfs
        def dfs(nums, start, path, res):
            res.append(path)
            for i in range(start, len(nums)):
                dfs(nums, i+1, path+[nums[i]], res)
        res = []
        dfs(nums, 0, [], res)
        return res
