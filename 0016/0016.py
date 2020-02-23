class Solution:
    def threeSumClosest1(self, nums: List[int], target: int) -> int:
        # Time limit exceeds
        res = sum(nums[:3])
        min_ = float('inf')
        def dfs(pos, cur, cnt, sums):
            if cnt == 3:
                sums.add(cur)
            if pos >= len(nums) or cnt >= 3:
                return
            dfs(pos+1, cur+nums[pos], cnt+1, sums)
            dfs(pos+1, cur, cnt, sums)
                
        sums = set()
        dfs(0, 0, 0, sums)
        for i in sums:
            if abs(i-target) == 0:
                return target
            if abs(i-target) < min_:
                min_ = abs(i-target)
                res  = i
        return res
    
    
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = sum(nums[:3])
        min_ = float('inf')
        for lo in range(len(nums)-2):
            tmp = target - nums[lo]
            idx = lo+1
            hi = len(nums)-1
            while idx < hi:
                s = nums[lo]+nums[hi]+nums[idx]
                if abs(s - target) < min_:
                    min_ = abs(s - target)
                    res = s
                if nums[idx] + nums[hi] == tmp:
                    return target
                if nums[idx] + nums[hi] < tmp:
                    idx += 1
                else:
                    hi -= 1
        return res
