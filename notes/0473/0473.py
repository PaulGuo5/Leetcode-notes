class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        if not nums: return False
        n = len(nums)
        side = sum(nums) // 4
        if side* 4 != sum(nums):
            return False
        sides = [0]*4
        nums.sort(reverse=True)
        
        def dfs(index):
            if index == n:
                return sides[0] == sides[1] == sides[2] == side
            for i in range(4):
                if sides[i] + nums[index] <= side:
                    sides[i] += nums[index]
                    if dfs(index+1):
                        return True
                    sides[i] -= nums[index]
            return False
        
        return dfs(0)
