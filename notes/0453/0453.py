class Solution:
    def minMoves1(self, nums: List[int]) -> int:
        #time exceed
        nums = sorted(nums)
        cnt = 0
        l = len(nums)
        while max(nums) != min(nums):
            id_max = nums.index(max(nums))
            diff = max(nums) - min(nums)
            cnt += diff
            for i in range(l):
                nums[i] = nums[i] + diff if i != id_max else nums[i]
        return cnt
    
    
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        moves = 0
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == nums[0]:
                break
            moves += nums[i] - nums[0]
        return moves
    
    def minMoves(self, nums: List[int]) -> int:
        return sum(nums) - len(nums)*min(nums)
