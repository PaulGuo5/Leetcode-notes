class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        s = sum(nums)
        if s % k != 0: return False
        target = s//k
        visited = [False]*len(nums)
        
        def helper(k, pos, cur):
            if k == 0: return True
            if cur == target:
                return helper(k-1, 0, 0)
            for i in range(pos, len(nums)):
                if not visited[i] and cur+nums[i] <= target:
                    visited[i] = True
                    if helper(k, i+1, cur+nums[i]):
                        return True
                    visited[i] = False
            return False
        
        return helper(k, 0, 0)
