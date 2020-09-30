class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        nums = [1,2,3,4,5,6,7,8,9]
        res = []
        def dfs(pos, cur):
            if low <= cur <= high:
                res.append(cur)
            if cur >= high or pos >= len(nums):
                return
            for i in range(pos, len(nums)):
                if not cur or nums[i] == int(str(cur)[-1])+1:
                    dfs(i+1, cur*10 + nums[i])
        dfs(0, 0)
        return sorted(res)
